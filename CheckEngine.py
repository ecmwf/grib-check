import sys
import logging
from LookupTable import SimpleLookupTable
from Test import Test
from Message import Message
from Report import Report
from Assert import Fail


class CheckEngine:
    def __init__(self, tests: SimpleLookupTable):
        self.logger = logging.getLogger(__class__.__name__)
        assert tests is not None
        self._test_store = tests 

    def _create_test(self, message:Message, parameters:dict) -> Test:
        raise NotImplementedError

    def validate(self, message) -> Report:
        # report = Report(f"Message[{message.position()}]")
        report = Report()
        kv = self._test_store.get_element(message)
        if kv is not None:
            test = self._create_test(message, kv)
            report.add(test.run())
        else:
            self.logger.debug(f"Could not find parameter for: {message}")
            report.add(Fail("Could not find parameter"))
            test_sub_report = Report()
            test_sub_report.add(message.get_report())
            report.add(test_sub_report)

        return report
