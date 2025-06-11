#!/usr/bin/env python3

import signal
import sys

signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))  # Disable traceback on Ctrl+C

import argparse
from FileScanner import FileScanner
from checker.Tigge import Tigge
from checker.Uerra import Uerra
from checker.S2S import S2S
from checker.S2SRefcst import S2SRefcst
from checker.Crra import Crra
from checker.Lam import Lam
from checker.DestinE import DestinE
from checker.Wmo import Wmo
from Grib import Grib
import logging
from Report import Report
import concurrent.futures
import multiprocessing
from Message import Message
from LookupTable import SimpleLookupTable
import os


def worker(filename, message_buffer, pos, checker, args):
    message = Message(message_buffer=message_buffer, position=pos)

    sub_report = Report(f"field {message.position()}")
    sub_report.add(checker.validate(message))

    report = Report(f"{filename}")
    report.add(sub_report)

    print(report.as_string(max_level=args.report_verbosity, color=args.color, failed_only=args.failed_only, format=args.format), end="", flush=True)

    # return report
    return None


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
        script_path = os.path.dirname(os.path.realpath(__file__))
        tigge_params = self.args.parameters if self.args.parameters is not None else f"{script_path}/checker/TiggeParameters.json"
        destine_params = self.args.parameters if self.args.parameters is not None else f"{script_path}/checker/DestineParameters.json"
        wmo_params = self.args.parameters if self.args.parameters is not None else f"{script_path}/checker/WmoParameters.json"

        if self.args.grib_type == "wmo":
            checker = Wmo(SimpleLookupTable(wmo_params), valueflg=self.args.valueflg)
        elif self.args.grib_type == "tigge":
            checker = Tigge(SimpleLookupTable(tigge_params), valueflg=self.args.valueflg)
        elif self.args.grib_type == "s2s":
            checker = S2S(SimpleLookupTable(tigge_params), valueflg=self.args.valueflg)
        elif self.args.grib_type == "s2s_refcst":
            checker = S2SRefcst(SimpleLookupTable(tigge_params), valueflg=self.args.valueflg)
        elif self.args.grib_type == "uerra":
            checker = Uerra(SimpleLookupTable(tigge_params, ignore_keys=["model"]), valueflg=self.args.valueflg)
        elif self.args.grib_type == "crra":
            checker = Crra(SimpleLookupTable(tigge_params, ignore_keys=["model"]), valueflg=self.args.valueflg)
        elif self.args.grib_type == "lam":
            checker = Lam(SimpleLookupTable(tigge_params), valueflg=self.args.valueflg)
        elif self.args.grib_type == "destine":
            checker = DestinE(SimpleLookupTable(destine_params), valueflg=self.args.valueflg)
        else:
            raise ValueError("Unknown data type")


        if self.args.num_threads > 1:
            results = []
            with multiprocessing.Pool(processes=self.args.num_threads) as pool:
                for filename in FileScanner(self.args.path):
                    grib = Grib(filename)
                    for pos, message in enumerate(grib):
                        results.append(pool.apply_async(worker, (filename, message.get_buffer(), pos + 1, checker, self.args)))
                for result in results:
                    result.wait()
        else:
            for filename in FileScanner(self.args.path):
                grib = Grib(filename)
                for pos, message in enumerate(grib):
                        worker(filename, message.get_buffer(), pos + 1, checker, self.args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("-w", "--warnflg", help="warnings are treated as errors", action="store_true")
    # parser.add_argument("-z", "--zeroflg", help="return 0 to calling shell", action="store_true")
    parser.add_argument("-a", "--valueflg", help="check value ranges", action="store_true")
    parser.add_argument("path", nargs="+", help="path to a GRIB file or directory", type=str)
    parser.add_argument("-t", "--grib_type", help="type of data to check", choices=["tigge", "s2s", "s2s_refcst", "uerra", "crra", "lam", "wmo", "destine"], default="wmo")
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

