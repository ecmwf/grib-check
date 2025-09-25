#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#


import logging

# from Message import Message
import math

import numpy as np

from .TermColor import TermColor


class Assert:
    def __init__(self, comment=None):
        self._logger = logging.getLogger(__class__.__name__)
        self._status = True
        self._comment = comment
        raise NotImplementedError(
            "Assert class is abstract and should not be instantiated directly"
        )

    def as_string(self, color=False, comment_position="below") -> str:
        if comment_position == "right":
            comment = f" : ({self._comment})" if self._comment is not None else ""
        elif comment_position == "below":
            comment = f"\n{self._comment}" if self._comment is not None else ""
        else:
            raise ValueError("comment_position must be either 'right' or 'below'")

        if color:
            return (
                f"{self._as_string(color)}{TermColor.OKBLUE}{comment}{TermColor.ENDC}"
            )
        else:
            return f"{self._as_string(color)}{comment}"

    def __str__(self) -> str:
        return self.as_string(color=False, comment_position="right")

    def __or__(self, other):
        return Or(self, other)

    def __and__(self, other):
        return And(self, other)

    def _as_string(self, color=False) -> str:
        raise NotImplementedError

    def status(self) -> bool:
        assert type(self._status) is bool or type(self._status) is np.bool_
        return self._status


class AssertTrue(Assert):
    def __init__(self, status, msg, comment=None):
        self._status = bool(status)
        self._comment = comment
        self.__msg = msg

    def status(self) -> bool:
        assert type(self._status) is bool
        return self._status

    def _as_string(self, color=False) -> str:
        return f"{self.__msg}"


class And(Assert):
    def __init__(self, lhs: Assert, rhs: Assert, comment=None):
        self.__lsh = lhs
        self.__rsh = rhs
        self._comment = comment
        self._status = self.__lsh.status() and self.__rsh.status()

    def _as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh.as_string(color)} {TermColor.OKCYAN}and{TermColor.ENDC} {self.__rsh.as_string(color)}"
        else:
            return f"{self.__lsh.as_string(color)} and {self.__rsh.as_string(color)}"


class Or(Assert):
    def __init__(self, lhs: Assert, rhs: Assert, comment=None):
        self.__lhs = lhs
        self.__rhs = rhs
        self._status = self.__lhs.status() or self.__rhs.status()
        self._comment = comment

    def _as_string(self, color=False) -> str:
        if color:
            return f"{self.__lhs.as_string(color)} {TermColor.OKCYAN}or{TermColor.ENDC} {self.__rhs.as_string(color)}"
        else:
            return f"{self.__lhs.as_string(color)} or {self.__rhs.as_string(color)}"


class IsIn(Assert):
    def __init__(self, actual, expected, comment=None):
        self.__actual = actual
        self.__expected = expected
        self._status = self.__actual.value() in self.__expected
        self._comment = comment

    def _as_string(self, color=False) -> str:
        if color:
            return f"{self.__actual} in {self.__expected}"
        else:
            return f"{self.__actual} in {self.__expected}"


class IsMultipleOf(Assert):
    def __init__(self, actual, multiplier, comment=None):
        self.__actual = actual
        self.__multiplier = multiplier
        self.__mod_value = self.__actual % self.__multiplier
        self._status = self.__mod_value == 0
        self._comment = comment

    def _as_string(self, color=False) -> str:
        if color:
            return f"{self.__mod_value} == 0"
        else:
            return f"{self.__mod_value} == 0"


class Missing(Assert):
    def __init__(self, message, key, comment=None):
        self.__key_is_missing = message[key].value() is None
        if not self.__key_is_missing:
            self.__value_is_missing = message.is_missing(key)
            self._status = self.__value_is_missing
        else:
            self.__value_is_missing = None
            self._status = False
        self.__key = key
        self._comment = comment

    def _as_string(self, color=False) -> str:
        return f"{self.__key} exists({not self.__key_is_missing}) and has a missing value({None if self.__value_is_missing is None else self.__value_is_missing})"


class Exists(Assert):
    def __init__(self, message, key, comment=None):
        self.__key_is_missing = message[key].value() is None
        if not self.__key_is_missing:
            self.__value_is_missing = message.is_missing(key)
            self._status = not self.__value_is_missing
        else:
            self.__value_is_missing = None
            self._status = False
        self.__key = key
        self._comment = comment

    def _as_string(self, color=False) -> str:
        return f"{self.__key} exists({not self.__key_is_missing}) and has a non-missing value({None if self.__value_is_missing is None else not self.__value_is_missing})"


class Eq(Assert):
    def __init__(self, lsh, rhs, comment=None):
        self.__lsh = lsh
        self.__rhs = rhs
        self._status = self.__lsh == self.__rhs
        self._comment = comment

    def _as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh} == {self.__rhs}"
        else:
            return f"{self.__lsh} == {self.__rhs}"


class EqDbl(Assert):
    def __init__(self, lsh, rhs, tolerance, comment=None):
        self.__lsh = lsh
        self.__rhs = rhs
        self.__tolerance = tolerance
        self._status = math.fabs((self.__lsh - self.__rhs).value()) <= self.__tolerance
        self._comment = comment

    def _as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh} == {self.__rhs} within {self.__tolerance}"
        else:
            return f"{self.__lsh} == {self.__rhs} within {self.__tolerance}"


class Ne(Assert):
    def __init__(self, lsh, rhs, comment=None):
        self.__lsh = lsh
        self.__rhs = rhs
        self._status = self.__lsh != self.__rhs
        self._comment = comment

    def _as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh} != {self.__rhs}"
        else:
            return f"{self.__lsh} != {self.__rhs}"


class Ge(Assert):
    def __init__(self, lsh, rhs, comment=None):
        self.__lsh = lsh
        self.__rhs = rhs
        self._status = self.__lsh >= self.__rhs
        self._comment = comment

    def _as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh} >= {self.__rhs}"
        else:
            return f"{self.__lsh} >= {self.__rhs}"


class Le(Assert):
    def __init__(self, lsh, rhs, comment=None):
        self.__lsh = lsh
        self.__rhs = rhs
        self._status = self.__lsh <= self.__rhs
        self._comment = comment

    def _as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh} <= {self.__rhs}"
        else:
            return f"{self.__lsh} <= {self.__rhs}"


class Gt(Assert):
    def __init__(self, lsh, rhs, comment=None):
        self.__lsh = lsh
        self.__rhs = rhs
        self._status = self.__lsh > self.__rhs
        self._comment = comment

    def _as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh} > {self.__rhs}"
        else:
            return f"{self.__lsh} > {self.__rhs}"


class Lt(Assert):
    def __init__(self, lsh, rhs, comment=None):
        self.__lsh = lsh
        self.__rhs = rhs
        self._status = self.__lsh < self.__rhs
        self._comment = comment

    def _as_string(self, color=False) -> str:
        if color:
            return f"{self.__lsh} < {self.__rhs}"
        else:
            return f"{self.__lsh} < {self.__rhs}"


class Fail(Assert):
    def __init__(self, msg, comment=None):
        self._status = False
        self.__msg = msg
        self._comment = comment

    def _as_string(self, color=False) -> str:
        return f"{self.__msg}"


class Pass(Assert):
    def __init__(self, msg, comment=None):
        self._comment = comment
        self.__msg = msg
        self._status = True

    def _as_string(self, color=False) -> str:
        return f"{self.__msg}"
