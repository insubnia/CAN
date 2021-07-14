#!/usr/local/bin/python3
import re
import codecs
from enum import Enum

GenMsgCycleTime, GenMsgSendType, VFrameFormat, GenSigSendType, GenSigStartValue = None, None, None, None, None


def get_attribute(lines):
    for line in lines:
        global GenMsgCycleTime, GenMsgSendType, VFrameFormat, GenSigSendType, GenSigStartValue

        """ GenMsgCycleTime
        """
        buf = re.search(r'BA_DEF_\s+BO_\s+"GenMsgCycleTime"\s+INT', line)
        if buf:
            class GenMsgCycleTime(object):
                def __init__(self):
                    self.default = None
            continue
        buf = re.search(r'BA_DEF_DEF_\s+"GenMsgCycleTime"\s+(\d+)', line)
        if GenMsgCycleTime and buf:
            GenMsgCycleTime.default = int(buf[1])
            continue

        """ GenMsgSendType
        """
        buf = re.search(r'BA_DEF_\s+BO_\s+"GenMsgSendType"\s+ENUM\s+(.+);', line)
        if buf:
            _list = buf[1].replace('"', '').replace(' ', '').split(',')
            GenMsgSendType = Enum('GenMsgSendType', [(e, _list.index(e)) for e in set(_list)])
            GenMsgSendType.default = None
            continue
        buf = re.search(r'BA_DEF_DEF_\s+"GenMsgSendType"\s+"(\w+)"', line)
        if buf:
            GenMsgSendType.default = GenMsgSendType[buf[1]]
            continue

        """ VFrameFormat
        """
        buf = re.search(r'BA_DEF_\s+BO_\s+"VFrameFormat"\s+ENUM\s+(.+);', line)
        if buf:
            _list = buf[1].replace('"', '').replace(' ', '').split(',')
            VFrameFormat = Enum('VFrameFormat', [(e, _list.index(e)) for e in set(_list)])
            VFrameFormat.default = None
            continue
        buf = re.search(r'BA_DEF_DEF_\s+"VFrameFormat"\s+"(\w+)"', line)
        if VFrameFormat and buf:
            VFrameFormat.default = VFrameFormat[buf[1]]
            continue

        """ GenSigSendType
        """
        buf = re.search(r'BA_DEF_\s+SG_\s+"GenSigSendType"\s+ENUM\s+(.+);', line)
        if buf:
            _list = buf[1].replace('"', '').replace(' ', '').split(',')
            GenSigSendType = Enum('GenSigSendType', [(e, _list.index(e)) for e in set(_list)])
            GenSigSendType.default = None
            continue
        buf = re.search(r'BA_DEF_DEF_\s+"GenSigSendType"\s+"(\w+)"', line)
        if GenSigSendType and buf:
            GenSigSendType.default = GenSigSendType[buf[1]]
            continue

        """ GenSigStartValue
        """
        buf = re.search(r'BA_DEF_\s+SG_\s+"GenSigStartValue"\s+', line)
        if buf:
            class GenSigStartValue(object):
                def __init__(self):
                    self.default = None
            continue
        buf = re.search(r'BA_DEF_DEF_\s+"GenSigStartValue"\s+(.+)\s*;', line)
        if GenSigStartValue and buf:
            GenSigStartValue.default = float(buf[1])
            continue

    return GenMsgCycleTime, GenMsgSendType, VFrameFormat, GenSigSendType, GenSigStartValue


if __name__ == "__main__":
    with codecs.open('./DBCs/X50_ECAN.dbc', 'r', encoding='latin1') as fd:
        lines = fd.read().splitlines()
        GenMsgCycleTime, GenMsgSendType, VFrameFormat, GenSigSendType, GenSigStartValue = get_attribute(lines)
