#!/usr/local/bin/python3
from .signal import Signal


class Message(object):
    def __init__(self,
                 frame_id,
                 name,
                 length,
                 senders=None,  # TODO: implement multi senders
                 signals=None,
                 comment=None,
                 send_type=None,
                 cycle_time=None,
                 is_extended=False,
                 bus_name=None,
                 protocol=None):
        self._frame_id = frame_id
        self._name = name
        self._length = length
        self._senders = senders or []
        self._signals = signals or {}
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
        print((f'<Message> {self._name} (0x{self._frame_id:03X})\n' if print_name else ""),
              '+' + '-' * 106 + '+\n'
              '| {:3} | {:34} | {:3} | {:8} | {:8} | {:6} | {:6} | {:6} | {:6} |\n'.
              format("SB", "Name", "Len", "Endian", "Sign", "Factor", "Offset", "Min", "Max"),
              '|' + '=' * 106 + '|', sep='')
        for start_bit in sorted(self._signals):
            self.print_signal(start_bit)
        print('+' + '-' * 106 + '+' + '\n')
