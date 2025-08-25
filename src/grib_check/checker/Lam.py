#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.
#

from grib_check.Assert import Eq, Fail, IsIn, IsMultipleOf, Le, Ne
from grib_check.Report import Report

from .Wmo import Wmo


class Lam(Wmo):
    def __init__(self, lookup_table, valueflg=False):
        super().__init__(lookup_table, valueflg=valueflg)

    def _basic_checks(self, message, p) -> Report:
        report = Report("Lam Basic Checks")
        report.add(IsIn(message["hour"], [0, 3, 6, 9, 12, 15, 18, 21]))
        report.add(IsIn(message["productionStatusOfProcessedData"], [4, 5]))
        report.add(Le(message["endStep"], 30 * 24))
        report.add(IsMultipleOf(message["step"], 3))

        report.add(self._check_date(message, p))

        return super()._basic_checks(message, p).add(report)

    # not registered in the lookup table
    def _statistical_process(self, message, p) -> Report:
        report = Report("Lam Statistical Process")

        topd = message.get("typeOfProcessedData", int)

        if topd in [0, 1, 2]:  # Analysis, Forecast, Analysis and forecast products
            pass
        elif topd in [3, 4]:  # Control forecast products
            report.add(Eq(message["productDefinitionTemplateNumber"], 11))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return report

        if message["indicatorOfUnitOfTimeRange"] == 10:  # three hours
            # Three hourly is OK
            pass
        else:
            report.add(Eq(message["indicatorOfUnitOfTimeRange"], 1))
            report.add(IsMultipleOf(message["forecastTime"], 3))

        report.add(Eq(message["timeIncrementBetweenSuccessiveFields"], 0))
        report.add(IsMultipleOf(message["endStep"], 3))  # Every three hours

        return super()._statistical_process(message, p).add(report)

    def _from_start(self, message, p) -> Report:
        report = Report("Lam From Start")
        if message["endStep"] != 0:
            report.add(self._check_range(message, p))

        return super()._from_start(message, p).add(report)

    def _point_in_time(self, message, p) -> Report:
        report = Report("Lam Point In Time")
        topd = message.get("typeOfProcessedData", int)
        if topd in [0, 1]:  # Analysis, Forecast
            if message["productDefinitionTemplateNumber"] == 1:
                report.add(Ne(message["numberOfForecastsInEnsemble"], 0))
                report.add(
                    Le(
                        message["perturbationNumber"],
                        message["numberOfForecastsInEnsemble"],
                    )
                )
        elif topd == 2:  # Analysis and forecast products
            pass
        elif topd == 3:  # Control forecast products
            report.add(Eq(message["productDefinitionTemplateNumber"], 1))
        elif topd == 4:  # Perturbed forecast products
            report.add(Eq(message["productDefinitionTemplateNumber"], 1))
            report.add(
                Le(
                    message["perturbationNumber"],
                    message["numberOfForecastsInEnsemble"],
                )
            )
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))

        if message["indicatorOfUnitOfTimeRange"] == 10:
            # Three hourly is OK
            pass
        else:
            report.add(Eq(message["indicatorOfUnitOfTimeRange"], 1))
            report.add(IsMultipleOf(message["forecastTime"], 3))

        return super()._point_in_time(message, p).add(report)
