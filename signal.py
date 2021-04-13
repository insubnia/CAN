#!/usr/local/bin/python3
import sys
from enum import Enum


class Signal(object):
    class ByteOrder(Enum):
        Motorola, Intel = range(2)

    class ValueType(Enum):
        Signed, Unsigned, Float, Double = range(4)

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

        if isinstance(byte_order, self.ByteOrder):
            self._byte_order = byte_order
        else:
            print("Invalid Byte Order")
            sys.exit()

        if isinstance(value_type, self.ValueType):
            self._value_type = value_type
        else:
            print("Ivalid Value Type")
            sys.exit()

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
