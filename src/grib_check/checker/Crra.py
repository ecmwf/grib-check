#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.
#

from grib_check.Assert import Eq, IsIn, IsMultipleOf
from grib_check.Report import Report

from .Uerra import Uerra


class Crra(Uerra):
    def __init__(self, lookup_table, valueflg=False):
        super().__init__(lookup_table, valueflg=valueflg)

    def basic_checks_2(self, message, p) -> Report:
        report = Report("Crra Basic Checks")
        report.add(IsIn(message["productionStatusOfProcessedData"], [10, 11]))
        report.add(IsIn(message["typeOfProcessedData"], [0, 1])) # 0 = analysis , 1 = forecast
        if message["typeOfProcessedData"] == 0:
            report.add(Eq(message["step"], 0))
        else:
            report.add(IsIn(message["step"], [1, 2, 4, 5]) | IsMultipleOf(message["step"], 3))
        return report

    def _pressure_level(self, message, p) -> Report:
        report = Report("Crra Pressure Level")
        levels = [1000, 975, 950, 925, 900, 875, 850, 825, 800, 750, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 10, 7, 5, 3, 2, 1]
        report.add(IsIn(message["level"], levels, 'invalid pressure level'))
        return report
