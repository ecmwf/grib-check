# from os import writev
import sys
import logging
from IndexedLookupTable import IndexedLookupTable
from Test import Test
from Message import Message

logger = logging.getLogger(__name__)


class CheckEngine:
    def __init__(
        self,
        tests: IndexedLookupTable,
        check_map: dict,
        valueflg=False,
        warnflg=False,
    ):
        self.__filename = ""
        self.__error = 0
        self.__warning = 0
        self.__field = 0
        self.__param = "unknown"

        self.__valueflg = valueflg
        self.__warnflg = warnflg

        self._check_map = check_map
        assert tests is not None
        self._test_store = tests 


    def _create_test(self, message:Message, parameters:dict) -> Test:
        raise NotImplementedError


    def __save(self, message, name, f):
        if f is None:
            return

        try:
            buffer = message.get_buffer()
        except Exception as e:
            print(
                "%s, field %d [%s]: cannot get message: %s"
                % (self.__filename, self.__field, self.__param, str(e))
            )
            sys.exit(1)

        try:
            f.write(bytearray(buffer))
        except Exception as e:
            print(str(e))
            sys.exit(1)

    def __output_key_value(self, message, name):
        print(f"{name}={message.get(name)}")

    def validate(self, message):
        keys = self._test_store.get_index_keys()
        # Use datatype=int for fast lookup. Potential issue if the key is not an integer
        index = {key: message.get(key, datatype=dtype) for (key, dtype) in keys.items()}
        kv = self._test_store.get_element(index)
        test = self._create_test(message, kv)
        return test.run() if test is not None else False

    def get_error_counter(self):
        return self.__error

    def get_warning_counter(self):
        return self.__warning
