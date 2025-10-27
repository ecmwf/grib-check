#!/usr/bin/env python3

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
import logging
import multiprocessing
import os
import signal
import sys

from .checker.Crra import Crra
from .checker.Lam import Lam
from .checker.S2S import S2S
from .checker.S2SRefcst import S2SRefcst
from .checker.Tigge import Tigge
from .checker.Uerra import Uerra
from .checker.Wpmip import Wpmip
from .FileScanner import FileScanner
from .Grib import Grib
from .LookupTable import SimpleLookupTable
from .Message import Message
from .Report import Report
from .ValueFormat import formatter

signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))  # Disable traceback on Ctrl+C


def worker(filename, message_buffer, pos, checker, args):
    message = Message(message_buffer=message_buffer, position=pos)

    sub_report = Report(f"field {message.position()}")
    sub_report.add(checker.validate(message))

    report = Report(f"{filename}")
    report.add(sub_report)

    print(
        report.as_string(
            max_level=args.report_depth,
            color=args.color,
            failed_only=args.failed_only,
            output_type=args.output_type,
        ),
        end="",
        flush=True,
    )

    # return report
    return None


class GribCheck:
    def __init__(self, args):
        self.args = args
        self.logger = logging.getLogger(__class__.__name__)

    def run(self):
        """
        lam: local area model
        s2s: subseasonal to subseasonal
        s2s_refcst: subseasonal to subseasonal reforecast
        uerra: uncertainty estimation reanalysis
        crra: climate reanalysis
        """
        script_path = os.path.dirname(os.path.realpath(__file__))
        tigge_params = (
            self.args.parameters
            if self.args.parameters is not None
            else f"{script_path}/checker/TiggeParameters.jsonnet"
        )
        wpmip_params = (
            self.args.parameters
            if self.args.parameters is not None
            else f"{script_path}/checker/WpmipParameters.jsonnet"
        )
        crra_params = (
            self.args.parameters
            if self.args.parameters is not None
            else f"{script_path}/checker/CrraParameters.jsonnet"
        )

        if self.args.convention == "tigge":
            checker = Tigge(SimpleLookupTable(tigge_params), check_limits=self.args.check_limits, check_validity=self.args.validity_check)
        elif self.args.convention == "wpmip":
            checker = Wpmip(SimpleLookupTable(wpmip_params), check_limits=self.args.check_limits, check_validity=self.args.validity_check)
        elif self.args.convention == "s2s":
            checker = S2S(SimpleLookupTable(tigge_params), check_limits=self.args.check_limits, check_validity=self.args.validity_check)
        elif self.args.convention == "s2s_refcst":
            checker = S2SRefcst(SimpleLookupTable(tigge_params), check_limits=self.args.check_limits, check_validity=self.args.validity_check)
        elif self.args.convention == "uerra":
            checker = Uerra(SimpleLookupTable(tigge_params, ignore_keys=["model"]),
                            check_limits=self.args.check_limits, check_validity=self.args.validity_check,)
        elif self.args.convention == "crra":
            checker = Crra(
                SimpleLookupTable(crra_params, ignore_keys=["model"]),
                check_limits=self.args.check_limits, check_validity=self.args.validity_check,
            )
        elif self.args.convention == "lam":
            checker = Lam(SimpleLookupTable(tigge_params), check_limits=self.args.check_limits, check_validity=self.args.validity_check)
        else:
            raise ValueError("Unknown data type")

        if self.args.num_jobs > 1:
            results = []
            with multiprocessing.Pool(processes=self.args.num_jobs) as pool:
                for filename in FileScanner(self.args.path):
                    grib = Grib(filename)
                    for pos, message in enumerate(grib):
                        results.append(
                            pool.apply_async(
                                worker,
                                (
                                    filename,
                                    message.get_buffer(),
                                    pos + 1,
                                    checker,
                                    self.args,
                                ),
                            )
                        )
                for result in results:
                    result.wait()
        else:
            for filename in FileScanner(self.args.path):
                grib = Grib(filename)
                for pos, message in enumerate(grib):
                    worker(filename, message.get_buffer(), pos + 1, checker, self.args)


def main():
    parser = argparse.ArgumentParser(description="""GribCheck is a tool that validates project-specific conventions of GRIB files.
It performs a set of checks on GRIB messages to ensure they comply with the project's internal standards and expectations.
    """)

    parser.add_argument("path", nargs="+", help="path(s) to a GRIB file(s) or directory(s)", type=str)
    parser.add_argument("-L", "--check-limits", help="check value ranges (min/max limits)", action="store_true")
    parser.add_argument(
        "-C",
        "--convention",
        help="data convention. The following conventions are experimental: wpmip.",
        choices=[
            "tigge",
            "s2s",
            "s2s_refcst",
            "uerra",
            "crra",
            "lam",
            "wpmip",
        ],
        required=True,
        type=str,
    )
    parser.add_argument("-l", "--report-depth", help="report depth", type=int, default=10)
    parser.add_argument("-d", "--debug", help="debug mode", action="store_true")
    parser.add_argument("-p", "--parameters", help="path to parameters file", default=None)
    parser.add_argument("-c", "--color", help="use color in output", action="store_true")
    parser.add_argument("-j", "--num-jobs", help="number of jobs", type=int, default=1)
    parser.add_argument("-f", "--failed-only", help="show only failed checks", action="store_true")
    parser.add_argument("-o", "--output-type", help="output format", choices=["short", "tree"], default="tree")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.0.4")
    parser.add_argument("-t", "--show-type", help="show value type", action="store_true")
    parser.add_argument(
        "--validity-check",
        help='check validity of messages using the "isMessageValid" key provided by ecCodes. (experimental)',
        action="store_true",
    )
    args = parser.parse_args()

    if args.debug:
        print("Debug mode")
        logging.basicConfig(
            filename="grib_check.log",
            format="%(asctime)s %(name)s %(levelname)-8s %(process)d %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.DEBUG,
        )

    logger = logging.getLogger(__name__)
    logger.info("Started")
    if args.show_type:
        formatter.set_format("{}:{}", show_type=True)

    grib_check = GribCheck(args)
    return grib_check.run()


if __name__ == "__main__":
    ret = main()
    # sys.exit(0 if ret is None else ret)
