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

from grib_check.CheckEngine import CheckEngine
from grib_check.Assert import Eq, IsIn, IsMultipleOf, Missing
from grib_check.Report import Report

from .GeneralChecks import GeneralChecks

class era6(GeneralChecks):
    def __init__(self, lookup_table, check_limits=False, check_validity=True):
        super().__init__(lookup_table, check_limits=check_limits, check_validity=check_validity)
        self.logger = logging.getLogger(__class__.__name__)
        self.register_checks(
            {
                "pressure_level": self._pressure_level,
                "basic_checks_era6": self._basic_checks_era6,
            }
        )

    def _basic_checks_era6(self, message, p) -> Report:
        report = Report("ERA6 Basic Checks")
        # re-analysis regarding code table 1.3
        report.add(IsIn(message["productionStatusOfProcessedData"], [3]))
        # IFS cycle cy49r2
        report.add(IsIn(message["backgroundProcess"], [255]))
        report.add(IsIn(message["generatingProcessIdentifier"], [159]))
        report.add(Missing(message, "hoursAfterDataCutoff"))
        report.add(Missing(message, "minutesAfterDataCutoff"))
        report.add(
            IsIn(message["typeOfProcessedData"], [0, 1])
        )  # 0 = analysis , 1 = forecast
        if message["typeOfProcessedData"] == 0:
            report.add(Eq(message["step"], 0))
        else:
            report.add(
                IsIn(message["step"], [1, 2, 4, 5]) | IsMultipleOf(message["step"], 1)
            )
        return report

    def _pressure_level(self, message, p) -> Report:
        report = Report("ERA6 Pressure Level")
        levels = [
            1000,
            975,
            950,
            925,
            900,
            875,
            850,
            825,
            800,
            750,
            700,
            600,
            500,
            400,
            300,
            250,
            200,
            150,
            100,
            70,
            50,
            30,
            20,
            10,
            7,
            5,
            3,
            2,
            1,
        ]
        report.add(IsIn(message["level"], levels, "invalid pressure level"))
        return report

    def _height_level(self, message, p) -> Report:
        report = Report("ERA6 Height Level")
        levels = [15, 30, 50, 75, 100, 150, 200, 250, 300, 400, 500]
        report.add(IsIn(message["level"], levels, "invalid height level"))
        return report
