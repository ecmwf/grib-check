from Message import Message
import math
import logging
from Assert import Eq
from Grib import Grib
from Report import Report


        
class Test:
    def __init__(self, message: Message, key: str, value):
        raise NotImplementedError

    def run(self) -> tuple[bool, Report]:
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

    def run(self) -> tuple[bool, Report]:
        data = self.__parameter
        for kv in data["expected"]:
            key = kv["key"]
            value = kv["value"]
            try:
                self._check("equal", self.__message, Eq(self.__message, key, value))
            except NotImplementedError:
                raise NotImplementedError("Not implemented")
            except FloatingPointError as e:
                pass

        for check_func in data["checks"]:
            print(f"  {check_func}")
            result = self.__check_map[check_func](self.__message, data)
            if result:
                print(f"  {check_func}: PASSED")
            else:
                print(f"  {check_func}: FAILED")

        return (False, Report())
    
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

    def run(self) -> tuple[bool, Report]:
        data = self.__parameter
        report = Report()
        results = []
        for check_func in data["checks"]:
            result, checks_report = self.__check_map[check_func](self.__message, data)
            results.append(result)
            result_str = "PASSED" if result else "FAILED"
            report.add(f"{result_str}: {check_func}")
            report.add(checks_report)

        return (all(results), report)
