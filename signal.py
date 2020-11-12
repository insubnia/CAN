#!/usr/local/bin/python3
from enum import Enum


class Signal(object):
    ByteOrder = Enum('ByteOrder', 'Motorola Intel')
    ValueType = Enum('ValueType', 'Signed Unsigned Float Double')

    def __init__(self,
                 start_bit,
                 name,
                 length,
                 byte_order,
                 value_type,
                 scale,
                 offset,
                 minimum,
                 maximum,
                 unit=None,
                 receivers=None,
                 initial=None,
                 choices=None,
                 comment=None,
                 send_type=None,
                 is_multiplexer=False,
                 multiplexer_ids=None,
                 multiplexer_signal=None):
        self._start_bit = start_bit
        self._name = name
        self._length = length
        if byte_order not in self.ByteOrder:
            raise ValueError("Invalid Byte Order")
        else:
            self._byte_order = byte_order
        self._value_type = value_type
        self._scale = scale
        self._offset = offset
        self._minimum = minimum
        self._maximum = maximum
        self._unit = unit
        self._receivers = receivers or []
        self._initial = initial
        self._choices = choices
        self._comment = comment
        self._send_type = send_type
        self._is_multiplexer = is_multiplexer
        self._multiplexer_ids = multiplexer_ids
        self._multiplexer_signal = multiplexer_signal


if __name__ == '__main__':
    print(Signal.ByteOrder.Intel)
    print(Signal.ValueType.Double.value)
