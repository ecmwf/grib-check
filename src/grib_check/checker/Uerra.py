#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from grib_check.Assert import AssertTrue, Eq, Fail, IsIn, IsMultipleOf, Le
from grib_check.Report import Report

from .GeneralChecks import GeneralChecks


class Uerra(GeneralChecks):
    def __init__(self, lookup_table, check_limits=False, check_validity=True):
        super().__init__(lookup_table, check_limits=check_limits, check_validity=check_validity)

    def _basic_checks_2(self, message, p) -> Report:
        # this class must not inhereted anything
        report = Report("UERRA Basic Checks 2")

        report.add(IsIn(message["productionStatusOfProcessedData"], [8, 9]))
        report.add(Le(message["endStep"], 30))
        report.add(
            IsIn(message["typeOfProcessedData"], [0, 1])
        )  # 0 = analysis, 1 = forecast
        if message["typeOfProcessedData"] == 0:
            report.add(Eq(message["step"], 0))
        else:
            report.add(IsIn(message["step"], [1, 2, 4, 5]) | IsMultipleOf(message["step"], 3))
        report.add(self._check_date(message, p))

        return report

    def _basic_checks(self, message, p) -> Report:
        report = Report("UERRA Basic Checks")
        if message.get("class", str) != 'rr' and message.get("class", str) != 'ci':
            report.add(Eq(message["versionNumberOfGribLocalTables"], 0))

        report.add(Le(message["hour"], 24))
        stream = message.get("stream", str)

        if stream != "moda":
            report.add(IsIn(message["step"], [1, 2, 4, 5]) | IsMultipleOf(message["step"], 3))

        return super()._basic_checks(message, p).add(report)

    def _from_start(self, message, p) -> Report:
        report = Report("Uerra From Start")
        min_value, max_value = message.minmax()
        if message["endStep"] == 0:
            report = Report(f"{__class__.__name__}")
            report.add(
                AssertTrue(
                    bool(min_value == 0) and bool(max_value == 0),
                    "min_value == 0 and max_value == 0",
                )
            )

        return super()._from_start(message, p).add(report)

    def _statistical_process(self, message, p) -> Report:
        report = Report("Uerra Statistical Process")

        topd = message.get("typeOfProcessedData", int)
        if topd in [0, 1]:  # Analysis, Forecast
            report.add(IsIn(message["productDefinitionTemplateNumber"], [8, 11]))
        elif topd == 2:  # Analysis and forecast products
            pass
        elif topd in [3, 4]:  # Control forecast products, Perturbed forecast products
            report.add(Eq(message["productDefinitionTemplateNumber"], 61))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return report

        #  forecastTime for uerra might be all steps decreased by 1 i.e 0,1,2,3,4,5,8,11...29 too many... */
        if message["indicatorOfUnitOfTimeRange"] == 1:
            report.add(Le(message["forecastTime"], 30))

        report.add(Eq(message["timeIncrementBetweenSuccessiveFields"], 0))

        stream = message.get("stream", str)
        if stream != "moda":
            report.add(IsIn(message["endStep"], [1, 2, 4, 5]) | IsMultipleOf(message["endStep"], 3))

        return super()._statistical_process(message, p).add(report)

    def _point_in_time(self, message, p) -> Report:
        report = Report("Uerra Point in Time")

        topd = message.get("typeOfProcessedData", int)
        if topd in [0, 1]:  # Analysis, Forecast
            report.add(IsIn(message["productDefinitionTemplateNumber"], [0, 1]))
        elif topd == 2:  # Analysis and forecast products
            pass
        elif topd == 3:  # Control forecast products
            report.add(Eq(message["productDefinitionTemplateNumber"], 1))
        elif topd == 4:  # Perturbed forecast products
            # Is there always cf in tigge global datasets??
            report.add(
                Le(
                    message["perturbationNumber"],
                    message["numberOfForecastsInEnsemble"] - 1,
                )
            )
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))

        if message["indicatorOfUnitOfTimeRange"] == 1:  # hourly
            report.add(
                IsIn(message["forecastTime"], [1, 2, 4, 5])
                | IsMultipleOf(message["forecastTime"], 3)
            )

        return super()._point_in_time(message, p).add(report)

    def _pressure_level(self, message, p) -> Report:
        report = Report("Uerra Pressure Level")
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
        ]
        report.add(IsIn(message["level"], levels, "valid pressure level"))
        return report

    def _height_level(self, message, p) -> Report:
        report = Report("Uerra Height Level")
        levels = [15, 30, 50, 75, 100, 150, 200, 250, 300, 400, 500]
        report.add(IsIn(message["level"], levels, "valid height level"))
        return report
