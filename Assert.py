# from Message import Message
import math
import logging
from TermColor import TermColor

def DBL_EQUAL(d1, d2, tolerance) -> int:
    return math.fabs(d1 - d2) <= tolerance

class Assert:
    def __init__(self, message, key, value, msg=None):
        self._logger = logging.getLogger(__class__.__name__)
        self._datatype = type(value)
        self._actual_value = message.get(key, self._datatype)
        self._key = key
        self._expected_value = value
        if self._actual_value is not None:
            assert type(self._actual_value) is self._datatype
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
        self._status = status 
        self.__msg = msg

    def status(self) -> bool:
        assert type(self._status) is bool
        return self._status

    def as_string(self, color=False) -> str:
        return f"{self.__msg}"


class And(Assert):
    def __init__(self, a:Assert, b:Assert):
        self.a = a
        self.b = b
        self._status = self.a.status() and self.b.status()

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.a.as_string(color)} {TermColor.OKCYAN}and{TermColor.ENDC} {self.b.as_string(color)}"
        else:
            return f"{self.a.as_string(color)} and {self.b.as_string(color)}"


class Or(Assert):
    def __init__(self, a:Assert, b:Assert):
        self.__a = a
        self.__b = b
        self._status = self.__a.status() or self.__b.status()

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__a.as_string(color)} {TermColor.OKCYAN}or{TermColor.ENDC} {self.__b.as_string(color)}"
        else:
            return f"{self.__a.as_string(color)} or {self.__b.as_string(color)}"


class IsIn(Assert):
    def __init__(self, message, key, values, msg=None):
        self.__actual_value = message.get(key, list)
        self.__key = key
        self.__expected_values = values
        self._status = self.__actual_value in self.__expected_values

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.__key}: {self.__actual_value} in {self.__expected_values}"
        else:
            return f"{self.__key}: {self.__actual_value} in {self.__expected_values}"


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
    def __init__(self, h, key, value, msg=None):
        super().__init__(h, key, value, msg)
        self._status = self._actual_value == self._expected_value

    def as_string(self, color=False) -> str:
        if color:
            return f"{self._key}: {self._actual_value} == {self._expected_value}"
        else:
            return f"{self._key}: {self._actual_value} == {self._expected_value}"


class Ne(Assert):
    def __init__(self, h, key, value):
        super().__init__(h, key, value)
        self._status = self._actual_value != self._expected_value

    def as_string(self, color=False) -> str:
        if color:
            return f"{self._key}: {self._actual_value} != {self._expected_value}"
        else:
            return f"{self._key}: {self._actual_value} != {self._expected_value}"


class Ge(Assert):
    def __init__(self, h, key, value, msg=None):
        super().__init__(h, key, value, msg)
        self._status = self._actual_value >= self._expected_value

    def as_string(self, color=False) -> str:
        if color:
            return f"{self._key}: {self._actual_value} >= {self._expected_value}"
        else:
            return f"{self._key}: {self._actual_value} >= {self._expected_value}"


class Le(Assert):
    def __init__(self, h, key, value, msg=None):
        super().__init__(h, key, value, msg)
        self._status = self._actual_value <= self._expected_value

    def as_string(self, color=False) -> str:
        if color:
            return f"{self._key}: {self._actual_value} <= {self._actual_value}"
        else:
            return f"{self._key}: {self._actual_value} <= {self._actual_value}"


class Gt(Assert):
    def __init__(self, h, key, value, tolerance, msg=None):
        super().__init__(h, key, value, msg)
        self.__tolerance = tolerance
        self._status = self._actual_value > self._expected_value + self.__tolerance

    def as_string(self, color=False) -> str:
        if color:
            return f"{self._key}: {self._actual_value} > {self._expected_value} +/- {self.__tolerance}"
        else:
            return f"{self._key}: {self._actual_value} > {self._expected_value} +/- {self.__tolerance}"


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
