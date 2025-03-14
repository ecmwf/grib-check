# from Message import Message
import math
import logging
from TermColor import TermColor

# def DBL_EQUAL(d1, d2, tolerance) -> int:
#     if type(KeyValue) is type(d1) and type(KeyValue) is type(d2):
#         v1 = d1.value()
#         v2 = d2.value()
#     return math.fabs(d1 - d2) <= tolerance

class Assert:
    def __init__(self, msg=None):
        self._logger = logging.getLogger(__class__.__name__)
        # self._datatype = type(value)
        # self._actual_value = message.get(key, self._datatype)
        # self._key = key
        # self._expected_value = value
        # if self._actual_value is not None:
        #     assert type(self._actual_value) is self._datatype
        self._status = True

    def as_string(self, color=False) -> str:
        raise NotImplementedError

    def __str__(self) -> str:
        return self.as_string(color=False)
    
    def __or__(self, other):
        return Or(self, other)

    def __and__(self, other):
        return And(self, other)

    def status(self) -> bool:
        assert type(self._status) is bool
        return self._status


class AssertTrue(Assert):
    def __init__(self, status, msg):
        self._status = bool(status)
        self.__msg = msg

    def status(self) -> bool:
        assert type(self._status) is bool
        return self._status

    def as_string(self, color=False) -> str:
        return f"{self.__msg}"


class And(Assert):
    def __init__(self, lhs:Assert, rhs:Assert):
        self.__lsh = lhs
        self.__rsh = rhs
        self._status = self.__lsh.status() and self.__rsh.status()

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh.as_string(color)} {TermColor.OKCYAN}and{TermColor.ENDC} {self.__rsh.as_string(color)}"
        else:
            return f"{self.__lsh.as_string(color)} and {self.__rsh.as_string(color)}"


class Or(Assert):
    def __init__(self, lhs:Assert, rhs:Assert):
        self.__lhs = lhs
        self.__rhs = rhs
        self._status = self.__lhs.status() or self.__rhs.status()

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__lhs.as_string(color)} {TermColor.OKCYAN}or{TermColor.ENDC} {self.__rhs.as_string(color)}"
        else:
            return f"{self.__lhs.as_string(color)} or {self.__rhs.as_string(color)}"


class IsIn(Assert):
    def __init__(self, actual, expected, msg=None):
        self.__actual = actual
        self.__expected = expected
        self._status = self.__actual.value() in self.__expected

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__actual} in {self.__expected}"
        else:
            return f"{self.__actual} in {self.__expected}"


class IsMultipleOf(Assert):
    def __init__(self, actual, multiplier, msg=None):
        self.__actual = actual
        self.__multiplier = multiplier
        self.__mod_value = self.__actual % self.__multiplier
        self._status = self.__mod_value == 0

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__mod_value} == 0"
        else:
            return f"{self.__mod_value} == 0"


class Exists(Assert):
    def __init__(self, message, key, msg=None):
        self.__is_missing = message.is_missing(key)
        self.__key = key
        self._status = not self.__is_missing

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__key} exists: {not self.__is_missing}"
        else:
            return f"{self.__key} exists: {not self.__is_missing}"


class Missing(Assert):
    def __init__(self, message, key, msg=None):
        self.__is_missing = message.is_missing(key)
        self.__key = key
        self._status = self.__is_missing

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__key} is missing: {self.__is_missing}"
        else:
            return f"{self.__key} is missing: {self.__is_missing}"


class Eq(Assert):
    def __init__(self, lsh, rhs, msg=None):
        self.__lsh = lsh
        self.__rhs = rhs
        self._status = self.__lsh == self.__rhs

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh} == {self.__rhs}"
        else:
            return f"{self.__lsh} == {self.__rhs}"


class EqDbl(Assert):
    def __init__(self, lsh, rhs, tolerance, msg=None):
        self.__lsh = lsh
        self.__rhs = rhs
        self.__tolerance = tolerance
        self._status = math.fabs(self.__lsh.value() - self.__rhs.value()) <= self.__tolerance

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh} == {self.__rhs} within {self.__tolerance}"
        else:
            return f"{self.__lsh} == {self.__rhs} within {self.__tolerance}"


class Ne(Assert):
    def __init__(self, lsh, rhs, msg=None):
        self.__lsh = lsh
        self.__rhs = rhs
        self._status = self.__lsh != self.__rhs

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh} != {self.__rhs}"
        else:
            return f"{self.__lsh} != {self.__rhs}"


class Ge(Assert):
    def __init__(self, lsh, rhs, msg=None):
        self.__lsh = lsh
        self.__rhs = rhs
        self._status = self.__lsh >= self.__rhs

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh} >= {self.__rhs}"
        else:
            return f"{self.__lsh} >= {self.__rhs}"


class Le(Assert):
    def __init__(self, lsh, rhs, msg=None):
        self.__lsh = lsh
        self.__rhs = rhs
        self._status = self.__lsh <= self.__rhs

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh} <= {self.__rhs}"
        else:
            return f"{self.__lsh} <= {self.__rhs}"


class Gt(Assert):
    def __init__(self, lsh, rhs, msg=None):
        self.__lsh = lsh
        self.__rhs = rhs
        self._status = self.__lsh > self.__rhs

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh} > {self.__rhs}"
        else:
            return f"{self.__lsh} > {self.__rhs}"

class Lt(Assert):
    def __init__(self, lsh, rhs, msg=None):
        self.__lsh = lsh
        self.__rhs = rhs
        self._status = self.__lsh < self.__rhs

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh} < {self.__rhs}"
        else:
            return f"{self.__lsh} < {self.__rhs}"


class Fail(Assert):
    def __init__(self, msg):
        self.__msg = msg
        self._status = False

    def as_string(self, color=False) -> str:
        return f"{self.__msg}"


class Pass(Assert):
    def __init__(self, msg):
        self.__msg = msg
        self._status = True

    def as_string(self, color=False) -> str:
        return f"{self.__msg}"
