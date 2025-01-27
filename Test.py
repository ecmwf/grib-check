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
        logger.debug(f"_check({name}, {a.status_msg()})")
        if not a.evaluate():
            pass
            # print(f"{self.__filename}, field {message.position()}: {a.status_msg()}")
            # print(f"Expected: {a.expected_value}, Actual: {a.actual_value}")
            # self.__error += 1

    # def score(self) -> list:
    #     score = 0
    #     max_score = len(self.__parameter["pairs"])
    #     for kv in self.__parameter["pairs"]:
    #         key = kv["key"]
    #         value = kv["value"]
    #         msg_value = self.__message.get(key)
    #         if msg_value == value:
    #             score += 1
    #     return [score, max_score]


    def run(self) -> bool:
        # i = 0
        data = self.__parameter
        for kv in data["expected"]:
            key = kv["key"]
            value = kv["value"]
            try:
                val = self.__message.get(key)
                print(f"key val: {key}, {val}, {value}")
                self._check("equal", self.__message, Eq(self.__message, key, value))
            except NotImplementedError:
                raise NotImplementedError("Not implemented")
            except FloatingPointError as e:
                pass
                # print(
                #     "%s, field %d [%s]: cannot get %s: %s"
                #     % (self.__filename, self.__field, self.__param, key, str(e))
                # )

        for check_func in data["checks"]:
            self.__check_map[check_func](self.__message, data)
            # self.__check_map[check_func](h)
            # i += 1
            # print('=========================')
            # print('%s -> %d %d' , (self.__param, match, best))
            # for pair in  parameters[match].pairs:
            #     print('%s val -> %ld %d' % (pair['key'], pair['value'], j))
            #     j += 1
            # print('matched parameter: %s' % self.__param)
        # if self.__error == 0:
        #     print(f"{self.__filename}, field {message.position()}: OK")

        return False

    # def status_msg(self) -> str:
    #     return f"{self._evaluate_str()}: {self.key}: {self.expected_value} == {self.actual_value}"
