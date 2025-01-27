# from Message import Message
import math
import logging

logger = logging.getLogger(__name__)


class Assert:
    def __init__(self, message, key, value):
        self.datatype = type(value)
        self.actual_value = message.get(key, self.datatype)
        self.key = key
        self.expected_value = value
        assert type(self.actual_value) is self.datatype

    def evaluate(self) -> bool:
        raise NotImplementedError

    def status_msg(self) -> str:
        raise NotImplementedError

    def _evaluate_str(self) -> str:
        if self.evaluate():
            return "PASSED"
        else:
            return "FAILED"


class Eq(Assert):
    def evaluate(self) -> bool:
        return self.actual_value == self.expected_value

    def status_msg(self) -> str:
        return f"{self._evaluate_str()}: {self.key}: {self.expected_value} == {self.actual_value}"


class Ne(Assert):
    def evaluate(self) -> bool:
        return self.actual_value != self.expected_value

    def status_msg(self) -> str:
        return f"{self._evaluate_str()}: {self.key}: {self.expected_value} != {self.actual_value}"


class Ge(Assert):
    def evaluate(self) -> bool:
        return self.actual_value >= self.expected_value

    def status_msg(self) -> str:
        return f"{self._evaluate_str()}: {self.key}: {self.expected_value} >= {self.actual_value}"


class Le(Assert):
    def evaluate(self) -> bool:
        return self.actual_value <= self.expected_value

    def status_msg(self) -> str:
        return f"{self._evaluate_str()}: {self.key}: {self.expected_value} <= {self.actual_value}"


class Gt(Assert):
    def __init__(self, h, key, value, tolerance):
        super().__init__(h, key, value)
        self.tolerance = tolerance

    def evaluate(self) -> bool:
        return math.fabs(self.actual_value - self.expected_value) > self.tolerance

    def status_msg(self) -> str:
        return f"{self._evaluate_str()}: {self.key}: {self.expected_value} > {self.actual_value} +/- {self.tolerance}"
