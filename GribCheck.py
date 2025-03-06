#!/usr/bin/env python3

import sys
import argparse
from FileScanner import FileScanner
from checker.WmoChecker import WmoChecker
from checker.Tigge import Tigge
from checker.Uerra import Uerra
from checker.S2S import S2S
from checker.S2SRefcst import S2SRefcst
from checker.Crra import Crra
from checker.Lam import Lam
from Grib import Grib
from Report import Report
from Assert import Pass, Fail
from eccodes import codes_write
import logging


class GribCheck:
    def __init__(self, args):
        self.args = args
        self.logger = logging.getLogger(__class__.__name__)

    def run(self):
        '''
        lam: local area model
        s2s: subseasonal to subseasonal
        s2s_refcst: subseasonal to subseasonal reforecast
        uerra: uncertainty estimation reanalysis
        crra: climate reanalysis
        '''

        if self.args.grib_type == "wmo":
            checker = WmoChecker(param_file=self.args.parameters)
        elif self.args.grib_type == "tigge":
            checker = Tigge(param_file=self.args.parameters)
        elif self.args.grib_type == "s2s":
            checker = S2S(param_file=self.args.parameters)
        elif self.args.grib_type == "s2s_refcst":
            checker = S2SRefcst(param_file=self.args.parameters)
        elif self.args.grib_type == "uerra":
            checker = Uerra(param_file=self.args.parameters)
        elif self.args.grib_type == "crra":
            checker = Crra(param_file=self.args.parameters)
        elif self.args.grib_type == "lam":
            checker = Lam(param_file=self.args.parameters)
        else:
            raise ValueError("Unknown data type")

        fgood = None
        if self.args.good:
            self.logger.debug(f"Good messages will be written to {self.args.good}")
            fgood = open(self.args.good, "wb")
            if not fgood:
                print("Couldn't open %s" % self.args.good)
                sys.exit(1)

        fbad = None
        if self.args.bad:
            self.logger.debug(f"Bad messages will be written to {self.args.bad}")
            fbad = open(self.args.bad, "wb")
            if not fbad:
                print("Couldn't open %s" % self.args.bad)
                sys.exit(1)

        for filename in FileScanner(self.args.path):
            # print(f"Checking {filename}") 
            count = 0
            file_report = Report()
            file_report.add(Pass(f"File: {filename}"))
            for message in Grib(filename):
                # print(f"Checking message[{message.position()}]")
                self.logger.debug(f"Check message[{message.position()}]")
                message_report  = checker.validate(message)
                result, _ = message_report.summary()
                count += 1
                if result:
                    self.logger.debug(f"Message[{message.position()}] is valid")
                    if fgood:
                        codes_write(message.handle, self.args.good)
                else:
                    self.logger.debug(f"Message[{message.position()}] is invalid")
                    if fbad:
                        codes_write(message.handle, self.args.bad)
                    
                file_report.add(message_report)

            status, summary = file_report.summary(max_level=int(self.args.report_verbosity), color=self.args.color)
            # status, summary = file_report.summary()
            print(summary)

            if count == 0:
                print("%s does not contain any GRIBs" % filename)
                # self.__error += 1

        if fgood:
            fgood.close()

        if fbad:
            fbad.close()

        err = 0
        if checker.get_error_counter() != 0:
            err = 1
        if checker.get_warning_counter() and self.args.warnflg:
            err = 1

        print(f"Zeroflg: {self.args.zeroflg}")
        return 0 if self.args.zeroflg else err


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--warnflg", help="warnings are treated as errors", action="store_true")
    parser.add_argument("-z", "--zeroflg", help="return 0 to calling shell", action="store_true")
    parser.add_argument("-a", "--valueflg", help="check value ranges", action="store_true")
    parser.add_argument("-g", "--good", help="write good gribs", default=None)
    parser.add_argument("-b", "--bad", help="write bad gribs", default=None)
    parser.add_argument("path", nargs="+", help="path to a GRIB file or directory", type=str)
    parser.add_argument("-t", "--grib_type", help="type of data to check", choices=["tigge", "s2s", "s2s_refcst", "uerra", "crra", "lam", "wmo"], default="tigge")
    parser.add_argument("-v", "--verbosity", help="increase output verbosity", default=0)
    parser.add_argument("-r", "--report_verbosity", help="increase output verbosity", type=int, default=10)
    parser.add_argument("-d", "--debug", help="debug mode", action="store_true")
    parser.add_argument("-p", "--parameters", help="path to parameters file", default=None)
    parser.add_argument("-c", "--color", help="use color in output", action="store_true")
    args = parser.parse_args()

    if args.debug:
        print("Debug mode")
        logging.basicConfig(
            filename='grib_check.log',
            format="%(asctime)s %(name)s %(levelname)-8s %(thread)d %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.DEBUG,
        )

    logger = logging.getLogger(__name__)
    logger.info('Started')

    grib_check = GribCheck(args)
    sys.exit(grib_check.run())

