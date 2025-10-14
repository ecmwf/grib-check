#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

class ValueFormat:
    def __init__(self, fmt: str = "{}", show_type: bool = False):
        self.__type_map = {
            int: "i",
            float: "d",
            str: "s",
        }
        self.__fmt = fmt
        self.__show_type = show_type

    def set_format(self, fmt: str, show_type: bool = True):
        self.__show_type = show_type
        self.__fmt = fmt

    def format(self, value=5):
        if type(value) is list:
            types = set(self.__type_map[type(v)] for v in value)
            if len(types) == 1:
                type_str = types.pop()
            else:
                type_str = "mixed"
        else:
            type_str = self.__type_map.get(type(value), "?")

        if self.__show_type:
            return self.__fmt.format(value, type_str)
        else:
            return self.__fmt.format(value)


# formatter = ValueFormat("{}:{}", show_type=True)
formatter = ValueFormat("{}", show_type=False)
