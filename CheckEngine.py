# from os import writev
import sys
import logging
from LookupTable import SimpleLookupTable
from Test import Test
from Message import Message
from Report import Report


class CheckEngine:
    def __init__(
        self,
        tests: SimpleLookupTable,
        valueflg=False,
        warnflg=False,
    ):
        self.logger = logging.getLogger(__class__.__name__)
        self.logger.debug("CheckEngine.__init__")
        self.__filename = ""
        self.__error = 0
        self.__warning = 0
        self.__field = 0
        self.__param = "unknown"

        self.__valueflg = valueflg
        self.__warnflg = warnflg

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

    def validate(self, message) -> tuple[bool, Report]:
        report = Report()
        kv = self._test_store.get_element(message)
        if kv is not None:
            test = self._create_test(message, kv)
            result, test_report = test.run()
            report.add(test_report)
            return (result, report)
        else:
            self.logger.debug(f"Could not find parameter for: {message}")
            test_report = Report()
            test_report.add("Could not find parameter")
            test_sub_report = Report()
            test_sub_report.add(message.get_report())
            test_report.add(test_sub_report)
            report.add(test_report)
            return (False, report)


    def get_error_counter(self):
        return self.__error

    def get_warning_counter(self):
        return self.__warning
