#!/usr/bin/env python3

from eccodes import *
from pathlib import Path
import math
import argparse
from shared import *
import sys
import os

class Context:
    def __init__(self):
        self.filename = ''
        self.error = 0
        self.field = 0
        self.param = 'unknown'
        self.list_mode = False
        self.compare_mode = False


def get(h, what) -> int:
    val = -1
    try:
        val = codes_get_long(h, what)
    except Exception as e:
        print("%s, field %d [%s]: cannot get %s: %s" % (ctx.filename, ctx.field, ctx.param, what, str(e)))
        ctx.error += 1
    return val


def sget(h, what) -> str:
    val = None
    try:
        val = codes_get_string(h, what)
    except Exception as e:
        print("%s, field %d [%s]: cannot get %s: %s" % (ctx.filename, ctx.field, ctx.param, what, str(e)))
        ctx.error += 1
    return val


def verify(h, full, base):
    level = 0
    number = 0

    marstype = sget(h, "type")
    levtype = sget(h, "levtype")

    if marstype == "fc":
        number = get(h,"number")

    if levtype == "sfc":
        levtype = "sl"
    else:
        level = get(h, "level")

    wmo_name = "z_tigge_c_%s_%08ld%04ld00_%s_%s_%s_%s_%04ld_%03ld_%04ld_%s.grib" % (
            sget(h, "origin"),
            0 if ctx.compare_mode else get(h, "date"),
            0 if ctx.compare_mode else get(h, "time"),
            sget(h,"model"),
            "xxxx" if ctx.compare_mode else sget(h, "expver"),
            marstype,
            levtype,
            get(h, "step"),
            number,
            level,
            sget(h,"tigge_short_name"))

    if ctx.list_mode:
        print("%s" % wmo_name)
    elif base != wmo_name:
        print("WRONG FILE NAME:   %s\nCORRECT FILE NAME: %s" % (base, wmo_name))
        ctx.error += 1


def validate(path):
    try:
        f = open(path,"rb")
    except Exception as e:
        print("%s: %s" % (path, str(e)))
        ctx.error += 1
        return

    err = 0
    count = 0

    ctx.filename  = path
    ctx.field = 0

    while True:
        h = None
        try:
            h = codes_grib_new_from_file(f)
        except Exception as e:
            err += 1
            last_error_message = str(e)
        if h == None:
              break
        ctx.field += 1
        verify(h, path, os.path.basename(path))
        codes_release(h)
        count += 1
        ctx.param = "unknown"

    f.close()

    if err != 0:
        print("%s: grib_handle_new_from_file: %s" % (path, last_error_message))
        ctx.error += 1
        return

    if count == 0:
        print("%s does not contain any GRIBs" % path)
        ctx.error += 1
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list-mode', help='Enable list mode', action='store_true')
    parser.add_argument('-c', '--compare-mode', help='Enable compare mode', action='store_true')
    parser.add_argument('file', nargs='+', help='Grib files', type=str)
    args = parser.parse_args()

    ctx = Context()
    ctx.list_mode = args.list_mode
    ctx.compare_mode = args.compare_mode

    for file in args.file:
        scan(file, validate)

    sys.exit(0 if ctx.error == 0 else 1)
