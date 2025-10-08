#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from grib_check.Assert import Eq, IsIn, IsMultipleOf, Fail, Le, Ne
from grib_check.Report import Report
from grib_check.KeyValue import KeyValue
import datetime

from .Uerra import Uerra


class Crra(Uerra):
    def __init__(self, lookup_table, valueflg=False):
        super().__init__(lookup_table, valueflg=valueflg)

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
                report.add( IsIn(message["step"], [1, 2, 4, 5]) | IsMultipleOf(message["step"], 3))

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
        return report

    def _statistical_process(self, message, p) -> Report:
        report = Report("CRRA Statistical Process")

        topd = message.get("typeOfProcessedData", int)
        if topd.value() in [0, 1]:  # Analysis, Forecast
            report.add( Eq(message["productDefinitionTemplateNumber"], 8, f"topd={topd}"))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return report

        report.add(Eq(message["numberOfMissingInStatisticalProcess"], 0))
        report.add(Eq(message["typeOfTimeIncrement"], 2))
        # report.add(Eq(message["indicatorOfUnitOfTimeForTheIncrementBetweenTheSuccessiveFieldsUsed"], 255))
        report.add(Eq(message["minuteOfEndOfOverallTimeInterval"], 0))
        report.add(Eq(message["secondOfEndOfOverallTimeInterval"], 0))

        # xxx add all Paul's encoding options?

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
                # saved_date = datetime.date(year, month, day)

                numberOfTimeRanges = message["numberOfTimeRanges"]
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
                if typeOfStatisticalProcessings == [1,1]:
                    report = Report("dame - daily_sum_fc")
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
                elif typeOfStatisticalProcessings == [2,2] or typeOfStatisticalProcessings == [3,3]:
                    report = Report("dame - daily_max_fc")
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
                elif typeOfStatisticalProcessings == [0]:
                    report = Report("dame - daily_mean_an / daily_mean_fc")
                    [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrements[0]), 1))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeRange", indicatorOfUnitForTimeRanges[0]), 1))]
                    [report.add(Eq(KeyValue("lengthOfTimeRange", lengthOfTimeRanges[0]), 21))]
                    [report.add(Eq(KeyValue("indicatorOfUnitForTimeIncrement", indicatorOfUnitForTimeIncrements[0]), 1))]
                    [report.add(Eq(KeyValue("timeIncrement", timeIncrements[0]), 3))]
                else:
                    report.add(Fail(f"Unsupported parameter in stream={stream}"))

#               validityTime = int(message.get("validityTime", int).value()/100)
#               validityDate = message.get("validityDate", str).value()
#               dame_validityDate = str(year) + str(month).zfill(2) + str(day).zfill(2)

                report.add(Eq(message["productDefinitionTemplateNumber"], 8))
#               [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrement), 1, f'idx={idx}')) for idx, typeOfTimeIncrement in enumerate(typeOfTimeIncrements)]
                [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrements[0]), 1, f'idx={0}'))]
#               [report.add(IsIn(KeyValue("lengthOfTimeRange", lengthOfTimeRange), [21, 24], f'idx={idx}')) for idx, lengthOfTimeRange in enumerate(lengthOfTimeRanges)]
                [report.add(IsIn(KeyValue("lengthOfTimeRange", lengthOfTimeRanges[0]), [21, 24], f'idx={0}'))]
                # report.add(IsIn(validityTime, [21, 24]))
                # report.add(Eq(validityDate, dame_validityDate))

            elif Eq(stream, "moda"):

                report = Report("CRRA Check Validity Datetime - monthly means")
                report.add(Eq(message["productDefinitionTemplateNumber"], 8))

                numberOfTimeRanges = message["numberOfTimeRanges"]
                typeOfStatisticalProcessing = message["typeOfStatisticalProcessing"]
                moda_lotr1 = [669, 693, 717, 741]
                moda_lotr2 = [672, 696, 720, 744]

                if month == 11:
                    month2 = 1
                    year2 += 1
                elif month == 12:
                    month2 = 2
                    year2 += 1
                else:
                    month2 = month + 2
                    year2 = year

                last_date_in_month = datetime.date(year + int(month / 12), (month % 12) + 1, 1) - datetime.timedelta(days=1)
                last_date_in_month = int(str(last_date_in_month).replace('-', ''))
                last_date_in_month2 = datetime.date(year2, month2, 1) - datetime.timedelta(days=1)
                last_date_in_month2 = int(str(last_date_in_month2).replace('-', ''))
                first_date_next_month = datetime.date(year + int(month / 12), (month % 12) + 1, 1)
                first_date_next_month = int(str(first_date_next_month).replace('-', ''))
                first_date_month2 = datetime.date(year2, month2, 1)
                first_date_month2 = int(str(first_date_month2).replace('-', ''))

#               [report.add(Eq(typeOfTimeIncrement, 1, f'idx=0')) for idx, typeOfTimeIncrement in enumerate(typeOfTimeIncrements)]
                [report.add(Eq(typeOfTimeIncrements[0], 1, f'idx=0'))]

                if Eq(numberOfTimeRanges, 1):
                    # FIX(maee):
                    # if int(lengthOfTimeRange[0]) not in moda_lotr1:
                    #     report.add( Fail( f"Invalid outer value of lengthOfTimeRange({int(lengthOfTimeRange[0])}) (Should be in {moda_lotr1})"))
                    [report.add(IsIn(lengthOfTimeRange, moda_lotr1)) for lengthOfTimeRange in lengthOfTimeRanges]

                    if topd == 0:
                        moda_validityDate = last_date_in_month
                    elif topd == 1:
                        moda_validityDate = last_date_in_month2

                    report.add(Eq(validityDateBefore, moda_validityDate))

                elif Eq(numberOfTimeRanges, 2):

                    if typeOfStatisticalProcessing in [1, 2, 3]:
                        moda_validityDate = first_date_next_month

                elif Eq(numberOfTimeRanges, 3):
#                   [report.add(IsIn(lengthOfTimeRange, moda_lotr2, f'idx={idx}')) for idx, lengthOfTimeRange in enumerate(lengthOfTimeRanges)]
                    [report.add(IsIn(lengthOfTimeRanges[0], moda_lotr2, f'idx={0}'))]
                    moda_validityDate = first_date_month2
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
        report = Report("Crra Pressure Level")
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
