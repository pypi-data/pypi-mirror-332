#!/usr/bin/env python3

import struct
import calendar
import logging
import binascii
from collections import namedtuple

import scat.util as util
import scat.parsers.qualcomm.diagcmd as diagcmd

class DiagNrLogParser:
    def __init__(self, parent):
        self.parent = parent

        i = diagcmd.diag_log_get_lte_item_id
        c = diagcmd.diag_log_code_5gnr
        self.process = {
            # Management Layer 1
            i(c.LOG_5GNR_ML1_MEAS_DATABASE_UPDATE): lambda x, y, z: self.parse_nr_ml1_meas_db_update(x, y, z),

            # MAC
            0xB88A: lambda x, y, z: self.parse_nr_mac_rach_attempt(x, y, z), # NR MAC RACH Attempt

            # RRC
            i(c.LOG_5GNR_RRC_OTA_MESSAGE): lambda x, y, z: self.parse_nr_rrc(x, y, z),
            i(c.LOG_5GNR_RRC_MIB_INFO): lambda x, y, z: self.parse_nr_mib_info(x, y, z),
            i(c.LOG_5GNR_RRC_SERVING_CELL_INFO): lambda x, y, z: self.parse_nr_rrc_scell_info(x, y, z),
            # i(0x0824): lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB824),
            i(c.LOG_5GNR_RRC_CONFIGURATION_INFO): lambda x, y, z: self.parse_nr_rrc_conf_info(x, y, z),
            i(c.LOG_5GNR_RRC_SUPPORTED_CA_COMBOS): lambda x, y, z: self.parse_nr_cacombos(x, y, z),

            # 0xB827: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB827), # NR5G RRC PLMN Search Request
            # 0xB828: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB828), # NR5G RRC PLMN Search Response
            # 0xB82B: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB82b), # NR5G RRC Detected Cell Info
            # 0xB82C: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB82c), # NR5G RRC Blacklist Update
            # 0xB832: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB832), # NR5G RRC Misc Blacklist Update
            # 0xB837: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB837), # NR5G RRC Page Share

            # NAS
            i(c.LOG_5GNR_NAS_5GSM_PLAIN_OTA_INCOMING_MESSAGE): lambda x, y, z: self.parse_nr_nas(x, y, z, 0xB800),
            i(c.LOG_5GNR_NAS_5GSM_PLAIN_OTA_OUTGOING_MESSAGE): lambda x, y, z: self.parse_nr_nas(x, y, z, 0xB801),
            i(c.LOG_5GNR_NAS_5GSM_SEC_OTA_INCOMING_MESSAGE): lambda x, y, z: self.parse_nr_nas(x, y, z, 0xB808),
            i(c.LOG_5GNR_NAS_5GSM_SEC_OTA_OUTGOING_MESSAGE): lambda x, y, z: self.parse_nr_nas(x, y, z, 0xB809),
            i(c.LOG_5GNR_NAS_5GMM_PLAIN_OTA_INCOMING_MESSAGE): lambda x, y, z: self.parse_nr_nas(x, y, z, 0xB80A),
            i(c.LOG_5GNR_NAS_5GMM_PLAIN_OTA_OUTGOING_MESSAGE): lambda x, y, z: self.parse_nr_nas(x, y, z, 0xB80B),
            i(c.LOG_5GNR_NAS_5GMM_PLAIN_OTA_CONTAINER_MESSAGE): lambda x, y, z: self.parse_nr_nas(x, y, z, 0xB814),
            i(c.LOG_5GNR_NAS_5GMM_STATE): lambda x, y, z: self.parse_nr_mm_state(x, y, z),

            # 0xB803: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB803), # NR5G NAS SNPN CONFIG LIST INFO
            # 0xB804: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB804), # MM5G RRC PAGE IND
            # 0xB805: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB805), # MM5G Serv Req Status Info
            # 0xB80D: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB80D), # NR5G NAS MM5G Service Request
            # 0xB80E: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB80E), # NR5G NAS MM5G Current Security Context
            # 0xB80F: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB80F), # NR5G NAS MM5G Security Context Keys
            # 0xB810: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB810), # NR5G NAS MM5G Native Security Context
            # 0xB811: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB811), # NR5G NAS MM5G Authentication Keys
            # 0xB812: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB812), # NR5G NAS MM5G Forbidden TAI List
            # 0xB813: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB813), # NR5G NAS MM5G Service Area List
            # 0xB814: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB814), # NR5G NAS Plain Message Container
            # 0xB815: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB815), # NR5G NAS MM5G NSSAI Info

            # NR PDCP
            # 0xB840: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB840), # NR PDCP DL Data PDU
            # 0xB841: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB841), # NR PDCP DL Control PDU
            # 0xB842: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB842), # NR PDCP DL Rbs Stats
            # 0xB843: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB843),
            # 0xB844: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB844), # NR5G PDCP DL SRB PDU
            # 0xB847: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB847), # NR5G PDCP DL ROHC RB Stats
            # 0xB848: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB848), # NR5G PDCP DL Debug PDU LOG

            # 0xB860: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB860), # NR PDCP UL Stats
            # 0xB861: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB861), # NR PDCP UL Control PDU
            # 0xB862: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB862),
            # 0xB863: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB863), # NR5G PDCP UL ROHC Stats

            # NR RLC
            # 0xB84B: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB84B), # NR L2 DL Config
            # 0xB84D: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB84D), # NR RLC DL Stats
            # 0xB84E: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB84E), # NL RLC DL Stats PDU

            # 0xB868: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB868), # NR RLC UL Stats
            # 0xB869: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB869), # NR RLC UL Stats PDU

            # Obsolete
            # 0xB84C: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB84C), # NR5G RLC DL Control PDU
            # 0xB858: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB858), # NR5G L2 DL MCE
            # 0xB880: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB880), # NR5G MAC UL TB
            # 0xB891: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB891), # NR5G MAC LL1 CSF Indication
            # 0xB8A0: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8A0), # NR5G MAC LL1 PUSCH Tx
            # 0xB975: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB975), # NR5G ML1 Serving Cell Beam Management

            # NR L2
            # 0xB856: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB856), # NR
            # 0xB857: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB857), # NR L2 DL Data PDU

            # 0xB870: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB870), # NR L2 UL Data PDU
            # 0xB871: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB871), # NR L2 UL Config
            # 0xB872: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB872), # NR L2 UL TB
            # 0xB873: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB873), # NR5G L2 UL BSR

            # NR MAC
            # 0xB881: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB881), # NR5G MAC UL TB Stats
            # 0xB882: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB882), #
            # 0xB883: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB883), # NR5G MAC UL Physical Channel Schedule Report
            # 0xB884: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB884), # NR5G MAC UL Physical Channel Power Control
            # 0xB885: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB885), # NR5G MAC DCI Info
            # 0xB886: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB886), # NR5G MAC DL TB Report
            # 0xB887: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB887), # NR5G MAC PDSCH Status
            # 0xB888: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB888), # NR5G MAC PDSCH Stats
            # 0xB889: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB889), # NR5G MAC RACH Trigger
            # 0xB88A: lambda x, y, z: self.parse_nr_mac_rach_attempt(x, y, z), # NR5G MAC RACH Attempt
            # 0xB88B: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB88B), #
            # 0xB88C: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB88C),
            # 0xB88D: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB88D),
            # 0xB88F: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB88F),

            # 0xB890: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB890), # NR5G MAC CDRX Events Info
            # 0xB896: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB896), # NR5G MAC UCI Payload Information
            # 0xB897: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB897),
            # 0xB89B: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB89B), # NR5G MAC UCI Information
            # 0xB89C: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB89C), # NR5G MAC Flow Control
            # 0xB89D: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB89D),
            # 0xB89E: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB89E),

            # 0xB8A1: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8A1), # NR5G MAC Symbol Arbitration
            # 0xB8A3: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8A3),
            # 0xB8A4: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8A4),
            # 0xB8A6: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8A6),
            # 0xB8A7: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8A7), # NR5G MAC CSF Report
            # 0xB8A8: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8A8),
            # 0xB8AE: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8AE), # NR5G MAC Skip UL TX
            # 0xB8AF: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8AF), # NR5G MAC Link Latency
            # 0xB8B0: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8B0), # NR5G MAC TX IQ Capture
            # 0xB8B3: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8B3), # NR5G MAC TX SHARING INFO LOG
            # 0xB8B5: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8B5), # NR5G MAC Tx Pwr Dist Stats LOG
            # 0xB8B8: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8B8), # NR5G MAC Metric Filter Result LOG

            # NR LL1
            # 0xB8C0: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8C0),
            # 0xB8C4: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8C4),
            # 0xB8C5: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8C5),
            # 0xB8C6: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8C6), # NR5G LL1 FW RX Control FTL
            # 0xB8C7: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8C7), # NR5G LL1 FW RX Control TTL
            # 0xB8C8: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8C8), # NR5G LL1 FW RX Control CCH
            # 0xB8C9: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8C9), # NR5G LL1 FW RX Control AGC
            # 0xB8CA: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8CA),
            # 0xB8CB: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8CB),
            # 0xB8CD: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8CD),
            # 0xB8CE: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8CE),

            # 0xB8D1: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8D1), # NR5G LL1 FW TX IU RF
            # 0xB8D2: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8D2), # NR5G LL1 FW MAC TX IU Power
            # 0xB8D3: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8D3),
            # 0xB8D8: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8D8), # NR5G LL1 LOG SERVING SNR
            # 0xB8DA: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8DA), # NR5G LL1 FW UL FTL
            # 0xB8DD: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8DD),
            # 0xB8DE: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8DE),
            # 0xB8E0: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8E0),
            # 0xB8E2: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB8E2),

            # ML1
            # 0xB950: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB950), # NR5G ML1 DL Common Config
            # 0xB951: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB951),
            # 0xB952: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB952),
            # 0xB954: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB954),
            # 0xB955: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB955),
            # 0xB956: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB956),
            # 0xB958: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB958),
            # 0xB959: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB959), # NR5G ML1 RLM Stats
            # 0xB95B: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB95B),
            # 0xB95C: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB95C),
            # 0xB95D: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB95D),
            # 0xB960: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB960),
            # 0xB969: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB969), # NR5G ML1 Searcher FW Cell Meas Request
            # 0xB96A: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB96A),
            # 0xB96B: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB96B),
            # 0xB96C: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB96C),
            # 0xB96D: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB96D), # NR5G ML1 Searcher ACQ Config And Response
            # 0xB96E: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB96E),
            # 0xB96F: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB96F), # NR5G ML1 Searcher Conn Eval
            # 0xB970: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB970), # NR5G ML1 Searcher Idle S Criteria
            # 0xB974: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB974),
            # 0xB977: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB977),
            # 0xB979: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB979),
            # 0xB97C: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB97C),
            # 0xB980: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB980),
            # 0xB981: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB981), # NR5G ML1 FC Information
            # 0xB982: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB982),
            # 0xB983: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB983),
            # 0xB986: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB986),
            # 0xB987: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB987),
            # 0xB989: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB989),
            # 0xB98A: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB98A),
            # 0xB98B: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB98B), # NR5G ML1 QMI Handler
            # 0xB98F: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB98F), # NR5G ML1 Antenna Switch Diversity
            # 0xB996: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB996), # NR5G ML1 SERVICES SRS INFO LOG
            # 0xB999: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB999), # NR5G ML1 OA UAI INFO S
            # 0xB9A3: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB9A3),
            # 0xB9A4: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB9A4), # NR5G ML1 BFR Ind
            # 0xB9A5: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB9A5), # NR5G ML1 RLM BFD IND
            # 0xB9A7: lambda x, y, z: self.parse_nr_stub(x, y, z, 0xB9A7), # NR5G ML1 DLM2 CA Metrics Request
        }

    def parse_nr_stub(self, pkt_ts, pkt, radio_id, item_id):
        if self.parent:
            self.parent.logger.log(logging.WARNING, "NR_STUB " + hex(item_id) + " " + util.xxd_oneline(pkt))

    def parse_nr_0xb80c(self, pkt_ts, pkt, radio_id):
        # 01 00 00 00 | 01 02 00 62 f2 20 ff ff ff ff ff ff ff ff ff ff ff ff 01 00 00 00
        pass

    # ML1
    def parse_float_q7(self, intnum):
        intval = (intnum & 0xfffffff80) >> 7
        if intval > 0x1000000:
            intval = -1 * (0x2000000 - intval)
        floatval = (intval & 0x7f) / 128

        return floatval + intval

    # ML1
    def parse_nr_ml1_meas_db_update(self, pkt_header, pkt_body, args):
        version = struct.unpack('<L', pkt_body[0:4])[0]
        stdout = ''

        if version == 0x00020007:
            # Found in RM500Q
            # num layers, ssb periodicity, reserved, frequency offset (/1024), timing offset
            v = struct.unpack('<BBHLL', pkt_body[4:16])
            num_layers = v[0]

            i = 0
            content = pkt_body[16:]
            for x in range(num_layers):
                # ARFCN, num cells, serving cell index, serving cell PCI, serving SSB (& 0xf)
                v2 = content[i:i+12]
                v2 = struct.unpack('<LBBHL', v2)
                i += 12

                # RSRP of secondary path (2x, 25b int, 7b frac), RX beam (2x, 2B), RFIC ID (2B), Reserved (2B)
                v3 = content[i:i+16]
                v3 = struct.unpack('<LLHHHH', v3)
                sec_rsrp_0 = self.parse_float_q7(v3[0])
                sec_rsrp_1 = self.parse_float_q7(v3[1])
                i += 16

                stdout += 'NR ML1 SCell: NR-ARFCN {}/PCI {:4d}/SSB: {}, Secondary Path RSRP: {:.2f}/{:.2f}, RX beam: {}/{}, # cells {} (S: {})\n'.format(
                    v2[0], v2[3], v2[4] & 0xf,
                    sec_rsrp_0, sec_rsrp_1,
                    v3[2] if v3[2] != 0xffff else 'NA',
                    v3[3] if v3[3] != 0xffff else 'NA', v2[1], v2[2])

                # Serving subarray ID (2x, 2B)
                v4 = content[i:i+4]
                v4 = struct.unpack('<HH', v4)
                i += 4

                for y in range(v2[1]):
                    # PCI, PBCH SFN, # beams (1B), reserved (3B), RSRP, RSRQ
                    cell_meas = struct.unpack('<HHLLL', content[i:i+16])
                    stdout += '└── NR ML1 Cell {}: PCI {:4d}, PBCH SFN: {:4d}, RSRP: {:.2f}, RSRQ: {:.2f}, # beams: {}\n'.format(
                        y, cell_meas[0], cell_meas[1], self.parse_float_q7(cell_meas[3]),
                        self.parse_float_q7(cell_meas[4]), cell_meas[2] & 0xf
                    )
                    i += 16

                    for z in range(cell_meas[2] & 0xf):
                        # SSB index (2B), reserved (2B), beam ID (2x2B), Reserved (4B), SSB ref timing (2x4B), beam RSRP (2x4B), RSRP-Nr2Nr, RSRQ-Nr2Nr, RSRP-L2Nr, RSRQ-L2Nr (all 4B)
                        beam = content[i:i+44]
                        beam = struct.unpack('<HHHHL LL LL LL LL', beam)
                        stdout += '    └── Beam {}: SSB[{}] Beam ID {}/{}, RSRP {:.2f}/{:.2f}, Filtered (Nr2Nr) RSRP/RSRQ: {:.2f}/{:.2f}, Filtered (L2Nr) RSRP/RSRQ: {:.2f}/{:.2f}\n'.format(
                            z, beam[0], beam[2], beam[3],
                            self.parse_float_q7(beam[7]), self.parse_float_q7(beam[8]),
                            self.parse_float_q7(beam[9]), self.parse_float_q7(beam[10]),
                            self.parse_float_q7(beam[11]), self.parse_float_q7(beam[12])
                        )
                        i += 44
            return {'stdout': stdout.rstrip()}
        elif version == 0x00020009:
            # system time, num layers, ssb periodicity, reserved, frequency offset (/1024), timing offset
            v = struct.unpack('<LBBHLL', pkt_body[4:20])
            num_layers = v[1]

            i = 0
            content = pkt_body[20:]
            for x in range(num_layers):
                # ARFCN, cc_id, num cells, serving cell PCI, serving cell index, serving SSB, reserved
                v2 = content[i:i+12]
                v2 = struct.unpack('<LBBHBBH', v2)
                i += 12

                # RSRP of secondary path (2x, 25b int, 7b frac), RX beam (2x, 2B), RFIC ID (2B), Reserved (2B)
                v3 = content[i:i+16]
                v3 = struct.unpack('<LLHHHH', v3)
                sec_rsrp_0 = self.parse_float_q7(v3[0])
                sec_rsrp_1 = self.parse_float_q7(v3[1])
                i += 16

                stdout += 'NR ML1 SCell: NR-ARFCN {}/PCI {:4d}/SSB: {}, Secondary Path RSRP: {:.2f}/{:.2f}, RX beam: {}/{}, # cells {} (S: {})\n'.format(
                    v2[0], v2[3], v2[5] & 0xf,
                    sec_rsrp_0, sec_rsrp_1,
                    v3[2] if v3[2] != 0xffff else 'NA',
                    v3[3] if v3[3] != 0xffff else 'NA', v2[2], v2[4])

                # Serving subarray ID (2x, 2B)
                v4 = content[i:i+4]
                v4 = struct.unpack('<HH', v4)
                i += 4

                for y in range(v2[2]):
                    # PCI, PBCH SFN, # beams (1B), reserved (3B), RSRP, RSRQ
                    cell_meas = struct.unpack('<HHLLL', content[i:i+16])
                    stdout += '└── NR ML1 Cell {}: PCI {:4d}, PBCH SFN: {:4d}, RSRP: {:.2f}, RSRQ: {:.2f}, # beams: {}\n'.format(
                        y, cell_meas[0], cell_meas[1], self.parse_float_q7(cell_meas[3]),
                        self.parse_float_q7(cell_meas[4]), cell_meas[2] & 0xf
                    )
                    i += 16

                    for z in range(cell_meas[2] & 0xf):
                        # SSB index (2B), reserved (2B), beam ID (2x2B), Reserved (4B), SSB ref timing (2x4B), beam RSRP (2x4B), RSRP-Nr2Nr, RSRQ-Nr2Nr, RSRP-L2Nr, RSRQ-L2Nr (all 4B)
                        beam = content[i:i+44]
                        beam = struct.unpack('<HHHHL LL LL LL LL', beam)
                        stdout += '    └── Beam {}: SSB[{}] Beam ID {}/{}, RSRP {:.2f}/{:.2f}, Filtered (Nr2Nr) RSRP/RSRQ: {:.2f}/{:.2f}, Filtered (L2Nr) RSRP/RSRQ: {:.2f}/{:.2f}\n'.format(
                            z, beam[0], beam[2], beam[3],
                            self.parse_float_q7(beam[7]), self.parse_float_q7(beam[8]),
                            self.parse_float_q7(beam[9]), self.parse_float_q7(beam[10]),
                            self.parse_float_q7(beam[11]), self.parse_float_q7(beam[12])
                        )
                        i += 44
            return {'stdout': stdout.rstrip()}
        else:
            if self.parent:
                self.parent.logger.log(logging.WARNING, 'Unknown NR ML1 Measurement Database Update packet version {:#x}'.format(version))
                self.parent.logger.log(logging.DEBUG, "Body: {}".format(util.xxd_oneline(pkt_body)))

    # MAC

    def frame_subframe(self, rawval):
        frame = (rawval & 0x03ff)
        subframe = (rawval & 0xfc00) >> 10
        return (frame, subframe)

    def parse_nr_mac_rach_attempt(self, pkt_header, pkt_body, args):
        version = struct.unpack('<L', pkt_body[0:4])[0]
        stdout = ''

        if version == 0x00020007:
            # Log fields change: sleep, r1, r2, dl dynamic cfg change, dl config, (ul config, ml1 state), r3, bmask
            v = struct.unpack('<BBBBBBHH', pkt_body[4:14])

            # subscription ID
            v = struct.unpack('<B', pkt_body[14:15])

            # num records, num attempt, ssb id, csi rs id, carrier id
            # RACH result, contention type, RACH msg bitmask, msg1 scs, ul bwp scs, reserved
            v = struct.unpack('<BHBBBBBBBBH', pkt_body[15:28])
            num_records = v[0]
            num_attempt = v[1]
            ssb_id = v[2]
            csi_rs_id = v[3]
            carrier_id = v[4]
            rach_result = v[5]
            contention_type = v[6]
            rach_msg_bitmask = v[7]
            msg1_scs = v[8]
            ul_bwp_scs = v[9]

            rach_result_map = {
                0: 'SUCCESS',
                1: 'FAILURE_MSG2_RA_TIMER_EXP',
                2: 'FAILURE_MSG2_RAPID_MISMATCH',
                3: 'FAILURE_MSG2_RAR_PRUNE',
                4: 'BOI_ONLY_MSG2',
                5: 'FAILURE_MSG4_CT_TIMER_EXPIRED',
                6: 'FAILURE_MSG4_CT_RESOLUTION_NOT_PASSED',
                7: 'ABORTED',
                8: 'SUSPENDED',
                9: 'RESUMED'
            }

            contention_type_map = {
                0: 'CONT_FREE',
                1: 'CONT_DL_MCE',
                2: 'CONT_UL_GRANT',
                3: 'PDCCH_CRNTI'
            }

            msg1_scs_map = {
                0: 1.25,
                1: 5,
                2: 15,
                3: 30,
                4: 60,
                5: 120,
                6: 240
            }

            ul_bwp_scs_map = {
                0: 15,
                1: 30,
                2: 60,
                3: 120,
                4: 240,
                5: 0
            }

            mac_log_scs_map = {
                0: 15,
                1: 30,
                2: 60,
                3: 120,
                4: 0,
                5: 0
            }

            if rach_result in rach_result_map:
                rach_result_str = rach_result_map[rach_result]
            else:
                rach_result_str = 'UNKNOWN'

            if contention_type in contention_type_map:
                contention_type_str = contention_type_map[contention_type]
            else:
                contention_type_str = 'UNKNOWN'

            if msg1_scs in msg1_scs_map:
                msg1_scs_val = msg1_scs_map[msg1_scs]
            else:
                msg1_scs_val = 0

            if ul_bwp_scs in ul_bwp_scs_map:
                ul_bwp_scs_val = ul_bwp_scs_map[ul_bwp_scs]
            else:
                ul_bwp_scs_val = 0

            stdout += "NR MAC RACH Attempt: {} {} {} {} {} {} {} Msg1 SCS: {} UL BWP SCS: {}\n".format(num_records, num_attempt, ssb_id, csi_rs_id,
                                                                        carrier_id, rach_result_str,
                                                                        contention_type_str, msg1_scs_val,
                                                                        ul_bwp_scs_val)

            pos = 28

            if rach_msg_bitmask & 0x01:
                # Msg1
                # frame/subframe 10b/6b, slot, scs
                v = struct.unpack('<HBB', pkt_body[pos:pos+4])
                frame, subframe = self.frame_subframe(v[0])
                slot = v[1]
                scs = v[2]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg1: Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                pos += 4

                # symbol start, prach config, preamble format, RA id, FDM, Uroot, cyclic shift v, RA-RNTI
                v = struct.unpack('<BBBBHHHH', pkt_body[pos:pos+12])
                stdout += "NR MAC RACH Msg1: Symbol start {} PRACH config {} Preamble {} RA ID {} FDM {} Uroot {} Cyclic shift {} RA-RNTI {}\n".format(v[0],
                                                                v[1], v[2], v[3],
                                                                v[4], v[5], v[6], v[7])
                pos += 12

                # RAR window start/end SFN, backoff duration
                v = struct.unpack('<HBBHBBL', pkt_body[pos:pos+12])
                frame, subframe = self.frame_subframe(v[0])
                slot = v[1]
                scs = v[2]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg1: RAR window start Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                frame, subframe = self.frame_subframe(v[3])
                slot = v[4]
                scs = v[5]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg1: RAR window end Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                stdout += "NR MAC RACH Msg1: Backoff duration {}\n".format(v[6])
                pos += 12

            if rach_msg_bitmask & 0x02:
                # Msg2
                # frame/subframe 10b/6b, slot, scs
                v = struct.unpack('<HBB', pkt_body[pos:pos+4])
                frame, subframe = self.frame_subframe(v[0])
                slot = v[1]
                scs = v[2]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg2: Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                pos += 4

                # max backoff duration, T-RNTI, TA, RACH result, SCS Msg2
                v = struct.unpack('<HHHBB', pkt_body[pos:pos+8])
                if v[4] in mac_log_scs_map:
                    scs_val = mac_log_scs_map[v[4]]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg2: Max backoff {} T-RNTI {} TA {} RAPID result {} SCS Msg2 {}\n".format(v[0],
                                                        v[1], v[2], v[3], scs_val)
                pos += 8

            if rach_msg_bitmask & 0x04:
                # Msg3
                # frame/subframe 10b/6b, slot, scs
                v = struct.unpack('<HBB', pkt_body[pos:pos+4])
                frame, subframe = self.frame_subframe(v[0])
                slot = v[1]
                scs = v[2]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg3: Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                pos += 4

                # grant raw, grant bytes, HARQ id, scs
                v = struct.unpack('<LHBB', pkt_body[pos:pos+8])
                if v[3] in mac_log_scs_map:
                    scs_val = mac_log_scs_map[v[3]]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg3: Grant 0x{:x} {}b HARQ ID {} SCS {}\n".format(v[0],
                                                    v[1], v[2], scs_val)
                pos += 8

                # MAC PDU (12 bytes)
                mac_pdu = pkt_body[pos:pos+12]
                stdout += "NR MAC RACH Msg3: MAC PDU: {}\n".format(binascii.hexlify(mac_pdu))
                pos += 12

            if rach_msg_bitmask & 0x08:
                # Msg4
                # frame/subframe 10b/6b, slot, scs
                v = struct.unpack('<HBB', pkt_body[pos:pos+4])
                frame, subframe = self.frame_subframe(v[0])
                slot = v[1]
                scs = v[2]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg4: Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                pos += 4

                # contention start SFN (frame/subframe 10b/6b, slot, scs)
                v = struct.unpack('<HBB', pkt_body[pos:pos+4])
                frame, subframe = self.frame_subframe(v[0])
                slot = v[1]
                scs = v[2]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg4: Contention start at Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                pos += 4

                # contention end SFN (frame/subframe 10b/6b, slot, scs)
                v = struct.unpack('<HBB', pkt_body[pos:pos+4])
                frame, subframe = self.frame_subframe(v[0])
                slot = v[1]
                scs = v[2]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg4: Contention end at Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                pos += 4

                # C-RNTI, reserved
                v = struct.unpack('<HBB', pkt_body[pos:pos+4])
                stdout += "NR MAC RACH Msg4: C-RNTI: {}\n".format(v[0])
                pos += 4

            return {'stdout': stdout.rstrip()}
        elif version == 0x00030005:
            # Padding, num attempt, ssb id, csi rs id, reserved, carrier id
            # RACH result, contention type, RACH msg bitmask, msg1 scs, ul bwp scs, reserved
            v = struct.unpack('<LHBBBB BBBBB BBBH', pkt_body[4:24])
            num_attempt = v[1]
            ssb_id = v[2]
            csi_rs_id = v[3]
            carrier_id = v[5]
            rach_result = v[6]
            contention_type = v[7]
            rach_msg_bitmask = v[8]
            msg1_scs = v[9]
            ul_bwp_scs = v[10]

            rach_result_map = {
                0: 'SUCCESS',
                1: 'FAILURE_MSG2_RA_TIMER_EXP',
                2: 'FAILURE_MSG2_RAPID_MISMATCH',
                3: 'FAILURE_MSG2_RAR_PRUNE',
                4: 'BOI_ONLY_MSG2',
                5: 'FAILURE_MSG4_CT_TIMER_EXPIRED',
                6: 'FAILURE_MSG4_CT_RESOLUTION_NOT_PASSED',
                7: 'ABORTED',
                8: 'SUSPENDED',
                9: 'RESUMED'
            }

            contention_type_map = {
                0: 'CONT_FREE',
                1: 'CONT_DL_MCE',
                2: 'CONT_UL_GRANT',
                3: 'PDCCH_CRNTI'
            }

            msg1_scs_map = {
                0: 1.25,
                1: 5,
                2: 15,
                3: 30,
                4: 60,
                5: 120,
                6: 240
            }

            ul_bwp_scs_map = {
                0: 15,
                1: 30,
                2: 60,
                3: 120,
                4: 240,
                5: 0
            }

            mac_log_scs_map = {
                0: 15,
                1: 30,
                2: 60,
                3: 120,
                4: 0,
                5: 0
            }

            if rach_result in rach_result_map:
                rach_result_str = rach_result_map[rach_result]
            else:
                rach_result_str = 'UNKNOWN'

            if contention_type in contention_type_map:
                contention_type_str = contention_type_map[contention_type]
            else:
                contention_type_str = 'UNKNOWN'

            if msg1_scs in msg1_scs_map:
                msg1_scs_val = msg1_scs_map[msg1_scs]
            else:
                msg1_scs_val = 0

            if ul_bwp_scs in ul_bwp_scs_map:
                ul_bwp_scs_val = ul_bwp_scs_map[ul_bwp_scs]
            else:
                ul_bwp_scs_val = 0

            stdout += "NR MAC RACH Attempt: {} {} {} {} {} {} Msg1 SCS: {} UL BWP SCS: {}\n".format(num_attempt, ssb_id, csi_rs_id,
                                                                        carrier_id, rach_result_str,
                                                                        contention_type_str, msg1_scs_val,
                                                                        ul_bwp_scs_val)

            pos = 24

            if rach_msg_bitmask & 0x01:
                # Msg1
                # frame/subframe 10b/6b, slot, scs
                v = struct.unpack('<HBB', pkt_body[pos:pos+4])
                frame, subframe = self.frame_subframe(v[0])
                slot = v[1]
                scs = v[2]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg1: Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                pos += 4

                # symbol start, preamble format, prach config, Uroot, RA id, FDM, cyclic shift v, N_CS, RA-RNTI, Pathloss
                v = struct.unpack('<BBHHBBHHHH', pkt_body[pos:pos+16])
                stdout += "NR MAC RACH Msg1: Symbol start {} PRACH config {} Preamble {} RA ID {} FDM {} Uroot {} Cyclic shift {} RA-RNTI {}\n".format(v[0],
                                                                v[2], v[1], v[4],
                                                                v[5], v[3], v[6], v[8])
                pos += 16

                # RAR window start/end SFN, backoff duration, reserved
                v = struct.unpack('<HBBHBBLL', pkt_body[pos:pos+16])
                frame, subframe = self.frame_subframe(v[0])
                slot = v[1]
                scs = v[2]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg1: RAR window start Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                frame, subframe = self.frame_subframe(v[3])
                slot = v[4]
                scs = v[5]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg1: RAR window end Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                stdout += "NR MAC RACH Msg1: Backoff duration {}\n".format(v[6])
                pos += 16

            if rach_msg_bitmask & 0x02:
                # Msg2
                # frame/subframe 10b/6b, slot, scs
                v = struct.unpack('<HBB', pkt_body[pos:pos+4])
                frame, subframe = self.frame_subframe(v[0])
                slot = v[1]
                scs = v[2]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg2: Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                pos += 4

                # max backoff duration, T-RNTI, TA, RACH result, SCS Msg2, reserved1, reserved2, RAID received
                v = struct.unpack('<HHHBBLLL', pkt_body[pos:pos+20])
                if v[4] in mac_log_scs_map:
                    scs_val = mac_log_scs_map[v[4]]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg2: Max backoff {} T-RNTI {} TA {} RAPID result {} SCS Msg2 {}\n".format(v[0],
                                                        v[1], v[2], v[3], scs_val)
                pos += 20

            if rach_msg_bitmask & 0x04:
                # Msg3
                # frame/subframe 10b/6b, slot, scs
                v = struct.unpack('<HBB', pkt_body[pos:pos+4])
                frame, subframe = self.frame_subframe(v[0])
                slot = v[1]
                scs = v[2]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg3: Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                pos += 4

                # grant raw, grant bytes, HARQ id, scs
                v = struct.unpack('<LHBB', pkt_body[pos:pos+8])
                if v[3] in mac_log_scs_map:
                    scs_val = mac_log_scs_map[v[3]]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg3: Grant 0x{:x} {}b HARQ ID {} SCS {}\n".format(v[0],
                                                    v[1], v[2], scs_val)
                pos += 8

                # MAC PDU (12 bytes)
                mac_pdu = pkt_body[pos:pos+12]
                stdout += "NR MAC RACH Msg3: MAC PDU: {}\n".format(binascii.hexlify(mac_pdu))
                pos += 12

            if rach_msg_bitmask & 0x08:
                # Msg4
                # frame/subframe 10b/6b, slot, scs
                v = struct.unpack('<HBB', pkt_body[pos:pos+4])
                frame, subframe = self.frame_subframe(v[0])
                slot = v[1]
                scs = v[2]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg4: Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                pos += 4

                # contention start SFN (frame/subframe 10b/6b, slot, scs)
                v = struct.unpack('<HBB', pkt_body[pos:pos+4])
                frame, subframe = self.frame_subframe(v[0])
                slot = v[1]
                scs = v[2]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg4: Contention start at Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                pos += 4

                # contention end SFN (frame/subframe 10b/6b, slot, scs)
                v = struct.unpack('<HBB', pkt_body[pos:pos+4])
                frame, subframe = self.frame_subframe(v[0])
                slot = v[1]
                scs = v[2]
                if scs in mac_log_scs_map:
                    scs_val = mac_log_scs_map[scs]
                else:
                    scs_val = 0
                stdout += "NR MAC RACH Msg4: Contention end at Frame {}/{}, Slot {}, SCS {}\n".format(frame, subframe, slot, scs_val)
                pos += 4

                # C-RNTI, reserved
                v = struct.unpack('<HBB', pkt_body[pos:pos+4])
                stdout += "NR MAC RACH Msg4: C-RNTI: {}\n".format(v[0])
                pos += 4

                return {'stdout': stdout.rstrip()}

        else:
            if self.parent:
                self.parent.logger.log(logging.WARNING, 'Unknown NR MAC RACH Attempt packet version %s' % version)
                self.parent.logger.log(logging.WARNING, "Body: %s" % (util.xxd_oneline(pkt_body[4:])))
            return

    # RRC
    def parse_nr_rrc(self, pkt_header, pkt_body, args):
        msg_content = b''
        stdout = ''
        pkt_ver = struct.unpack('<I', pkt_body[0:4])[0]
        item_struct = namedtuple('QcDiagNrRrcOtaPacket', 'rrc_rel_maj rrc_rel_min rbid pci nrarfcn sfn_subfn pdu_id sib_mask len')
        item_struct_v17 = namedtuple('QcDiagNrRrcOtaPacketV17', 'rrc_rel_maj rrc_rel_min rbid pci unk1 nrarfcn sfn_subfn pdu_id sib_mask len')

        if pkt_ver in (0x09, ): # Version 9
            item = item_struct._make(struct.unpack('<BBBHIIBIH', pkt_body[4:24]))
            msg_content = pkt_body[24:]
        elif pkt_ver in (0x0c, 0x0e): # Version 12, 14
            item = item_struct._make(struct.unpack('<BBBHI3sBIH', pkt_body[4:23]))
            msg_content = pkt_body[23:]
        elif pkt_ver in (0x11, ): # Version 17
            item = item_struct_v17._make(struct.unpack('<BBBH Q I3sBIH', pkt_body[4:31]))
            msg_content = pkt_body[31:]
        elif pkt_ver in (0x13, ): # Version 19
            item = item_struct_v17._make(struct.unpack('<BBBH Q I3sBIHx', pkt_body[4:32]))
            msg_content = pkt_body[32:]
        elif pkt_ver in (0x17, ): # Version 23
            item = item_struct_v17._make(struct.unpack('<BBBH Q I3sBIH4x', pkt_body[4:35]))
            msg_content = pkt_body[35:]
        else:
            if self.parent:
                self.parent.logger.log(logging.WARNING, 'Unknown NR RRC OTA Message packet version {:#x}'.format(pkt_ver))
                self.parent.logger.log(logging.DEBUG, "Body: {}".format(util.xxd_oneline(pkt_body)))
            return None

        if pkt_ver in (0x09, ):
            rrc_type_map = {
                1: util.x_nr_rrc_types.BCCH_BCH,
                2: util.x_nr_rrc_types.BCCH_DL_SCH,
                3: util.x_nr_rrc_types.DL_CCCH,
                4: util.x_nr_rrc_types.DL_DCCH,
                5: util.x_nr_rrc_types.PCCH,
                6: util.x_nr_rrc_types.UL_CCCH,
                7: util.x_nr_rrc_types.UL_CCCH1,
                8: util.x_nr_rrc_types.UL_DCCH,
                9: util.x_nr_rrc_types.RRC_RECONFIGURATION,
                28: util.x_nr_rrc_types.UE_MRDC_CAPABILITY,
                29: util.x_nr_rrc_types.UE_NR_CAPABILITY,
            }
            rrc_type_map_no = {
                10: 'RRCReconfigurationComplete',
                11: 'SIB1',
                12: 'SysInfo',
                13: 'UECapabilityInquiry-v1560',
                14: 'SIB2',
                15: 'SIB3',
                16: 'SIB4',
                17: 'SIB5',
                18: 'SIB6',
                19: 'SIB7',
                20: 'SIB8',
                21: 'SIB9',
                22: 'CellGroupConfig',
                23: 'Meas Result Cell List Eutra',
                24: 'Meas Result Scg Fail',
                25: 'nr-RadioBearerConfig',
                26: 'Freq Band List',
                27: 'UE_CAP_REQ_FILTER_NR',
                30: 'VAR_RESUME_MAC_INPUT',
                31: 'VAR_SHORT_MAC_INPUT',
            }

        elif pkt_ver == 0x0c:
            if (item.rrc_rel_maj == 0x0f and item.rrc_rel_min == 0x70) or \
            (item.rrc_rel_maj == 0x0f and item.rrc_rel_min == 0x90):
                rrc_type_map = {
                    1: util.x_nr_rrc_types.BCCH_BCH,
                    2: util.x_nr_rrc_types.BCCH_DL_SCH,
                    3: util.x_nr_rrc_types.DL_CCCH,
                    4: util.x_nr_rrc_types.DL_DCCH,
                    5: util.x_nr_rrc_types.PCCH,
                    6: util.x_nr_rrc_types.UL_CCCH,
                    7: util.x_nr_rrc_types.UL_CCCH1,
                    8: util.x_nr_rrc_types.UL_DCCH,
                    9: util.x_nr_rrc_types.RRC_RECONFIGURATION,
                    28: util.x_nr_rrc_types.UE_MRDC_CAPABILITY,
                    29: util.x_nr_rrc_types.UE_NR_CAPABILITY,
                }
                rrc_type_map_no = {
                    10: 'RRCReconfigurationComplete',
                    11: 'SIB1',
                    12: 'SysInfo',
                    13: 'UECapabilityInquiry-v1560',
                    14: 'SIB2',
                    15: 'SIB3',
                    16: 'SIB4',
                    17: 'SIB5',
                    18: 'SIB6',
                    19: 'SIB7',
                    20: 'SIB8',
                    21: 'SIB9',
                    22: 'CellGroupConfig',
                    23: 'Meas Result Cell List Eutra',
                    24: 'Meas Result Scg Fail',
                    25: 'nr-RadioBearerConfig',
                    26: 'Freq Band List',
                    27: 'UE_CAP_REQ_FILTER_NR',
                    30: 'VAR_RESUME_MAC_INPUT',
                    31: 'VAR_SHORT_MAC_INPUT',
                }
            else:
                rrc_type_map = {}
                rrc_type_map_no = {}

        elif pkt_ver in (0x0e, ):
            rrc_type_map = {
                1: util.x_nr_rrc_types.BCCH_BCH,
                2: util.x_nr_rrc_types.BCCH_DL_SCH,
                3: util.x_nr_rrc_types.DL_CCCH,
                4: util.x_nr_rrc_types.DL_DCCH,
                5: util.x_nr_rrc_types.PCCH,
                6: util.x_nr_rrc_types.UL_CCCH,
                7: util.x_nr_rrc_types.UL_CCCH1,
                8: util.x_nr_rrc_types.UL_DCCH,
                9: util.x_nr_rrc_types.RRC_RECONFIGURATION,
                31: util.x_nr_rrc_types.UE_MRDC_CAPABILITY,
                32: util.x_nr_rrc_types.UE_NR_CAPABILITY,
                33: util.x_nr_rrc_types.UE_NR_CAPABILITY,
            }
            rrc_type_map_no = {
                10: 'RRCReconfigurationComplete',
                11: 'SIB1',
                12: 'SysInfo',
                13: 'OVERHEATINGASSISTANCE',
                14: 'UECapabilityInquiry-v1560',
                15: 'SIB2',
                16: 'SIB3',
                17: 'SIB4',
                18: 'SIB5',
                19: 'SIB6',
                20: 'SIB7',
                21: 'SIB8',
                22: 'SIB9',
                23: 'SIB12-r16',
                24: 'POS_SYSINFO_R16',
                25: 'CellGroupConfig',
                26: 'Meas Result Cell List Eutra',
                27: 'Meas Result Scg Fail',
                28: 'nr-RadioBearerConfig',
                29: 'Freq Band List',
                30: 'UE_CAP_REQ_FILTER_NR',
                34: 'VAR_RESUME_MAC_INPUT',
                35: 'VAR_RLF_RPT_R16',
                36: 'VAR_SHORT_MAC_INPUT',
            }
        elif pkt_ver in (0x11, 0x13, ):
            rrc_type_map = {
                1: util.x_nr_rrc_types.BCCH_BCH,
                2: util.x_nr_rrc_types.BCCH_DL_SCH,
                3: util.x_nr_rrc_types.DL_CCCH,
                4: util.x_nr_rrc_types.DL_DCCH,
                5: util.x_nr_rrc_types.PCCH,
                6: util.x_nr_rrc_types.UL_CCCH,
                7: util.x_nr_rrc_types.UL_CCCH1,
                8: util.x_nr_rrc_types.UL_DCCH,
                9: util.x_nr_rrc_types.RRC_RECONFIGURATION,
            }
            rrc_type_map_no = {
                10: 'RRCReconfigurationComplete',
                29: "nr-RadioBearerConfig",
            }
        elif pkt_ver in (0x17, ):
           rrc_type_map = {
                1: "BCCH_BCH",
                2: "BCCH_DL_SCH",
                3: "DL_CCCH",
                4: "DL_DCCH",
                5: "MCCH",
                6: "PCCH",
                7: "UL_CCCH",
                8: "UL_CCCH1",
                9: "UL_DCCH",
                10: "RRC_RECONFIGURATION",
                11: "RRC_RECONFIGURATION_COMPLETE",
                36: "nr-RadioBearerConfig",
            }

        pkt_ts = util.parse_qxdm_ts(pkt_header.timestamp)
        ts_sec = calendar.timegm(pkt_ts.timetuple())
        ts_usec = pkt_ts.microsecond

        if not (item.pdu_id in rrc_type_map.keys() or item.pdu_id in rrc_type_map_no.keys()):
            if self.parent:
                self.parent.logger.log(logging.WARNING, "Unknown RRC subtype 0x%02x for RRC packet version 0x%02x" % (item.pdu_id, pkt_ver))
                self.parent.logger.log(logging.DEBUG, util.xxd(pkt_body))
            return

        if item.pdu_id in rrc_type_map.keys():
            type_str = rrc_type_map[item.pdu_id]
            stdout += "NR RRC OTA Packet: NR-ARFCN {}, PCI {}".format(item.nrarfcn, item.pci)
            nr_pdu_id_gsmtap = rrc_type_map[item.pdu_id]

            # TODO: GSMTAP header for 5GNR
            gsmtap_hdr = util.create_gsmtap_header(
                version = 3,
                payload_type = util.gsmtap_type.X_NR_RRC,
                arfcn = 0,
                sub_type = nr_pdu_id_gsmtap,
                device_sec = ts_sec,
                device_usec = ts_usec)

            return {'layer': 'rrc', 'cp': [gsmtap_hdr + msg_content], 'ts': pkt_ts, 'stdout': stdout}
        else:
            type_str = rrc_type_map_no[item.pdu_id]
            stdout += "NR RRC OTA Packet: NR-ARFCN {}, PCI {}, Type: {}\n".format(item.nrarfcn, item.pci, type_str)
            stdout += "NR RRC OTA Packet: Body: {}".format(binascii.hexlify(msg_content).decode())

    def parse_nr_mib_info(self, pkt_header, pkt_body, args):
        pkt_ts = util.parse_qxdm_ts(pkt_header.timestamp)
        pkt_ver = struct.unpack('<I', pkt_body[0:4])[0]

        item_struct = namedtuple('QcDiagNrMibInfo', 'pci nrarfcn props')
        scs_map = {
            0: 15,
            1: 30,
            2: 60,
            3: 120,
        }

        scs_str = ''
        if pkt_ver == 0x03: # Version 3
            # SFN: 0:10
            # Block Index: 10:13
            # Half Number: 13:1
            # Intra Freq Reselection: 14:1
            # Cell Barred: 15:1
            # PDCCH Config SIB1: 16:8
            # DMRS TypeA Pos: 24:2
            # SSB Subcarrier Offset: 26:4
            # Subcarrier Spacing Common: 30:2
            item = item_struct._make(struct.unpack('<HI4s', pkt_body[4:14]))
            sfn = (item.props[0]) | (((item.props[1] & 0b11000000) >> 6) << 8)
            scs = (item.props[3] & 0b11000000) >> 6
        elif pkt_ver == 0x20000: # Version 131072
            item = item_struct._make(struct.unpack('<HI5s', pkt_body[4:15]))
            sfn = (item.props[0]) | (((item.props[1] & 0b11000000) >> 6) << 8)
            scs = (item.props[3] & 0b10000000) >> 7 | ((item.props[4] & 0b00000001) << 1)
        else:
            if self.parent:
                self.parent.logger.log(logging.WARNING, 'Unknown NR MIB Information packet version {}'.format(pkt_ver))
                self.parent.logger.log(logging.WARNING, "Body: {}".format(util.xxd_oneline(pkt_body)))
            return

        if scs in scs_map:
            scs_str = '{} kHz'.format(scs_map[scs])

        if len(scs_str) > 0:
            stdout = 'NR MIB: NR-ARFCN {}, PCI {:4d}, SFN: {}, SCS: {}'.format(item.nrarfcn, item.pci, sfn, scs_str)
        else:
            stdout = 'NR MIB: NR-ARFCN {}, PCI {:4d}, SFN: {}'.format(item.nrarfcn, item.pci, sfn)
        return {'stdout': stdout, 'ts': pkt_ts}

    def parse_nr_rrc_scell_info(self, pkt_header, pkt_body, args):
        pkt_ts = util.parse_qxdm_ts(pkt_header.timestamp)
        pkt_ver = struct.unpack('<I', pkt_body[0:4])[0]

        item_struct = namedtuple('QcDiagNrScellInfo', 'pci dl_nrarfcn ul_nrarfcn dl_bandwidth ul_bandwidth cell_id mcc mnc_digit mnc allowed_access tac band')
        item_struct_v30000 = namedtuple('QcDiagNrScellInfoV30000', 'pci nr_cgi dl_nrarfcn ul_nrarfcn dl_bandwidth ul_bandwidth cell_id mcc mnc_digit mnc allowed_access tac band')
        if pkt_ver == 0x04:
            # PCI 2b, DL NR-ARFCN 4b, UL NR-ARFCN 4b, DLBW 2b, ULBW 2b, Cell ID 8b, MCC 2b, MCC digit 1b, MNC 2b, MNC digit 1b, TAC 4b, ?
            item = item_struct._make(struct.unpack('<H LLHH Q H BH B LH', pkt_body[4:38]))
        elif pkt_ver == 0x30000:
            # PCI 2b, NR CGI 8b, DL NR-ARFCN 4b, UL NR-ARFCN 4b, DLBW 2b, ULBW 2b, Cell ID 8b, MCC 2b, MCC digit 1b, MNC 2b, MNC digit 1b, TAC 4b, ?
            item = item_struct_v30000._make(struct.unpack('<H Q LLHH Q H BH B LH', pkt_body[4:46]))
        elif pkt_ver in (0x30002, 0x30003, ):
            # ? 3b, PCI 2b, NR CGI 8b, DL NR-ARFCN 4b, UL NR-ARFCN 4b, DLBW 2b, ULBW 2b, Cell ID 8b, MCC 2b, MCC digit 1b, MNC 2b, MNC digit 1b, TAC 4b, ?
            item = item_struct_v30000._make(struct.unpack('<H Q LLHH Q H BH B LH', pkt_body[7:49]))
        else:
            if self.parent:
                self.parent.logger.log(logging.WARNING, 'Unknown NR SCell Information packet version {:4x}'.format(pkt_ver))
                self.parent.logger.log(logging.WARNING, "Body: {}".format(util.xxd_oneline(pkt_body)))
            return None

        if item.mnc_digit == 2:
            stdout = 'NR RRC SCell Info: NR-ARFCN {}/{}, Bandwidth {}/{} MHz, Band {}, PCI {:4d}, xTAC/xCID {:x}/{:x}, MCC {}, MNC {:02}'.format(item.dl_nrarfcn,
                item.ul_nrarfcn, item.dl_bandwidth, item.ul_bandwidth, item.band, item.pci, item.tac, item.cell_id, item.mcc, item.mnc)
        elif item.mnc_digit == 3:
            stdout = 'NR RRC SCell Info: NR-ARFCN {}/{}, Bandwidth {}/{} MHz, Band {}, PCI {:4d}, xTAC/xCID {:x}/{:x}, MCC {}, MNC {:02}'.format(item.dl_nrarfcn,
                item.ul_nrarfcn, item.dl_bandwidth, item.ul_bandwidth, item.band, item.pci, item.tac, item.cell_id, item.mcc, item.mnc)
        else:
            stdout = 'NR RRC SCell Info: NR-ARFCN {}/{}, Bandwidth {}/{} MHz, Band {}, PCI {:4d}, xTAC/xCID {:x}/{:x}, MCC {}, MNC {:02}'.format(item.dl_nrarfcn,
                item.ul_nrarfcn, item.dl_bandwidth, item.ul_bandwidth, item.band, item.pci, item.tac, item.cell_id, item.mcc, item.mnc)
        return {'stdout': stdout, 'ts': pkt_ts}

    def parse_nr_0xb824(self, pkt_ts, pkt, radio_id):
        # 05 00 00 00 | 01 01 0c | c0 ac 05 00 | 00 00
        pass

    def parse_nr_rrc_conf_info(self, pkt_header, pkt_body, args):
        version = struct.unpack('<L', pkt_body[0:4])[0]
        stdout = ''

        item_struct = namedtuple('QcDiagNrRrcConf',
            'rrc_state is_configured nr_mode num_active_srb num_active_drb '
            'mn_mcg_drb_id sn_mcg_drb_id mn_scg_drb_id sn_scg_drb_id mn_split_drb_id sn_split_drb_id')
        item_struct_v30003 = namedtuple('QcDiagNrRrcConfV30003',
            ('nr_cgi', ) + item_struct._fields)
        item_struct_lte_bands = namedtuple('QcDiagNrRrcConfLteBands',
            'num_lte_bands')
        item_struct_num_res = namedtuple('QcDiagNrRrcConfNumRes',
            'num_cont_cc_group num_active_cc num_active_rb')
        item_struct_num_res_v30003 = namedtuple('QcDiagNrRrcConfNumRes',
            'num_cont_cc_group num_nrdc_scg_cont_cc_group num_active_cc num_nrdc_scg_active_cc num_active_rb')

        item_struct_cont_cc = namedtuple('QcDiagNrRrcConfContCC', 'band dl_bw_class ul_bw_class')
        item_struct_scell = namedtuple('QcDiagNrRrcConfScell', 'cc_id pci dl_nrarfcn ul_nrarfcn band band_type dl_bandwidth ul_bandwidth dl_max_mimo ul_max_mimo')
        item_struct_scell_vA = namedtuple('QcDiagNrRrcConfScellVA', 'cc_id pci dl_nrarfcn ul_nrarfcn ssb_nrarfcn band band_type dl_bandwidth ul_bandwidth dl_max_mimo ul_max_mimo')
        item_struct_scell_v30003 = namedtuple('QcDiagNrRrcConfScellV30003', 'cc_id pci dl_nrarfcn ul_nrarfcn ssb_nrarfcn band band_type dl_bandwidth ul_bandwidth scs dl_max_mimo ul_max_mimo')
        item_struct_rb = namedtuple('QcDiagNrRrcConfRadioBearer', 'rb_id term_point dl_rb_type dl_rb_path dl_rohc_enabled dl_cipher_algo dl_integrity_algo ul_rb_type ul_rb_path ul_rohc_enabled ul_ciper_algo ul_integrity_algo ul_primary_path ul_pdcp_dup_activated ul_data_split_threshold')

        if version in (0x08, 0x0a, 0x20000):
            # Found in RM500Q
            # RRC state, config status, connectivity mode, num active SRB, num active DRB
            # MN/SN MCG DRB ID, MN/SN SCG DRB ID, MN/SN split DRB ID
            item_format = '<BBBBB LLLLLL'
            item = item_struct._make(struct.unpack(item_format, pkt_body[4:4+struct.calcsize(item_format)]))

            item_format = '<B'
            item_lte_bands = item_struct_lte_bands._make(struct.unpack(item_format, pkt_body[33:33+struct.calcsize(item_format)]))
            item_format = '<12H'
            item_lte_bands_vals = struct.unpack(item_format, pkt_body[34:34+struct.calcsize(item_format)])

            item_format = '<BBB'
            item_num_res = item_struct_num_res._make(struct.unpack(item_format, pkt_body[58:58+struct.calcsize(item_format)]))

            nr_rrc_state_map = {
                0: 'DEACTIVATED',
                1: 'INITIAL',
                2: 'INACTIVE',
                3: 'IDLE_NOT_CAMPED',
                4: 'IDLE_CAMPED',
                5: 'CONNECTING',
                6: 'CONNECTING_NOT_CAMPED',
                7: 'CONNECTED',
                8: 'SUSPENDED',
                9: 'IRAT_TO_NR5G_STARTED',
                10: 'CLOSING',
                11: 'RESUMING',
                12: 'INACTIVE_SUSPENDING',
                13: 'INACTIVE_NOT_CAMPED',
                14: 'INACTIVE_CAMPED',
                15: 'INVALID',
                16: 'IDLE',
                17: 'IRAT'
            }

            nr_mode_map = {
                0: 'INVALID',
                1: 'NSA',
                2: 'SA'
            }

            nr_band_type_map = {
                0: 'INVALID',
                1: 'SUB6',
                2: 'MMW'
            }

            nr_bandwidth_map = {
                0: 5,
                1: 10,
                2: 15,
                3: 20,
                4: 25,
                5: 30,
                6: 40,
                7: 50,
                8: 60,
                9: 70,
                10: 80,
                11: 90,
                12: 100,
                13: 200,
                14: 400
            }

            if item.rrc_state in nr_rrc_state_map:
                rrc_state_str = nr_rrc_state_map[item.rrc_state]
            else:
                rrc_state_str = 'UNKNOWN'

            if item.nr_mode in nr_mode_map:
                nr_mode_str = nr_mode_map[item.nr_mode]
            else:
                nr_mode_str = 'UNKNOWN'

            stdout += 'NR RRC Configuration Info: RRC status {}, Config status {}, Mode {}, Active SRB/DRB: {}/{}\n'.format(rrc_state_str,
                item.is_configured, nr_mode_str, item.num_active_srb, item.num_active_drb)
            if item_lte_bands.num_lte_bands > 0:
                stdout += 'NR RRC Configuration Info: Active LTE bands: {}\n'.format(', '.join([str(x) for x in item_lte_bands_vals[0:item_lte_bands.num_lte_bands]]))

            # num contiguous CC groups, num active CC, num active RB

            pos = 61

            # contiguous CC info - num contiguous CC groups
            for i in range(item_num_res.num_cont_cc_group):
                cont_cc = item_struct_cont_cc._make(struct.unpack('<HBB', pkt_body[pos:pos+4]))
                stdout += 'NR RRC Configuration Info/Contiguous CC {}: Band {}, Class {}/{}\n'.format(i,
                    cont_cc.band, cont_cc.dl_bw_class, cont_cc.ul_bw_class)
                pos += 4

            # NR scell info - num active CC
            for i in range(item_num_res.num_active_cc):
                if version == 0x08:
                    scell = item_struct_scell._make(struct.unpack('<BHLLHBBBBB', pkt_body[pos:pos+18]))
                    pos += 18
                elif version == 0x0a or version == 0x20000:
                    scell = item_struct_scell_vA._make(struct.unpack('<BHLLLHBBBBB', pkt_body[pos:pos+22]))
                    pos += 22

                if scell.dl_bandwidth in nr_bandwidth_map:
                    dl_bw = nr_bandwidth_map[scell.dl_bandwidth]
                else:
                    dl_bw = 0

                if scell.ul_bandwidth in nr_bandwidth_map:
                    ul_bw = nr_bandwidth_map[scell.ul_bandwidth]
                else:
                    ul_bw = 0

                if scell.band_type in nr_band_type_map:
                    nr_band_type_str = nr_band_type_map[scell.band_type]
                else:
                    nr_band_type_str = 'UNKNOWN'

                stdout += 'NR RRC Configuration Info/Active CC {}: CC ID {}: NR-ARFCN {}/{}, Bandwidth {}/{} MHz, Band {} ({}), PCI {:4d}, Max MIMO {}/{}\n'.format(i,
                    scell.cc_id, scell.dl_nrarfcn, scell.ul_nrarfcn, dl_bw, ul_bw, scell.band, nr_band_type_str, scell.pci, scell.dl_max_mimo, scell.ul_max_mimo)

            # radio bearer info - num active RB
            for i in range(item_num_res.num_active_rb):
                rb = item_struct_rb._make(struct.unpack('<BBBBBBBBBBBBBBL', pkt_body[pos:pos+18]))
                pos += 18
                stdout += 'NR RRC Configuration Info/Active RB {}: RB ID {}\n'.format(i, rb.rb_id)

            return {'stdout': stdout.rstrip()}

        elif version == 0x30003:
            # NR CGI, RRC state, config status, connectivity mode, num active SRB, num active DRB
            # MN/SN MCG DRB ID, MN/SN SCG DRB ID, MN/SN split DRB ID
            item_format = '<QBBBBB LLLLLL'
            item = item_struct_v30003._make(struct.unpack(item_format, pkt_body[4:4+struct.calcsize(item_format)]))

            item_format = '<B'
            item_lte_bands = item_struct_lte_bands._make(struct.unpack(item_format, pkt_body[41:41+struct.calcsize(item_format)]))
            item_format = '<12H'
            item_lte_bands_vals = struct.unpack(item_format, pkt_body[42:42+struct.calcsize(item_format)])

            item_format = '<BBBBB'
            item_num_res = item_struct_num_res_v30003._make(struct.unpack(item_format, pkt_body[66:66+struct.calcsize(item_format)]))

            nr_rrc_state_map = {
                0: 'INACTIVE',
                1: 'IDLE_NOT_CAMPED',
                2: 'CONNECTED',
                3: 'SUSPENDED',
                4: 'IDLE',
                5: 'IRAT',
                6: 'INVALID'
            }

            nr_mode_map = {
                0: 'INVALID',
                1: 'NSA',
                2: 'SA',
                3: 'NRDC'
            }

            nr_band_type_map = {
                0: 'INVALID',
                1: 'SUB6',
                2: 'MMW'
            }

            nr_bandwidth_map = {
                0: 5,
                1: 10,
                2: 15,
                3: 20,
                4: 25,
                5: 30,
                6: 35,
                7: 40,
                8: 45,
                9: 50,
                10: 60,
                11: 70,
                12: 80,
                13: 90,
                14: 100,
                15: 200,
                16: 400
            }

            if item.rrc_state in nr_rrc_state_map:
                rrc_state_str = nr_rrc_state_map[item.rrc_state]
            else:
                rrc_state_str = 'UNKNOWN'

            if item.nr_mode in nr_mode_map:
                nr_mode_str = nr_mode_map[item.nr_mode]
            else:
                nr_mode_str = 'UNKNOWN'

            stdout += 'NR RRC Configuration Info: RRC status {}, Config status {}, Mode {}, Active SRB/DRB: {}/{}\n'.format(rrc_state_str,
                item.is_configured, nr_mode_str, item.num_active_srb, item.num_active_drb)
            if item_lte_bands.num_lte_bands > 0:
                stdout += 'NR RRC Configuration Info: Active LTE bands: {}\n'.format(', '.join([str(x) for x in item_lte_bands_vals[0:item_lte_bands.num_lte_bands]]))

            pos = 71

            # contiguous CC info - num contiguous CC groups
            for i in range(item_num_res.num_cont_cc_group):
                cont_cc = item_struct_cont_cc._make(struct.unpack('<HBB', pkt_body[pos:pos+4]))
                stdout += 'NR RRC Configuration Info/Contiguous CC {}: Band {}, Class {}/{}\n'.format(i,
                    cont_cc.band, cont_cc.dl_bw_class, cont_cc.ul_bw_class)
                pos += 4

            # contiguous NRDC SCG CC info - num NRDC SCG contiguous CC groups
            for i in range(item_num_res.num_nrdc_scg_cont_cc_group):
                cont_cc = item_struct_cont_cc._make(struct.unpack('<HBB', pkt_body[pos:pos+4]))
                stdout += 'NR RRC Configuration Info/NRDC SCG Contiguous CC {}: Band {}, Class {}/{}\n'.format(i,
                    cont_cc.band, cont_cc.dl_bw_class, cont_cc.ul_bw_class)
                pos += 4

            # NR scell info - num active CC
            for i in range(item_num_res.num_active_cc):
                # CC ID, PCI, DL ARFCN, UL ARFCN, SSB ARFCN, Band, Type, DL BW, UL BW, SCS, DL MIMO, UL MIMO
                scell = item_struct_scell_v30003._make(struct.unpack('<BHLLLHBBBBBB', pkt_body[pos:pos+23]))
                pos += 23

                if scell.dl_bandwidth in nr_bandwidth_map:
                    dl_bw = nr_bandwidth_map[scell.dl_bandwidth]
                else:
                    dl_bw = 0

                if scell.ul_bandwidth in nr_bandwidth_map:
                    ul_bw = nr_bandwidth_map[scell.ul_bandwidth]
                else:
                    ul_bw = 0

                if scell.band_type in nr_band_type_map:
                    nr_band_type_str = nr_band_type_map[scell.band_type]
                else:
                    nr_band_type_str = 'UNKNOWN'

                stdout += 'NR RRC Configuration Info/Active CC {}: CC ID {}: NR-ARFCN {}/{}, Bandwidth {}/{} MHz, Band {} ({}), PCI {:4d}, Max MIMO {}/{}\n'.format(i,
                    scell.cc_id, scell.dl_nrarfcn, scell.ul_nrarfcn, dl_bw, ul_bw, scell.band, nr_band_type_str, scell.pci, scell.dl_max_mimo, scell.ul_max_mimo)

            # NRDC SCG scell info - num NRDC SCG active CC
            for i in range(item_num_res.num_nrdc_scg_active_cc):
                # CC ID, PCI, DL ARFCN, UL ARFCN, SSB ARFCN, Band, Type, DL BW, UL BW, SCS, DL MIMO, UL MIMO
                scell = item_struct_scell_v30003._make(struct.unpack('<BHLLLHBBBBBB', pkt_body[pos:pos+23]))
                pos += 23

                if scell.dl_bandwidth in nr_bandwidth_map:
                    dl_bw = nr_bandwidth_map[scell.dl_bandwidth]
                else:
                    dl_bw = 0

                if scell.ul_bandwidth in nr_bandwidth_map:
                    ul_bw = nr_bandwidth_map[scell.ul_bandwidth]
                else:
                    ul_bw = 0

                if scell.band_type in nr_band_type_map:
                    nr_band_type_str = nr_band_type_map[scell.band_type]
                else:
                    nr_band_type_str = 'UNKNOWN'

                stdout += 'NR RRC Configuration Info/NRDC Active CC {}: CC ID {}: NR-ARFCN {}/{}, Bandwidth {}/{} MHz, Band {} ({}), PCI {:4d}, Max MIMO {}/{}\n'.format(i,
                    scell.cc_id, scell.dl_nrarfcn, scell.ul_nrarfcn, dl_bw, ul_bw, scell.band, nr_band_type_str, scell.pci, scell.dl_max_mimo, scell.ul_max_mimo)

            # radio bearer info - num active RB
            for i in range(item_num_res.num_active_rb):
                rb = item_struct_rb._make(struct.unpack('<BBBBBBBBBBBBBBL', pkt_body[pos:pos+18]))
                pos += 18
                stdout += 'NR RRC Configuration Info/Active RB {}: RB ID {}\n'.format(i, rb.rb_id)

            return {'stdout': stdout.rstrip()}

            # 08 00 00 00 | 10 | 01 | 02 |
            # RRC State 1b, Config Status 1b, Connectivity Mode 1b
            # 01 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            # 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            # 01 01 01 4e 00 01 01 00
            # 9d 02 | 52 d2 09 00 | 52 d2 09 00 | 4e 00 | 01 | 0b | 0b
            # PCI, DL ARFCN, UL ARFCN, Band, Band Type, DL BW, UL BW
            # 00 00 21 02 01 02 00 00 00 01 02 00 00 00 00 00 00 00 00 00
        else:
            if self.parent:
                self.parent.logger.log(logging.WARNING, 'Unknown NR RRC Configuration packet version %s' % version)
                self.parent.logger.log(logging.WARNING, "Body: %s" % (util.xxd_oneline(pkt_body[4:])))
            return

    def parse_nr_cacombos(self, pkt_header, pkt_body, args):
        pkt_ts = util.parse_qxdm_ts(pkt_header.timestamp)
        if self.parent:
            if not self.parent.cacombos:
                return None

        return {'stdout': 'NR UE CA Combos Raw: {}'.format(binascii.hexlify(pkt_body).decode()), 'ts': pkt_ts}

    # NAS
    def parse_nr_nas(self, pkt_header, pkt_body, args, cmd_id):
        pkt_ts = util.parse_qxdm_ts(pkt_header.timestamp)
        ts_sec = calendar.timegm(pkt_ts.timetuple())
        ts_usec = pkt_ts.microsecond
        stdout = ''
        plain = (cmd_id in (0xB800, 0xB801, 0xB80A, 0xB80B, 0xB814))

        # Version 4b, std version maj.min.rev 1b each
        pkt_ver = struct.unpack('<L', pkt_body[0:4])[0]
        item_struct = namedtuple('QcDiagNrNasMsg', 'vermaj vermid vermin')
        msg_content = pkt_body[7:]
        if pkt_ver == 0x1:
            item = item_struct._make(struct.unpack('<BBB', pkt_body[4:7]))
            stdout = "NAS-5GS message ({:04X}) version {:x}.{:x}.{:x}: ".format(cmd_id, item.vermaj, item.vermid, item.vermin)
            msg_content = pkt_body[7:]

            # XXX: internal header for NR NAS
            gsmtap_hdr = util.create_gsmtap_header(
                version = 3,
                payload_type = util.gsmtap_type.X_NR_NAS,
                arfcn = 0,
                sub_type = 0 if plain else 1,
                device_sec = ts_sec,
                device_usec = ts_usec)

            return {'layer': 'nas', 'stdout': stdout, 'cp': [gsmtap_hdr + msg_content], 'ts': pkt_ts}
        else:
            if self.parent:
                self.parent.logger.log(logging.WARNING, 'Unknown NR NAS Message packet version {:#x}'.format(pkt_ver))
                self.parent.logger.log(logging.DEBUG, "Body: {}".format(util.xxd_oneline(pkt_body)))
            return None

    def parse_nr_mm_state(self, pkt_header, pkt_body, args):
        pkt_ts = util.parse_qxdm_ts(pkt_header.timestamp)
        pkt_ver = struct.unpack('<I', pkt_body[0:4])[0]

        if pkt_ver in (0x01, 0x30000, ): # Version 1 and 196608
            item_struct = namedtuple('QcDiagNrNasMmState', 'mm_state mm_substate plmn_id guti_5gs mm_update_status tac')
            item = item_struct._make(struct.unpack('<BH3s12sb3s', pkt_body[4:26]))
            plmn_id = util.unpack_mcc_mnc(item.plmn_id)
            tac = struct.unpack('>L', b'\x00'+item.tac)[0]

            if item.guti_5gs[0] == 0x02:
                # mcc-mcc-amf_rid-amf_sid-amf_ptr-5g_tmsi
                plmn_id_guti = util.unpack_mcc_mnc(item.guti_5gs[1:4])
                amf_sid = struct.unpack('<H', item.guti_5gs[5:7])[0]
                tmsi_5gs = struct.unpack('<L', item.guti_5gs[8:12])[0]
                guti_str = '{:03x}-{:03x}-{:02x}-{:03x}-{:02x}-{:08x}'.format(plmn_id_guti[0], plmn_id_guti[1], item.guti_5gs[4],
                                                              amf_sid, item.guti_5gs[7], tmsi_5gs)
            else:
                guti_str = binascii.hexlify(item.guti_5gs).decode()

            stdout = '5GMM State: {}/{}/{}, PLMN: {:3x}/{:3x}, TAC: {:6x}, GUTI: {}'.format(
                item.mm_state, item.mm_substate, item.mm_update_status, plmn_id[0], plmn_id[1], tac, guti_str
            )
            return {'stdout': stdout, 'ts': pkt_ts}
        else:
            if self.parent:
                self.parent.logger.log(logging.WARNING, 'Unknown NR MM State packet version %s' % pkt_ver)
                self.parent.logger.log(logging.WARNING, "Body: %s" % (util.xxd_oneline(pkt_body[4:])))
            return
