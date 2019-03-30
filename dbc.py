#!/usr/local/bin/python3
import re
import codecs


class DBC(object):
    def __init__(self):
        pass


msg_attribute = {}
sig_attribute = {}


def scan_dbc(lines):
    for line in lines:
        """GenMsgCycleTime
        """
        buf = re.search(r'BA_DEF_\s+BO_\s+"GenMsgCycleTime"\s+INT', line)
        if buf:
            msg_attribute['GenMsgCycleTime'] = {}
            continue
        buf = re.search(r'BA_DEF_DEF_\s+"GenMsgCycleTime"\s+(\d+)', line)
        if 'GenMsgCycleTime' in msg_attribute and buf:
            msg_attribute['GenMsgCycleTime']['Default'] = int(buf[1])
            continue

        """GenMsgSendType
        """
        buf = re.search(r'BA_DEF_\s+BO_\s+"GenMsgSendType"\s+ENUM\s+(.+);', line)
        if buf:
            enum = buf[1].replace('"', '').split(',')
            msg_attribute['GenMsgSendType'] = {'ENUM': enum}
            continue
        buf = re.search(r'BA_DEF_DEF_\s+"GenMsgSendType"\s+"(\w+)"', line)
        if buf:
            idx = msg_attribute['GenMsgSendType']['ENUM'].index(buf[1])
            msg_attribute['GenMsgSendType']['Default'] = idx
            continue

        """VFrameFormat
        """
        buf = re.search(r'BA_DEF_\s+BO_\s+"VFrameFormat"\s+ENUM\s+(.+);', line)
        if buf:
            enum = buf[1].replace('"', '').split(',')
            msg_attribute['VFrameFormat'] = {'ENUM': enum}
            continue
        buf = re.search(r'BA_DEF_DEF_\s+"VFrameFormat"\s+"(\w+)"', line)
        if 'VFrameFormat' in msg_attribute and buf:
            idx = msg_attribute['VFrameFormat']['ENUM'].index(buf[1])
            msg_attribute['VFrameFormat']['Default'] = idx
            continue

        """GenSigStartValue
        """
        buf = re.search(r'BA_DEF_\s+SG_\s+"GenSigStartValue"\s+INT', line)
        if buf:
            sig_attribute['GenSigStartValue'] = {}
            continue
        buf = re.search(r'BA_DEF_DEF_\s+"GenSigStartValue"\s+(\d+);', line)
        if 'GenSigStartValue' in sig_attribute and buf:
            sig_attribute['GenSigStartValue']['Default'] = int(buf[1])
            continue


if __name__ == "__main__":
    with codecs.open('../LCANFD.dbc', 'r', encoding='latin1') as fd:
        lines = fd.read().splitlines()
        scan_dbc(lines)
    # print(msg_attribute)
