#!/usr/bin/env python3
# coding: utf8

import scat.util as util
import struct
import logging
import binascii
from collections import namedtuple
import zlib
from inspect import currentframe, getframeinfo
from pathlib import Path
import os, sys

class IntelParser:
    def __init__(self):
        self.io_device = None
        self.writer = None

        self.name = 'intel'
        self.shortname = 'imc'

        self.logger = logging.getLogger('scat.intelparser')

        self.process = { }
        self.no_process = { }

        # for p in self.diag_log_parsers:
        #     self.process.update(p.process)
        #     try:
        #         self.no_process.update(p.no_process)
        #     except AttributeError:
        #         pass

        self.msgs = False

    def set_io_device(self, io_device):
        self.io_device = io_device

    def set_writer(self, writer):
        self.writer = writer

    def set_parameter(self, params):
        for p in params:
            if p == 'log_level':
                self.logger.setLevel(params[p])
            elif p == 'msgs':
                self.msgs = params[p]
            elif p == 'combine-stdout':
                self.combine_stdout = params[p]

    def init_diag(self):
        pass

    def prepare_diag(self):
        pass

    def parse_diag(self, pkt, hdlc_encoded = True, check_crc = True, args = None):
        if len(pkt) < 3:
            return

        if hdlc_encoded:
            pkt = util.unwrap(pkt)

        if check_crc:
            crc = util.dm_crc16(pkt[:-2])
            crc_pkt = struct.unpack('<H', pkt[-2:])[0]

            crc32 = zlib.crc32(pkt[:-4])
            crc32_pkt = struct.unpack('<L', pkt[-4:])[0]

            if crc == crc_pkt:
                # CRC16
                pkt = pkt[:-2]
            elif crc32 == crc32_pkt:
                # CRC32
                pkt = pkt[:-4]
            else:
                self.logger.log(logging.WARNING, "Neither CRC16 nor CRC32 mismatch: CRC16: {:#06x}/{:#06x}, CRC32 {:#10x}/{:#10x}".format(
                    crc, crc_pkt, crc32, crc32_pkt))
                self.logger.log(logging.DEBUG, util.xxd(pkt))
                return None

        return self.parse_diag_log(pkt)

    def run_diag(self):
        pass

    def stop_diag(self):
        pass

    def run_dump(self):
        self.logger.log(logging.INFO, 'Starting diag from dump')

        oldbuf = b''
        loop = True
        cur_pos = 0
        try:
            while loop:
                buf = self.io_device.read(0x90000)
                if len(buf) == 0:
                    if self.io_device.block_until_data:
                        continue
                    else:
                        loop = False

                last_pkt_pos = buf.rfind(b'\x7e')
                if last_pkt_pos > 0:
                    buf_t = oldbuf + buf[0:last_pkt_pos]
                    oldbuf = buf[last_pkt_pos:]
                    buf = buf_t
                else:
                    buf = oldbuf + buf

                buf_atom = buf.split(b'\x7e')

                for pkt in buf_atom:
                    if len(pkt) == 0:
                        continue
                    parse_result = self.parse_diag(pkt)

                    if parse_result is not None:
                        self.postprocess_parse_result(parse_result)

        except KeyboardInterrupt:
            return

    def read_dump(self):
        while self.io_device.file_available:
            self.logger.log(logging.INFO, "Reading from {}".format(self.io_device.fname))
            if self.io_device.fname.find('.istp') > 0:
                self.run_dump()
            else:
                self.logger.log(logging.INFO, 'Unknown baseband dump type, assuming ISTP')
                self.run_dump()
            self.io_device.open_next_file()

    def postprocess_parse_result(self, parse_result):
        if 'radio_id' in parse_result:
            radio_id = parse_result['radio_id']
        else:
            radio_id = 0

        if 'ts' in parse_result:
            ts = parse_result['ts']
        else:
            ts = None

        if 'cp' in parse_result:
            for sock_content in parse_result['cp']:
                self.writer.write_cp(sock_content, radio_id, ts)

        if 'up' in parse_result:
            for sock_content in parse_result['up']:
                self.writer.write_up(sock_content, radio_id, -1, ts)

        if 'stdout' in parse_result:
            if len(parse_result['stdout']) > 0:
                if self.combine_stdout:
                    for l in parse_result['stdout'].split('\n'):
                        osmocore_log_hdr = util.create_osmocore_logging_header(
                            timestamp = ts,
                            process_name = Path(sys.argv[0]).name,
                            pid = os.getpid(),
                            level = 3,
                            subsys_name = self.__class__.__name__,
                            filename = Path(__file__).name,
                            line_number = getframeinfo(currentframe()).lineno
                        )
                        gsmtap_hdr = util.create_gsmtap_header(
                            version = 2,
                            payload_type = util.gsmtap_type.OSMOCORE_LOG)
                        self.writer.write_cp(gsmtap_hdr + osmocore_log_hdr + l.encode('utf-8'), radio_id, ts)
                else:
                    for l in parse_result['stdout'].split('\n'):
                        print('Radio {}: {}'.format(radio_id, l))

    log_header = namedtuple('IntelLogHeader', 'type seq_nr ts')
    stream_0x00_header = namedtuple('Intel0x00Header', 'ts0 ts1 cmd_id')

    def parse_diag_log(self, pkt, args=None):
        if len(pkt) < 2:
            print('Packet length shorter than 0x02: ' + binascii.hexlify(pkt).decode('utf-8'))
            return None

        stream = pkt[0]
        seq_nr = pkt[1]

        # print('{:#04x}/{:#04x} '.format(stream, seq_nr) + binascii.hexlify(pkt[2:]).decode('utf-8'))
        if stream == 0:
            if len(pkt) < 9:
                return None
            cmd_hdr = self.stream_0x00_header._make(struct.unpack('<LBH', pkt[2:9]))
            # https://github.com/xmm7360/xmm7360-pci/blob/master/trace/trace.py
            if cmd_hdr.cmd_id == 0x10:
                print(str(cmd_hdr) + ' ' + pkt[9:].decode('utf-8', errors='ignore'))
            elif cmd_hdr.cmd_id == 0x11:
                print(str(cmd_hdr) + ' ' + pkt[9:].decode('utf-8', errors='ignore'))
            elif cmd_hdr.cmd_id == 0x18:
                print(str(cmd_hdr) + ' ' + binascii.hexlify(pkt[9:]).decode('utf-8'))
        else:
            return None
            header = self.log_header._make(struct.unpack('<BBL', pkt[0:6]))
            content = pkt[6:]
            print(str(header) + ' ' + binascii.hexlify(content).decode('utf-8'))
        return None

__entry__ = IntelParser

def name():
    return 'intel'

def shortname():
    return 'imc'
