#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import logging

import numpy as np
from eccodes import (
    codes_get_double,
    codes_get_double_array,
    codes_get_long,
    codes_get_message,
    codes_get_native_type,
    codes_get_size,
    codes_get_string,
    codes_is_missing,
    codes_keys_iterator_get_name,
    codes_keys_iterator_new,
    codes_keys_iterator_next,
    codes_new_from_message,
    codes_release,
    codes_set_string,
)

from .Assert import Eq
from .KeyValue import KeyValue
from .Report import Report


class Message:
    def __init__(self, handle=None, message_buffer=None, position=None):
        assert position != 0
        assert handle is not None or message_buffer is not None
        assert (handle is not None and message_buffer is not None) is not True
        self.logger = logging.getLogger(__class__.__name__)

        self.__h = None
        if handle is not None:
            self.__h = handle
        elif message_buffer is not None:
            self.__h = codes_new_from_message(message_buffer)

        self.__position = position
        self.min = None
        self.max = None

    def __getitem__(self, key):
        return self.get(key)

    def get_report(self):
        report = Report("Message dump")
        iterator = codes_keys_iterator_new(self.__h, "ls")
        while iterator is not None and codes_keys_iterator_next(iterator):
            key = codes_keys_iterator_get_name(iterator)
            report.add(f"{key} = {self[key].value()}")
        report.add("")

        iterator = codes_keys_iterator_new(self.__h, "mars")
        while iterator is not None and codes_keys_iterator_next(iterator):
            key = codes_keys_iterator_get_name(iterator)
            report.add(f"{key} = {self[key].value()}")
        report.add("")

        report.add(f"model = {self['model'].value()}")
        report.add(f"paramId = {self['paramId'].value()}")
        report.add(f"discipline = {self['discipline'].value()}")
        report.add(f"parameterCategory = {self['parameterCategory'].value()}")
        report.add(f"parameterNumber = {self['parameterNumber'].value()}")
        report.add(
            f"typeOfStatisticalProcessing = {self['typeOfStatisticalProcessing'].value()}"
        )
        report.add(
            f"typeOfFirstFixedSurface = {self['typeOfFirstFixedSurface', int].value()}"
        )

        return report

    @property
    def handle(self):
        return self.__h

    def __del__(self):
        codes_release(self.__h)

    def set(self, key, value):
        if type(value) is KeyValue:
            value = value.value()
        codes_set_string(self.__h, key, value)

    def get(self, key, datatype=None) -> KeyValue:
        try:
            if datatype is None:
                datatype = codes_get_native_type(self.__h, key)
            else:
                assert datatype is int or datatype is float or datatype is str

            if datatype is int:
                return KeyValue(key, codes_get_long(self.__h, key))
            elif datatype is float:
                return KeyValue(key, codes_get_double(self.__h, key))
            elif datatype is str:
                return KeyValue(key, codes_get_string(self.__h, key))
            else:
                self.logger.debug(f"Unknown datatype: {datatype}")
                return KeyValue(key, None)
        except Exception:
            self.logger.debug(f"KeyError: {key}")
            return KeyValue(key, None)

    def get_size(self, key) -> int:
        return codes_get_size(self.__h, key)

    def get_double_array(self, key) -> np.ndarray:
        return codes_get_double_array(self.__h, key)

    def get_buffer(self) -> bytes:
        return codes_get_message(self.__h)

    # Check whether the given key has the value 'missing'
    def is_missing(self, key) -> bool:
        return False if codes_is_missing(self.__h, key) == 0 else True

    def position(self):
        return self.__position

    def minmax(self):
        if self.min is not None and self.max is not None:
            return self.min, self.max

        try:
            values = self.get_double_array("values")
        except Exception:
            return

        bitmap = not Eq(self, "bitMapIndicator", 255).status()

        if bitmap:
            missing = self.get("missingValue")
            it = (v for v in values if v != missing)
            try:
                m = M = next(it)
            except StopIteration:
                m = M = missing
            else:
                for v in it:
                    if v < m:
                        m = v
                    elif v > M:
                        M = v
        else:
            m = min(values)
            M = max(values)

        self.min, self.max = m, M
        return m, M
