from os import curdir
import numpy as np
from eccodes import (
    codes_release,
    codes_is_missing,
    codes_get_version_info,
    codes_get_message,
    codes_get_size,
    codes_get_long,
    codes_get_double,
    codes_get_string,
    codes_get_double_array,
    codes_get_native_type,
    codes_get_gaussian_latitudes,
    codes_set_string,
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
    # def get_double_array(self, key) -> list:
        return codes_get_double_array(self.__h, key)

    def get_buffer(self, key) -> bytes:
        return codes_get_message(self.__h)

    def is_missing(self, h, key) -> bool:
        try:
            return False if codes_is_missing(h, key) == 0 else True
        except KeyValueNotFoundError:
            return True

    def position(self):
        return self.__position

    def minmax(self):

        count = 0
        try:
            count = self.get_size("values")
        except Exception as e:
            # print(
            #     "%s, field %d [%s]: cannot get number of values: %s"
            #     % (self.__filename, self.__field, self.__param, str(e))
            # )
            # self.__error += 1
            return


        bitmap = not Eq(self, "bitMapIndicator", 255).evaluate()
        # self.__check(
        #     'eq(h,"numberOfDataPoints",count)',
        #     self._eq(h, "numberOfDataPoints", count),
        # )
        n = count
        try:
            self.__values = self.get_double_array("values")
        except Exception as e:
            # print(
            #     "%s, field %d [%s]: cannot get values: %s"
            #     % (self.__filename, self.__field, self.__param, str(e))
            # )
            # self.__error += 1
            return

        # if n != count:
        #     print(
        #         "%s, field %d [%s]: value count changed %ld -> %ld"
        #         % (self.__filename, self.__field, self.__param, count, n)
        #     )
        #     self.__error += 1
        #     return

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
