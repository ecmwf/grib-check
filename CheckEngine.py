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
        good=None,
        bad=None,
    ):

        # self.__tests = list()
        # self.__last_n = 0
        # self.__values = None

        self.__filename = ""
        self.__error = 0
        self.__warning = 0
        self.__field = 0
        self.__param = "unknown"

        self.__valueflg = valueflg
        self.__warnflg = warnflg
        self.__good = good
        self.__bad = bad

        self._check_map = check_map
        assert tests is not None
        self._test_store = tests 

        self.__fgood = None
        if self.__good:
            self.__fgood = open(self.__good, "w")
            if not self.__fgood:
                print("Couldn't open %s" % self.__good)
                sys.exit(1)

        self.__fbad = None
        if self.__bad:
            self.__fbad = open(self.__bad, "w")
            if not self.__fbad:
                print("Couldn't open %s" % self.__bad)
                sys.exit(1)

    def __del__(self):
        if self.__fgood is not None and not self.__fgood.closed:
            self.__fgood.close()
        if self.__fbad is not None and not self.__fbad.closed:
            self.__fbad.close()

    def _create_test(self, message: Message, parameters:dict) -> Test:
        raise NotImplementedError

    # def warn(const char* name,int a):
    #   if not a:
    #       print('%s, field %d [%s]: %s failed' (filename, field, param, name));
    #       warning += 1;

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
        index = {key: message.get(key) for key in keys}
        kv = self._test_store.get_element(index)
        test = self._create_test(message, kv)
        return test.run() if test is not None else False

    def get_error_counter(self):
        return self.__error

    def get_warning_counter(self):
        return self.__warning

    def create_test(self, message, parameter) -> Test:
        raise NotImplementedError
