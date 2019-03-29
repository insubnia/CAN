#!/usr/local/bin/python3
import re
import codecs


class Message(object):
    def __init__(self,
                 frame_id,
                 name,
                 length,
                 senders,  # TODO: implement multi senders
                 signals,
                 comment=None,
                 send_type=None,
                 cycle_time=None,
                 is_extended=False,
                 bus_name=None,
                 protocol=None):
        self._frame_id = frame_id
        self._name = name
        self._length = length
        self._senders = senders if senders else []
        self._signals = signals
        self._comment = comment
        self._send_type = send_type
        self._cycle_time = cycle_time
        self._is_extended = is_extended
        self._bus_name = bus_name
        self._protocol = protocol

    def add_signal(self, signal):
        self._signals[signal._start_bit] = signal

    def print_signal(self, start_bit, _end='\n'):
        s = self._signals[start_bit]
        print('| {:3} | {:34} | {:3} | {:>8} | {:>8} | {:6g} | {:6g} | {:6g} | {:6g} |'.
              format(s._start_bit, s._name, s._length,
                     "Intel" if s._byte_order == Signal.LITTLE_ENDIAN else "Motorola",
                     "Signed" if s._is_signed else "Unsigned",
                     s._scale, s._offset, s._minimum, s._maximum), end=_end)

    def print_signal_list(self, print_name=True):
        print(("<Message> %s (0x%03X)\n" % (self._name, self._frame_id) if print_name else "") +
              '+' + '-' * 106 + '+\n'
              '| {:3} | {:34} | {:3} | {:8} | {:8} | {:6} | {:6} | {:6} | {:6} |\n'.
              format("SB", "Name", "Len", "Endian", "Sign", "Factor", "Offset", "Min", "Max") +
              '|' + '=' * 106 + '|')
        for start_bit in sorted(self._signals):
            self.print_signal(start_bit)
        print('+' + '-' * 106 + '+' + '\n')


class Signal(object):
    BIG_ENDIAN = 0
    LITTLE_ENDIAN = 1

    def __init__(self,
                 start_bit,
                 name,
                 length,
                 byte_order,
                 is_signed,
                 scale,
                 offset,
                 minimum,
                 maximum,
                 unit=None,
                 receivers=None,
                 initial=None,
                 choices=None,
                 comment=None,
                 is_multiplexer=False,
                 multiplexer_ids=None,
                 multiplexer_signal=None,
                 is_float=False):
        self._start_bit = start_bit
        self._name = name
        self._length = length
        self._byte_order = byte_order
        self._is_signed = is_signed
        self._scale = scale
        self._offset = offset
        self._minimum = minimum
        self._maximum = maximum
        self._unit = unit
        self._receivers = [] if receivers is None else receivers
        self._initial = initial
        self._choices = choices
        self._comment = comment
        self._is_multiplexer = is_multiplexer
        self._multiplexer_ids = multiplexer_ids
        self._multiplexer_signal = multiplexer_signal
        self._is_float = is_float


if __name__ == "__main__":
    pass
