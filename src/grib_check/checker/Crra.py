#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import datetime
import logging

from grib_check.Assert import (
    Eq,
    Fail,
    IsIn,
    IsMultipleOf,
    Le,
    Ne,
    Pass,
)
from grib_check.KeyValue import KeyValue
from grib_check.Report import Report

from .Uerra import Uerra


class Crra(Uerra):
    def __init__(self, lookup_table, check_limits=False, check_validity=True):
        super().__init__(lookup_table, check_limits=check_limits, check_validity=check_validity)
        self.logger = logging.getLogger(__class__.__name__)
        self.register_checks(
            {
                "pressure_level": self._pressure_level,
            }
        )

    def _basic_checks(self, message, p) -> Report:
        report = Report("CRRA Basic Checks")
        report.add(IsIn(message["productionStatusOfProcessedData"], [10, 11]))
        topd = message.get("typeOfProcessedData", int)
        report.add(IsIn(topd, [0, 1]))

        stream = message.get("stream", str)
        if stream != "moda":
            if topd == 0:
                report.add(Eq(message["step"], 0))
            else:
                report.add(IsIn(message["step"], [1, 2, 4, 5]) | IsMultipleOf(message["step"], 3))

        if message.get("paramId", int) not in [260651, 235072]:
            report.add(Eq(message["versionNumberOfGribLocalTables"], 0))

        return super()._basic_checks(message, p).add(report)

    def _point_in_time(self, message, p) -> Report:
        report = Report("CRRA Point in Time")

        topd = message.get("typeOfProcessedData", int)
        stream = message.get("stream", str)
        if topd in [0, 1]:  # Analysis, Forecast
            if stream == "dame" or stream == "moda":
                report.add(Eq(message["productDefinitionTemplateNumber"], 8))
            else:
                report.add(IsIn(message["productDefinitionTemplateNumber"], [0, 1]))
#       elif topd == 2:  # Analysis and forecast products
#           pass
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

        return report

    def _from_start(self, message, p):
        report = Report("CRRA From Start")
        stream = message.get("stream", str)
        if stream != "moda" and stream != "dame":
            report.add(Eq(message["startStep"], 0))
        report.add(self._statistical_process(message, p))

        endStep = message["endStep"]
        if endStep == 0:
            min_value, max_value = message.minmax()
            if min_value == 0 and max_value == 0:
                report.add(Pass(f"min and max are both {KeyValue(None, 0)} for {endStep}"))
            else:
                report.add(Fail(f"min and max should both be {KeyValue(None, 0)} for {endStep} but are {KeyValue(None, min_value)} and {KeyValue(None, max_value)}"))

        return report

    def _statistical_process(self, message, p) -> Report:
        report = Report("CRRA Statistical Process")

        topd = message.get("typeOfProcessedData", int)
        if topd.value() in [0, 1]:  # Analysis, Forecast
            report.add(Eq(message["productDefinitionTemplateNumber"], 8, f"topd={topd}"))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return report

        report.add(Eq(message["numberOfMissingInStatisticalProcess"], 0))
        # report.add(Eq(message["indicatorOfUnitOfTimeForTheIncrementBetweenTheSuccessiveFieldsUsed"], 255))
        report.add(Eq(message["minuteOfEndOfOverallTimeInterval"], 0))
        report.add(Eq(message["secondOfEndOfOverallTimeInterval"], 0))

        return report

    def _check_validity_datetime(self, message):

        report = Report("CRRA Check Validity Datetime")

        stepType = message.get("stepType", str)
        stream = message.get("stream", str)
        topd = message.get("typeOfProcessedData", int)

        if Ne(stepType, "instant"):  # not instantaneous
            # Check only applies to accumulated, max etc.
            stepRange = message.get("stepRange", str)

            if Eq(stream, "dame") or Eq(stream, "moda"):
                year = message["year"].value()
                month = message["month"].value()
                day = message["day"].value()
                if month == 11:
                    month2 = 1
                    year2 = year + 1
                elif month == 12:
                    month2 = 2
                    year2 = year + 1
                else:
                    month2 = month + 2
                    year2 = year

                same_day = int(str(datetime.date(year, month, day)).replace('-', ''))
                next_day1 = datetime.date(year, month, day) + datetime.timedelta(days=1)
                next_day1 = int(str(next_day1).replace('-', ''))
                next_day2 = datetime.date(year, month, day) + datetime.timedelta(days=2)
                next_day2 = int(str(next_day2).replace('-', ''))
                last_date_month0 = datetime.date(year + int(month / 12), (month % 12) + 1, 1) - datetime.timedelta(days=1)
                last_date_month0 = int(str(last_date_month0).replace('-', ''))
                last_date_month1 = datetime.date(year2, month2, 1) - datetime.timedelta(days=1)
                last_date_month1 = int(str(last_date_month1).replace('-', ''))
                first_date_month1 = datetime.date(year + int(month / 12), (month % 12) + 1, 1)
                first_date_month1 = int(str(first_date_month1).replace('-', ''))
                first_date_month2 = datetime.date(year2, month2, 1)
                first_date_month2 = int(str(first_date_month2).replace('-', ''))

                # numberOfTimeRanges = message["numberOfTimeRanges"]
                lengthOfTimeRanges = [KeyValue("lengthOfTimeRange", v) for v in message.get_long_array("lengthOfTimeRange")]
                typeOfStatisticalProcessings = [KeyValue("typeOfStatisticalProcessing", v) for v in message.get_long_array("typeOfStatisticalProcessing")]

                typeOfTimeIncrements = [KeyValue("typeOfTimeIncrement", v) for v in message.get_long_array("typeOfTimeIncrement")]
                indicatorOfUnitForTimeRanges = [KeyValue("indicatorOfUnitForTimeRange", v) for v in message.get_long_array("indicatorOfUnitForTimeRange")]
                lengthOfTimeRanges = [KeyValue("lengthOfTimeRange", v) for v in message.get_long_array("lengthOfTimeRange")]
                indicatorOfUnitForTimeIncrements = [KeyValue("indicatorOfUnitForTimeIncrement", v) for v in message.get_long_array("indicatorOfUnitForTimeIncrement")]
                timeIncrements = [KeyValue("timeIncrement", v) for v in message.get_long_array("timeIncrement")]

                validityDateBefore = message["validityDate"]
                validityTimeBefore = message["validityTime"]

            # monthly/daily averages are archived under instant paramIds as param-db was not ready for all time-mean proper ones..
            # https://confluence.ecmwf.int/display/DGOV/Support+page+for+DGOV-399+CARRA+daily+and+monthly+GRIB+headers
            if Eq(stream, "dame"):

                report = Report("CRRA Check Validity Datetime - daily means")
                if typeOfStatisticalProcessings == [0]:
                    report = Report("dame - daily_mean_an/fc")
                    dame_validityDate = same_day
                    dame_validityTime = 21
                    if topd == 0:
                        dame_validityDate = same_day
                    elif topd == 1:
                        dame_validityDate = next_day1
                    [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrements[0]), 1))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeRange", indicatorOfUnitForTimeRanges[0]), 1))]
                    [report.add(Eq(KeyValue("lengthOfTimeRange", lengthOfTimeRanges[0]), 21))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeIncrement", indicatorOfUnitForTimeIncrements[0]), 1))]
                    [report.add(Eq(KeyValue("timeIncrement", timeIncrements[0]), 3))]
                elif typeOfStatisticalProcessings == [1, 1]:
                    report = Report("dame - daily_sum_an/fc")
                    dame_validityDate = next_day2
                    dame_validityTime = 0
                    [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrements[0]), 1))]
                    [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrements[1]), 2))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeRange", indicatorOfUnitForTimeRanges[0]), 1))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeRange", indicatorOfUnitForTimeRanges[1]), 1))]
                    [report.add(Eq(KeyValue("lengthOfTimeRange", lengthOfTimeRanges[0]), 24))]
                    [report.add(Eq(KeyValue("lengthOfTimeRange", lengthOfTimeRanges[1]), 12))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeIncrement", indicatorOfUnitForTimeIncrements[0]), 1))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeIncrement", indicatorOfUnitForTimeIncrements[1]), 255))]
                    [report.add(Eq(KeyValue("timeIncrement", timeIncrements[0]), 12))]
                    [report.add(Eq(KeyValue("timeIncrement", timeIncrements[1]), 0))]
                elif typeOfStatisticalProcessings == [2, 2] or typeOfStatisticalProcessings == [3, 3]:
                    report = Report("dame - daily_min/max_an/fc")
                    dame_validityDate = next_day1
                    dame_validityTime = 0
                    [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrements[0]), 1))]
                    [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrements[1]), 2))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeRange", indicatorOfUnitForTimeRanges[0]), 1))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeRange", indicatorOfUnitForTimeRanges[1]), 1))]
                    [report.add(Eq(KeyValue("lengthOfTimeRange", lengthOfTimeRanges[0]), 21))]
                    [report.add(Eq(KeyValue("lengthOfTimeRange", lengthOfTimeRanges[1]), 3))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeIncrement", indicatorOfUnitForTimeIncrements[0]), 1))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeIncrement", indicatorOfUnitForTimeIncrements[1]), 255))]
                    [report.add(Eq(KeyValue("timeIncrement", timeIncrements[0]), 3))]
                    [report.add(Eq(KeyValue("timeIncrement", timeIncrements[1]), 0))]
                else:
                    report.add(Fail(f"Unsupported parameter in stream={stream}"))

                report.add(Eq(validityTimeBefore/100, dame_validityTime))
                report.add(Eq(validityDateBefore, dame_validityDate))

            elif Eq(stream, "moda"):

                report = Report("CRRA Check Validity Datetime - monthly means")

                moda_lotr1 = [669, 693, 717, 741]
                moda_lotr2 = [672, 696, 720, 744]

                if typeOfStatisticalProcessings == [0]:
                    report = Report("moda - monthly_mean_an/fc")
                    if topd == 0:
                        moda_validityDate = last_date_month0
                    elif topd == 1:
                        moda_validityDate = last_date_month1
                    moda_validityTime = 21
                    [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrements[0]), 1))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeRange", indicatorOfUnitForTimeRanges[0]), 1))]
                    [report.add(IsIn(KeyValue("lengthOfTimeRange", lengthOfTimeRanges[0]), moda_lotr1))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeIncrement", indicatorOfUnitForTimeIncrements[0]), 1))]
                    [report.add(Eq(KeyValue("timeIncrement", timeIncrements[0]), 3))]
                elif typeOfStatisticalProcessings == [2, 2] or typeOfStatisticalProcessings == [3, 3]:
                    report = Report("moda - monthly_min/max_an/fc")
                    moda_validityDate = first_date_month1
                    moda_validityTime = 0
                    [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrements[0]), 1))]
                    [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrements[1]), 2))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeRange", indicatorOfUnitForTimeRanges[0]), 1))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeRange", indicatorOfUnitForTimeRanges[1]), 1))]
                    [report.add(IsIn(KeyValue("lengthOfTimeRange", lengthOfTimeRanges[0]), moda_lotr1))]
                    [report.add(Eq(KeyValue("lengthOfTimeRange", lengthOfTimeRanges[1]), 3))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeIncrement", indicatorOfUnitForTimeIncrements[0]), 1))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeIncrement", indicatorOfUnitForTimeIncrements[1]), 255))]
                    [report.add(Eq(KeyValue("timeIncrement", timeIncrements[0]), 3))]
                    [report.add(Eq(KeyValue("timeIncrement", timeIncrements[1]), 0))]
                elif typeOfStatisticalProcessings == [0, 1, 1]:
                    report = Report("moda - monthly_daysum_an/fc")
                    moda_validityDate = first_date_month2
                    moda_validityTime = 0
                    [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrements[0]), 1))]
                    [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrements[1]), 1))]
                    [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrements[2]), 2))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeRange", indicatorOfUnitForTimeRanges[0]), 1))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeRange", indicatorOfUnitForTimeRanges[1]), 1))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeRange", indicatorOfUnitForTimeRanges[2]), 1))]
                    [report.add(IsIn(KeyValue("lengthOfTimeRange", lengthOfTimeRanges[0]), moda_lotr2))]
                    [report.add(Eq(KeyValue("lengthOfTimeRange", lengthOfTimeRanges[1]), 24))]
                    [report.add(Eq(KeyValue("lengthOfTimeRange", lengthOfTimeRanges[2]), 12))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeIncrement", indicatorOfUnitForTimeIncrements[0]), 1))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeIncrement", indicatorOfUnitForTimeIncrements[1]), 1))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeIncrement", indicatorOfUnitForTimeIncrements[2]), 255))]
                    [report.add(Eq(KeyValue("timeIncrement", timeIncrements[0]), 24))]
                    [report.add(Eq(KeyValue("timeIncrement", timeIncrements[1]), 12))]
                    [report.add(Eq(KeyValue("timeIncrement", timeIncrements[2]), 0))]
                else:
                    report.add(Fail(f"Unsupported parameter in stream={stream}"))

                report.add(Eq(validityTimeBefore/100, moda_validityTime))
                report.add(Eq(validityDateBefore, moda_validityDate))

            else:

                # If we just set the stepRange (for non-instantaneous fields) to its
                # current value, then this causes the validity date and validity time
                # keys to be correctly computed.
                # Then we can compare the previous (possibly wrongly coded) value with
                # the newly computed one

                message.set("stepRange", stepRange)
                validityDate = message["validityDate"]
                validityTime = message["validityTime"]
                report.add(Eq(validityDate, validityDateBefore, f'Set stepRange={stepRange} has no effect on validityDate'))
                report.add(Eq(validityTime, validityTimeBefore, f'Set stepRange={stepRange} has no effect on validityTime'))

        return report

    def _pressure_level(self, message, p) -> Report:
        report = Report("CRRA Pressure Level")
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
        report.add(IsIn(message["level"], levels, "valid pressure level"))
        return report

    def _height_level(self, message, p) -> Report:
        report = Report("CRRA Height Level")
        levels = [15, 30, 50, 75, 100, 150, 200, 250, 300, 400, 500, 750, 1000, 1250, 1500, 2000, 2500, 3000]
        report.add(IsIn(message["level"], levels, "valid height level"))
        return report
