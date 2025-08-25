#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import sys

from eccodes import (
    codes_get_gaussian_latitudes,
    codes_grib_new_from_file,
)

from .Assert import Fail
from .Message import Message
from .Report import Report


class Grib:
    def __init__(self, path):
        self.__report = Report(f"File: {path}")
        self.__position = 0
        self.__f = None
        try:
            self.__f = open(path, "rb")
        except Exception as e:
            print(f"{path}, {str(e)}", file=sys.stderr)
            self.__report.add(Fail(f"Could not open file: {path}"))
            return

    def __del__(self):
        if self.__f is not None:
            self.__f.close()

    def __iter__(self):
        self.__position = 0
        return self

    def __next__(self):
        try:
            handle = codes_grib_new_from_file(self.__f)
        except Exception:
            self.__report.add(Fail(f"Could not read message[{self.__position + 1}]"))
            handle = None

        if handle is not None:
            self.__position += 1
            return Message(handle=handle, position=self.__position)
        else:
            raise StopIteration

    def report(self):
        return self.__report


def get_gaussian_latitudes(order):
    return codes_get_gaussian_latitudes(order)
