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
import logging
from Report import Report
import concurrent.futures
import multiprocessing
from Message import Message


def worker(filename, message_buffer, pos, checker):
    message = Message(message_buffer=message_buffer, position=pos)

    sub_report = Report(f"field {message.position()}")
    sub_report.add(checker.validate(message))

    report = Report(f"{filename}")
    report.add(sub_report)

    return report


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
            checker = Tigge(param_file=self.args.parameters, valueflg=self.args.valueflg)
        elif self.args.grib_type == "s2s":
            checker = S2S(param_file=self.args.parameters, valueflg=self.args.valueflg)
        elif self.args.grib_type == "s2s_refcst":
            checker = S2SRefcst(param_file=self.args.parameters, valueflg=self.args.valueflg)
        elif self.args.grib_type == "uerra":
            checker = Uerra(param_file=self.args.parameters, valueflg=self.args.valueflg)
        elif self.args.grib_type == "crra":
            checker = Crra(param_file=self.args.parameters, valueflg=self.args.valueflg)
        elif self.args.grib_type == "lam":
            checker = Lam(param_file=self.args.parameters, valueflg=self.args.valueflg)
        else:
            raise ValueError("Unknown data type")

        results = []
        with multiprocessing.Pool(processes=self.args.num_threads) as pool:
            for filename in FileScanner(self.args.path):
                grib = Grib(filename)
                for pos, message in enumerate(grib):
                    results.append(pool.apply_async(worker, (filename, message.get_buffer(), pos, checker)))

            for result in results:
                print(result.get().as_string(max_level=self.args.report_verbosity, color=self.args.color, failed_only=self.args.failed_only, format=self.args.format), end="")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("-w", "--warnflg", help="warnings are treated as errors", action="store_true")
    # parser.add_argument("-z", "--zeroflg", help="return 0 to calling shell", action="store_true")
    parser.add_argument("-a", "--valueflg", help="check value ranges", action="store_true")
    parser.add_argument("path", nargs="+", help="path to a GRIB file or directory", type=str)
    parser.add_argument("-t", "--grib_type", help="type of data to check", choices=["tigge", "s2s", "s2s_refcst", "uerra", "crra", "lam", "wmo"], default="tigge")
    parser.add_argument("-v", "--verbosity", help="increase log verbosity", default=0)
    parser.add_argument("-l", "--report_verbosity", help="report depth", type=int, default=10)
    parser.add_argument("-d", "--debug", help="debug mode", action="store_true")
    parser.add_argument("-p", "--parameters", help="path to parameters file", default=None)
    parser.add_argument("-c", "--color", help="use color in output", action="store_true")
    parser.add_argument("-j", "--num_threads", help="number of threads", type=int, default=4)
    parser.add_argument("-b", "--failed_only", help="show only failed checks", action="store_true")
    parser.add_argument("-f", "--format", help="output format", choices=["short", "tree"], default="tree")
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
    grib_check.run()
    # sys.exit(grib_check.run())

