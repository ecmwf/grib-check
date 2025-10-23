#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from grib_check.Assert import Eq, Fail, IsIn, IsMultipleOf, Le, Ne, Pass
from grib_check.KeyValue import KeyValue
from grib_check.Report import Report

from .GeneralChecks import GeneralChecks


class Lam(GeneralChecks):
    def __init__(self, lookup_table, check_limits=False, check_validity=True):
        super().__init__(lookup_table, check_limits=check_limits, check_validity=check_validity)

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
        endStep = message["endStep"]
        if endStep == 0:
            min_value, max_value = message.minmax()
            if min_value == 0 and max_value == 0:
                report.add(Pass(f"min and max are both {KeyValue(None, 0)} for {endStep}"))
            else:
                report.add(Fail(f"min and max should both be {KeyValue(None, 0)} for {endStep} but are {KeyValue(None, min_value)} and {KeyValue(None, max_value)}"))

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
