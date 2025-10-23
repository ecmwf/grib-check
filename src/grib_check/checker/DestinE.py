#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from grib_check.Assert import IsIn, IsMultipleOf, Le
from grib_check.Report import Report

from .GeneralChecks import GeneralChecks


class DestinE(GeneralChecks):
    def __init__(self, lookup_table, valueflg=False):
        super().__init__(lookup_table, valueflg=valueflg)
        self.register_checks({"destine_limits": self._destine_limits})

    # Reuse / override checks
    def _point_in_time(self, message, p) -> Report:
        report = Report("Point In Time (DestinE)")
        report.add(IsMultipleOf(message["step"], 3))
        return super()._point_in_time(message, p).add(report)

    # Create new checks
    def _destine_limits(self, message, p) -> Report:
        report = Report("DestinE Limits")
        report.add(Le(message["step"], 30))
        report.add(IsIn(message["forecastTime"], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        report.add(IsIn(message["indicatorOfUnitOfTimeRange"], [0, 1]))
        report.add(IsIn(message["timeIncrementBetweenSuccessiveFields"], [0, 1]))
        return report
