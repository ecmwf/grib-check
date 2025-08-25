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
from enum import Enum


class OpType(Enum):
    DASH = 0
    DOT = 1
    NONE = 2


class KeyValue:
    def __init__(self, key, value, level=0, last_op_type=OpType.NONE):
        self.logger = logging.getLogger(__class__.__name__)
        self.__key = key
        self.__value = value
        self.__level = level
        self.__last_op_type = last_op_type

    def key(self):
        return self.__key

    def value(self):
        return self.__value

    def type(self):
        return type(self.__value)

    def __str__(self):
        if self.__level == 0:
            return f"{self.__key}({self.__value})"
        else:
            return f"{self.__key}"

    def __repr__(self):
        if self.__level == 0:
            return f"{self.__key}({self.__value})"
        else:
            return f"{self.__key}"

    def __eq__(self, other):
        if type(other) is KeyValue:
            # return self.__value == other.__value and self.__key == other.__key and type(self.__value) == type(other.__value)
            return self.__value == other.__value
        else:
            return self.__value == other

    def __ne__(self, other):
        if type(other) is KeyValue:
            return self.__value != other.__value
        else:
            return self.__value != other

    def __lt__(self, other):
        if type(other) is KeyValue:
            return self.__value < other.__value
        else:
            return self.__value < other

    def __le__(self, other):
        if type(other) is KeyValue:
            return self.__value <= other.__value
        else:
            return self.__value <= other

    def __gt__(self, other):
        if type(other) is KeyValue:
            return self.__value > other.__value
        else:
            return self.__value > other

    def __ge__(self, other):
        if type(other) is KeyValue:
            return self.__value >= other.__value
        else:
            return self.__value >= other

    def __dash_op__(self, lhs, rhs, op, op_sign, op_type):
        lhs_last_op_type = lhs.__last_op_type if type(lhs) is KeyValue else OpType.NONE
        rhs_last_op_type = rhs.__last_op_type if type(rhs) is KeyValue else OpType.NONE

        lhss = (
            f"({lhs})"
            if lhs_last_op_type == OpType.DASH and op_type == OpType.DOT
            else f"{lhs}"
        )
        rhss = (
            f"({rhs})"
            if rhs_last_op_type == OpType.DASH and op_type == OpType.DOT
            else f"{rhs}"
        )

        k = f"{lhss} {op_sign} {rhss}"

        if lhs is None or rhs is None:
            return KeyValue(k, None, self.__level + 1)

        if type(lhs) is KeyValue and lhs.__value is None:
            return KeyValue(k, None, self.__level + 1)

        if type(rhs) is KeyValue and rhs.__value is None:
            return KeyValue(k, None, self.__level + 1)

        v1 = lhs.__value if type(lhs) is KeyValue else lhs
        v2 = rhs.__value if type(rhs) is KeyValue else rhs

        return KeyValue(k, op(v1, v2), self.__level + 1, op_type)

    def __add__(self, other):
        return self.__dash_op__(self, other, lambda x, y: x + y, "+", OpType.DASH)

    def __radd__(self, other):
        return self.__dash_op__(other, self, lambda x, y: x + y, "+", OpType.DASH)

    def __sub__(self, other):
        return self.__dash_op__(self, other, lambda x, y: x - y, "-", OpType.DASH)

    def __rsub__(self, other):
        return self.__dash_op__(other, self, lambda x, y: x - y, "-", OpType.DASH)

    def __mul__(self, other):
        return self.__dash_op__(self, other, lambda x, y: x * y, "*", OpType.DOT)

    def __rmul__(self, other):
        return self.__dash_op__(other, self, lambda x, y: x * y, "*", OpType.DOT)

    def __truediv__(self, other):
        return self.__dash_op__(self, other, lambda x, y: x / y, "/", OpType.DOT)

    def __rtruediv__(self, other):
        return self.__dash_op__(other, self, lambda x, y: x / y, "/", OpType.DOT)

    def __mod__(self, other):
        k = f"{self} % {other}" if self.__level == 0 else f"({self}) % {other}"
        if not (
            isinstance(self.__value, (int, float)) and isinstance(other, (int, float))
        ):
            return KeyValue(k, None, self.__level + 1)
        v = (
            None
            if self.__value is None
            else (
                self.__value % other.__value
                if type(other) is KeyValue
                else self.__value % other
            )
        )
        return KeyValue(k, v, self.__level + 1)

    def __neg__(self):
        k = f"-({self})" if self.__level == 0 else f"-({self})"
        v = None if self.__value is None else -self.__value
        return KeyValue(k, v, self.__level + 1)

    def __rcontains__(self, other):
        k = f"{self} in {other}"
        v = (
            self.__value in other.__value
            if type(other) is KeyValue
            else self.__value in other
        )
        return KeyValue(k, v, self.__level + 1)

    def __int__(self):
        return int(self.__value)

    def abs(self):
        k = f"|{self}|"
        v = None if self.__value is None else abs(self.__value)
        return KeyValue(k, v, self.__level + 1)

    def to_int(self):
        k = f"int({self})"
        v = None if self.__value is None else int(self.__value)
        return KeyValue(k, v, self.__level + 1)
