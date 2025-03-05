from Message import Message
import math
import logging
from Assert import Eq, Fail, Pass
from Grib import Grib
from Report import Report


        
class Test:
    def __init__(self, message: Message, key: str, value):
        raise NotImplementedError

    def run(self) -> Report:
        raise NotImplementedError

    def _evaluate_str(self) -> str:
        return "PASSED" if self.run() else "FAILED"

class WmoTest(Test):
    def __init__(self, message: Message, parameter: dict, check_map: dict):
        self.logger = logging.getLogger(__class__.__name__)
        self.__message = message
        self.__parameter = parameter
        self.__check_map = check_map

    def _check(self, name, message, a):
        self.logger.debug(f"_check({name}, {a})")
        return a.evaluate()

    def run(self) -> Report:
        data = self.__parameter
        report = Report()
        expected_report = Report()
        for kv in data["expected"]:
            key = kv["key"]
            value = kv["value"]
            try:
                expected_report.add(Eq(self.__message, key, value))
            except NotImplementedError:
                raise NotImplementedError("Not implemented")
            except FloatingPointError as e:
                pass

        status, _ = expected_report.summary()
        if status:
            report.add(Pass("Check expected values"))
        else:
            report.add(Fail("Check expected values"))
        report.add(expected_report)

        for check_func in data["checks"]:
            check_report = self.__check_map[check_func](self.__message, data)
            status, _ = check_report.summary()
            if status:
                report.add(Pass(f"{check_func}"))
            else:
                report.add(Fail(f"{check_func}"))
            report.add(check_report)

        return report
    
class TiggeTest(Test):
    def __init__(self, message: Message, parameter: dict, check_map: dict):
        self.logger = logging.getLogger(__class__.__name__)
        assert parameter is not None
        assert message is not None
        assert check_map is not None

        self.__message = message
        self.__parameter = parameter
        self.__check_map = check_map

    def _check(self, name, message, a):
        self.logger.debug(f"_check({name}, {a.status_msg()})")
        if not a.evaluate():
            pass

    def run(self) -> Report:
        data = self.__parameter
        report = Report()
        # results = []
        for check_func in data["checks"]:
            checks_report = self.__check_map[check_func](self.__message, data)
            result, _ = checks_report.summary()
            if result:
                report.add(Pass(f"{check_func}"))
            else:
                report.add(Fail(f"{check_func}"))
            report.add(checks_report)

        return report
