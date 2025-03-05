# from Message import Message
import math
import logging
from TermColor import TermColor


class Assert:
    def __init__(self, message, key, value, msg=None):
        self.logger = logging.getLogger(__class__.__name__)
        self.datatype = type(value)
        self.actual_value = message.get(key, self.datatype)
        self.key = key
        self.expected_value = value
        if self.actual_value is not None:
            assert type(self.actual_value) is self.datatype


    def as_string(self, color=False) -> str:
        raise NotImplementedError

    def __str__(self) -> str:
        return self.as_string(color=False)
    
    def __or__(self, other):
        return Or(self, other)

    def __and__(self, other):
        return And(self, other)

    def evaluate(self) -> bool:
        raise NotImplementedError

    def result(self, color=False) -> tuple[bool, str]:
        return self.evaluate(), self.as_string(color)


class And(Assert):
    def __init__(self, a:Assert, b:Assert):
        self.a = a
        self.b = b

    def evaluate(self) -> bool:
        return self.a.evaluate() and self.b.evaluate()

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.a.as_string(color)} {TermColor.OKCYAN}and{TermColor.ENDC} {self.b.as_string(color)}"
        else:
            return f"{self.a.as_string(color)} and {self.b.as_string(color)}"


class Or(Assert):
    def __init__(self, a:Assert, b:Assert):
        self.a = a
        self.b = b

    def evaluate(self) -> bool:
        return self.a.evaluate() or self.b.evaluate()

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.a.as_string(color)} {TermColor.OKCYAN}or{TermColor.ENDC} {self.b.as_string(color)}"
        else:
            return f"{self.a.as_string(color)} or {self.b.as_string(color)}"


class Exists(Assert):
    def __init__(self, message, key, msg=None):
        self.is_missing = message.is_missing(key)
        self.key = key

    def evaluate(self) -> bool:
        return not self.is_missing

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.key} exists: {not self.is_missing}"
        else:
            return f"{self.key} exists: {not self.is_missing}"


class Missing(Assert):
    def __init__(self, message, key, msg=None):
        self.is_missing = message.is_missing(key)
        self.key = key

    def evaluate(self) -> bool:
        return self.is_missing

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.key} is missing: {self.is_missing}"
        else:
            return f"{self.key} is missing: {self.is_missing}"


class Eq(Assert):
    def evaluate(self) -> bool:
        return self.actual_value == self.expected_value

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.key}: {self.expected_value} == {self.actual_value}"
        else:
            return f"{self.key}: {self.expected_value} == {self.actual_value}"


class Ne(Assert):
    def evaluate(self) -> bool:
        return self.actual_value != self.expected_value

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.key}: {self.expected_value} != {self.actual_value}"
        else:
            return f"{self.key}: {self.expected_value} != {self.actual_value}"


class Ge(Assert):
    def evaluate(self) -> bool:
        return self.actual_value >= self.expected_value

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.key}: {self.expected_value} >= {self.actual_value}"
        else:
            return f"{self.key}: {self.expected_value} >= {self.actual_value}"


class Le(Assert):
    def evaluate(self) -> bool:
        return self.actual_value <= self.expected_value

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.key}: {self.expected_value} <= {self.actual_value}"
        else:
            return f"{self.key}: {self.expected_value} <= {self.actual_value}"


class Gt(Assert):
    def __init__(self, h, key, value, tolerance):
        super().__init__(h, key, value)
        self.tolerance = tolerance

    def evaluate(self) -> bool:
        return math.fabs(self.actual_value - self.expected_value) > self.tolerance

    def as_string(self, color=False) -> str:
        if color:
            return f"{self.key}: {self.expected_value} > {self.actual_value} +/- {self.tolerance}"
        else:
            return f"{self.key}: {self.expected_value} > {self.actual_value} +/- {self.tolerance}"


class Fail(Assert):
    def __init__(self, msg):
        self.msg = msg

    def evaluate(self) -> bool:
        return False
    
    def as_string(self, color=False) -> str:
        return f"{self.msg}"


class Pass(Assert):
    def __init__(self, msg):
        self.msg = msg

    def evaluate(self) -> bool:
        return True

    def as_string(self, color=False) -> str:
        return f"{self.msg}"
