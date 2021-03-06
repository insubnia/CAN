#!/usr/local/bin/python3
import re
import codecs


def get_attribute(lines):
    msg_attr, sig_attr = {}, {}

    for line in lines:
        """ GenMsgCycleTime
        """
        buf = re.search(r'BA_DEF_\s+BO_\s+"GenMsgCycleTime"\s+INT', line)
        if buf:
            msg_attr['GenMsgCycleTime'] = {}
            continue
        buf = re.search(r'BA_DEF_DEF_\s+"GenMsgCycleTime"\s+(\d+)', line)
        if 'GenMsgCycleTime' in msg_attr and buf:
            msg_attr['GenMsgCycleTime']['Default'] = int(buf[1])
            continue

        """ GenMsgSendType
        """
        buf = re.search(r'BA_DEF_\s+BO_\s+"GenMsgSendType"\s+ENUM\s+(.+);', line)
        if buf:
            enum = buf[1].replace('"', '').split(',')
            msg_attr['GenMsgSendType'] = {'ENUM': enum}
            continue
        buf = re.search(r'BA_DEF_DEF_\s+"GenMsgSendType"\s+"(\w+)"', line)
        if buf:
            idx = msg_attr['GenMsgSendType']['ENUM'].index(buf[1])
            msg_attr['GenMsgSendType']['Default'] = idx
            continue

        """ VFrameFormat
        """
        buf = re.search(r'BA_DEF_\s+BO_\s+"VFrameFormat"\s+ENUM\s+(.+);', line)
        if buf:
            enum = buf[1].replace('"', '').split(',')
            msg_attr['VFrameFormat'] = {'ENUM': enum}
            continue
        buf = re.search(r'BA_DEF_DEF_\s+"VFrameFormat"\s+"(\w+)"', line)
        if 'VFrameFormat' in msg_attr and buf:
            idx = msg_attr['VFrameFormat']['ENUM'].index(buf[1])
            msg_attr['VFrameFormat']['Default'] = idx
            continue

        """ GenSigStartValue
        """
        buf = re.search(r'BA_DEF_\s+SG_\s+"GenSigStartValue"\s+', line)
        if buf:
            sig_attr['GenSigStartValue'] = {}
            continue
        buf = re.search(r'BA_DEF_DEF_\s+"GenSigStartValue"\s+(.+)\s*;', line)
        if 'GenSigStartValue' in sig_attr and buf:
            sig_attr['GenSigStartValue']['Default'] = float(buf[1])
            continue

    return msg_attr, sig_attr


if __name__ == "__main__":
    with codecs.open('../CCANFD1.dbc', 'r', encoding='latin1') as fd:
        lines = fd.read().splitlines()
        msg_attr, sig_attr = get_attribute(lines)
    print(msg_attr)
    print(sig_attr)
