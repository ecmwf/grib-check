from Message import Message
import math
import logging
from Assert import Eq
from Grib import Grib

logger = logging.getLogger(__name__)

        
class Test:
    def __init__(self, message: Message, key: str, value):
        raise NotImplementedError

    def score(self):
        raise NotImplementedError

    def run(self) -> bool:
        raise NotImplementedError

    def _evaluate_str(self) -> str:
        if self.run():
            return "PASSED"
        else:
            return "FAILED"


class WmoTest(Test):
    def __init__(self, message: Message, parameter: dict, check_map: dict):
        self.__message = message
        self.__parameter = parameter
        self.__check_map = check_map

    def _check(self, name, message, a):
        logger.debug(f"_check({name}, {a})")
        return a.evaluate()

    def run(self) -> bool:
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

        return False
    
class TiggeTest(Test):
    def __init__(self, message: Message, parameter: dict, check_map: dict):
        assert parameter is not None
        assert message is not None
        assert check_map is not None

        self.__message = message
        self.__parameter = parameter
        self.__check_map = check_map

    def _check(self, name, message, a):
        logger.debug(f"_check({name}, {a.status_msg()})")
        if not a.evaluate():
            pass

    def run(self) -> bool:
        data = self.__parameter
        for check_func in data["checks"]:
            result, summary = self.__check_map[check_func](self.__message, data)
            if result:
                print(f"  PASSED: {check_func}")
            else:
                print(f"  FAILED: {check_func}")

            if summary:
                [print(f"    {s}") for s in summary]

        return False
