#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import argparse
import os
import sys

from eccodes import (
    codes_get_long,
    codes_get_string,
    codes_grib_new_from_file,
    codes_release,
)

from grib_check.FileScanner import FileScanner


class TiggeName:
    def __init__(self, list_mode=False, compare_mode=False):
        self.filename = ""
        self.error = 0
        self.field = 0
        self.param = "unknown"

        self.list_mode = list_mode
        self.compare_mode = compare_mode

    def __get(self, h, what) -> int:
        val = -1
        try:
            val = codes_get_long(h, what)
        except Exception as e:
            print(
                "%s, field %d [%s]: cannot get %s: %s"
                % (self.filename, self.field, self.param, what, str(e))
            )
            self.error += 1
        return val

    def __sget(self, h, what) -> str:
        val = None
        try:
            val = codes_get_string(h, what)
        except Exception as e:
            print(
                "%s, field %d [%s]: cannot get %s: %s"
                % (self.filename, self.field, self.param, what, str(e))
            )
            self.error += 1
        return val

    def __verify(self, h, full, base):
        level = 0
        number = 0

        marstype = self.__sget(h, "type")
        levtype = self.__sget(h, "levtype")

        if marstype == "fc":
            number = self.__get(h, "number")

        if levtype == "sfc":
            levtype = "sl"
        else:
            level = self.__get(h, "level")

        wmo_name = "z_tigge_c_%s_%08ld%04ld00_%s_%s_%s_%s_%04ld_%03ld_%04ld_%s.grib" % (
            self.__sget(h, "origin"),
            0 if self.compare_mode else self.__get(h, "date"),
            0 if self.compare_mode else self.__get(h, "time"),
            self.__sget(h, "model"),
            "xxxx" if self.compare_mode else self.__sget(h, "expver"),
            marstype,
            levtype,
            self.__get(h, "step"),
            number,
            level,
            self.__sget(h, "tigge_short_name"),
        )

        if self.list_mode:
            print("%s" % wmo_name)
        elif base != wmo_name:
            print("WRONG FILE NAME:   %s\nCORRECT FILE NAME: %s" % (base, wmo_name))
            self.error += 1

    def validate(self, path):
        try:
            f = open(path, "rb")
        except Exception as e:
            print("%s: %s" % (path, str(e)))
            self.error += 1
            return

        err = 0
        count = 0

        self.filename = path
        self.field = 0

        while True:
            h = None
            try:
                h = codes_grib_new_from_file(f)
            except Exception as e:
                err += 1
                last_error_message = str(e)
            if h is None:
                break
            self.field += 1
            self.__verify(h, path, os.path.basename(path))
            codes_release(h)
            count += 1
            self.param = "unknown"

        f.close()

        if err != 0:
            print("%s: grib_handle_new_from_file: %s" % (path, last_error_message))
            self.error += 1
            return

        if count == 0:
            print("%s does not contain any GRIBs" % path)
            self.error += 1
            return

    def get_error_counter(self):
        return self.error


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--list-mode", help="enable list mode", action="store_true"
    )
    parser.add_argument(
        "-c", "--compare-mode", help="enable compare mode", action="store_true"
    )
    parser.add_argument(
        "path", nargs="+", help="path to a GRIB file or directory", type=str
    )
    args = parser.parse_args()

    tigge_name = TiggeName(list_mode=args.list_mode, compare_mode=args.compare_mode)

    for filename in FileScanner(args.path):
        tigge_name.validate(filename)

    sys.exit(0 if tigge_name.get_error_counter() == 0 else 1)


if __name__ == "__main__":
    main()
