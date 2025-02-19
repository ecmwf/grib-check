from os import curdir
import numpy as np
from eccodes import (
    codes_release,
    codes_is_missing,
    codes_get_message,
    codes_get_size,
    codes_get_long,
    codes_get_double,
    codes_get_string,
    codes_get_double_array,
    codes_get_native_type,
    codes_keys_iterator_new,
    codes_keys_iterator_next,
    codes_keys_iterator_get_name,
    KeyValueNotFoundError,
)
import logging
from inspect import currentframe, getframeinfo
from Assert import Eq

logger = logging.getLogger(__name__)


class Message:
    def __init__(self, h, position=None):
        self.__h = h
        self.__position = position

    def __str__(self):
        output = [f"Message[{self.__position}]"]
        iterator = codes_keys_iterator_new(self.__h, "ls") 
        while iterator is not None and codes_keys_iterator_next(iterator):
            key = codes_keys_iterator_get_name(iterator)
            output.append(f"{key}={self.get(key)}")

        output.append("")

        iterator = codes_keys_iterator_new(self.__h, "mars") 
        while iterator is not None and codes_keys_iterator_next(iterator):
            key = codes_keys_iterator_get_name(iterator)
            output.append(f"{key}={self.get(key)}")

        output.append("")

        output.append(f"model={self.get('model')}")
        output.append(f"paramId={self.get('paramId')}")
        output.append(f"discipline={self.get('discipline')}")
        output.append(f"parameterCategory={self.get('parameterCategory')}")
        output.append(f"parameterNumber={self.get('parameterNumber')}")
        output.append(f"typeOfStatisticalProcessing={self.get('typeOfStatisticalProcessing')}")
        output.append(f"typeOfFirstFixedSurface={self.get('typeOfFirstFixedSurface', int)}")

        return "\n".join(output)

    @property
    def handle(self):
        return self.__h

    def __del__(self):
        codes_release(self.__h)

    def get(self, key, datatype=None):
        try:
            if datatype is None:
                datatype = codes_get_native_type(self.__h, key)
            else:
                assert datatype is int or datatype is float or datatype is str

            if datatype is int:
                return codes_get_long(self.__h, key)
            elif datatype is float:
                return codes_get_double(self.__h, key)
            elif datatype is str:
                return codes_get_string(self.__h, key)
            else:
                logger.debug(
                    f"key: {key}, datatype: {datatype}, frameinfo: {getframeinfo(currentframe()).lineno}"
                )
                return None
        except Exception:
            logger.debug(
                f"key: {key}, Exception, frameinfo: {getframeinfo(currentframe()).lineno}"
            )
            return None

    def get_size(self, key) -> int:
        return codes_get_size(self.__h, key)

    def get_double_array(self, key) -> np.ndarray:
        return codes_get_double_array(self.__h, key)

    def get_buffer(self, key) -> bytes:
        return codes_get_message(self.__h)

    def is_missing(self, key) -> bool:
        try:
            return False if codes_is_missing(self.__h, key) == 0 else True
        except KeyValueNotFoundError:
            return True

    def position(self):
        return self.__position

    def minmax(self):
        bitmap = not Eq(self, "bitMapIndicator", 255).evaluate()

        try:
            self.__values = self.get_double_array("values")
        except Exception as e:
            return

        if bitmap:
            missing = self.get("missingValue")
            min_value = max_value = missing
            for value in self.__values:
                if (min_value == missing) or (
                    (value != missing) and (min_value > value)
                ):
                    min_value = value
                if (max_value == missing) or (
                    (value != missing) and (max_value < value)
                ):
                    max_value = value
        else:
            min_value = max_value = self.__values[0]
            for value in self.__values:
                if min_value > value:
                    min_value = value
                if max_value < value:
                    max_value = value

        return min_value, max_value
