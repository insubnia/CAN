#!/usr/local/bin/python3
import enum


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
                 send_type=None,
                 value_type=None,
                 is_multiplexer=False,
                 multiplexer_ids=None,
                 multiplexer_signal=None):
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
        self._receivers = receivers or []
        self._initial = initial
        self._choices = choices
        self._comment = comment
        self._send_type = send_type
        self._value_type = value_type
        self._is_multiplexer = is_multiplexer
        self._multiplexer_ids = multiplexer_ids
        self._multiplexer_signal = multiplexer_signal
