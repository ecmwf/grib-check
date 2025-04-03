import logging

class KeyValue:
    def __init__(self, key, value, level=0):
        self.logger = logging.getLogger(__class__.__name__)
        self.__key = key
        self.__value = value
        self.__level = level

    def key(self):
        return self.__key

    def value(self):
        return self.__value 

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

    def __add__(self, other):
        k = f"{self} + {other}"
        v = self.__value + other.__value if type(other) is KeyValue else self.__value + other
        return KeyValue(k, v, self.__level + 1)

    def __radd__(self, other):
        k = f"{other} + {self}"
        v = self.__value + other.__value if type(other) is KeyValue else self.__value + other
        return KeyValue(k, v, self.__level + 1)

    def __sub__(self, other):
        k = f"{self} - {other}"
        v = self.__value - other.__value if type(other) is KeyValue else self.__value - other
        return KeyValue(k, v, self.__level + 1)

    def __mul__(self, other):
        k = f"{self} * {other}"
        v = self.__value * other.__value if type(other) is KeyValue else self.__value * other
        return KeyValue(k, v, self.__level + 1)

    def __truediv__(self, other):
        k = f"{self} / {other}"
        v = self.__value / other.__value if type(other) is KeyValue else self.__value / other
        return KeyValue(k, v, self.__level + 1)

    def __mod__(self, other):
        k = f"{self} % {other}"
        v = self.__value % other.__value if type(other) is KeyValue else self.__value % other
        return KeyValue(k, v, self.__level + 1)

    def __neg__(self):
        k = f"-{self}"
        v = -self.__value
        return KeyValue(k, v, self.__level + 1)

    def __rcontains__(self, other):
        k = f"{self} in {other}"
        v = self.__value in other.__value if type(other) is KeyValue else self.__value in other
        return KeyValue(k, v, self.__level + 1)

    def __int__(self):
        return int(self.__value)

    def abs(self):
        k = f"|{self}|"
        v = abs(self.__value)
        return KeyValue(k, v, self.__level + 1)

    def to_int(self):
        k = f"int({self})"
        v = int(self.__value)
        return KeyValue(k, v, self.__level + 1)
