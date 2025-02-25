# from Message import Message
import math
import logging

logger = logging.getLogger(__name__)


class Assert:
    def __init__(self, message, key, value, msg=None):
        self.datatype = type(value)
        self.actual_value = message.get(key, self.datatype)
        self.key = key
        self.expected_value = value
        assert type(self.actual_value) is self.datatype

    def __str__(self) -> str:
        raise NotImplementedError

    def __or__(self, other):
        self_status, self_status_msg = self.result()
        other_status, other_status_msg = other.result()
        status = self_status or other_status
        return status, f"{self_status_msg} or {other_status_msg}"

    def __and__(self, other):
        self_status, self_status_msg = self.result()
        other_status, other_status_msg = other.result()
        status = self_status and other_status
        return status, f"{self_status_msg} and {other_status_msg}"

    def evaluate(self) -> bool:
        raise NotImplementedError

    def result(self) -> tuple[bool, str]:
        return self.evaluate(), self.__str__()

class Exists(Assert):
    def __init__(self, message, key, msg=None):
        self.is_missing = message.is_missing(key)
        self.key = key

    def evaluate(self) -> bool:
        return not self.is_missing

    def __str__(self) -> str:
        return f"{self.key} exists"

class Missing(Assert):
    def __init__(self, message, key, msg=None):
        self.is_missing = message.is_missing(key)
        self.key = key

    def evaluate(self) -> bool:
        return self.is_missing

    def __str__(self) -> str:
        return f"{self.key} exists"

class Eq(Assert):
    def evaluate(self) -> bool:
        return self.actual_value == self.expected_value

    def __str__(self) -> str:
        return f"{self.key}: {self.expected_value} == {self.actual_value}"


class Ne(Assert):
    def evaluate(self) -> bool:
        return self.actual_value != self.expected_value

    def __str__(self) -> str:
        return f"{self.key}: {self.expected_value} != {self.actual_value}"


class Ge(Assert):
    def evaluate(self) -> bool:
        return self.actual_value >= self.expected_value

    def __str__(self) -> str:
        return f"{self.key}: {self.expected_value} >= {self.actual_value}"


class Le(Assert):
    def evaluate(self) -> bool:
        return self.actual_value <= self.expected_value

    def __str__(self) -> str:
        return f"{self.key}: {self.expected_value} <= {self.actual_value}"


class Gt(Assert):
    def __init__(self, h, key, value, tolerance):
        super().__init__(h, key, value)
        self.tolerance = tolerance

    def evaluate(self) -> bool:
        return math.fabs(self.actual_value - self.expected_value) > self.tolerance

    def __str__(self) -> str:
        return f"{self.key}: {self.expected_value} > {self.actual_value} +/- {self.tolerance}"
