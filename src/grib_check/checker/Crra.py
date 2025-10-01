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

    def _basic_checks_2(self, message, p) -> Report:
    # this class must not inhereted anything
        report = Report("CRRA Basic Checks 2")
        report.add(IsIn(message["productionStatusOfProcessedData"], [10, 11]))
        return report

    def _basic_checks(self, message, p) -> Report:
        report = Report("CRRA Basic Checks")
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
        if stream != "moda":
            report.add(Eq(message["startStep"], 0))
        report.add(self._statistical_process(message, p))
        return report

        # not registered in the lookup table
    def _check_validity_datetime(self, message):

        report = Report("CRRA Check Validity Datetime")

        stepType = message.get("stepType", str)
        stream = message.get("stream", str)

        year = message["year"]
        month = message["month"]
        day = message["day"]
        # saved_date = datetime.date(year, month, day)

        typeOfTimeIncrements = [KeyValue("typeOfTimeIncrement", v) for v in message.get_long_array("typeOfTimeIncrement")]
        lengthOfTimeRanges = [KeyValue("lengthOfTimeRange", v) for v in message.get_long_array("lengthOfTimeRange")]

        validityDateBefore = message["validityDate"]
        validityTimeBefore = message["validityTime"]

        if Ne(stepType, "instant"):  # not instantaneous
            # Check only applies to accumulated, max etc.
            stepRange = message.get("stepRange", str)


            # monthly/daily averages are archived under instant paramIds as param-db was not ready for all time-mean proper ones..
            if Eq(stream, "dame"):

                report = Report("CRRA Check Validity Datetime - daily means")

#               validityTime = int(message.get("validityTime", int).value()/100)
#               validityDate = message.get("validityDate", str).value()
#               dame_validityDate = str(year) + str(month).zfill(2) + str(day).zfill(2)

                report.add(Eq(message["productDefinitionTemplateNumber"], 8))
                # FIX(maee):
#                 if int(typeOfTimeIncrement[0]) != 1:
#                     report.add( Fail( f"Invalid outer value of typeOfTimeIncrement({int(typeOfTimeIncrement[0])}) (Should be 1)"))
#                 if int(lengthOfTimeRange[0]) not in [21, 24]:
#                     report.add( Fail( f"Invalid outer value of lengthOfTimeRange({int(lengthOfTimeRange[0])}) (Should be in [21, 24])"))
# #               if validityTime not in [21, 24]:
# #                   report.add( Fail( f"Invalid validityTime (Should be validityTime({validityTime}))"))
# #               if validityDate != dame_validityDate:
# #                   report.add( Fail( f"Invalid validityDate({validityDate}) (Should be {dame_validityDate})"))
                [report.add(Eq(KeyValue("typeOfTimeIncrement", typeOfTimeIncrement), 1, f'idx={idx}')) for idx, typeOfTimeIncrement in enumerate(typeOfTimeIncrements)]
                [report.add(IsIn(KeyValue("lengthOfTimeRange", lengthOfTimeRange), [21, 24], f'idx={idx}')) for idx, lengthOfTimeRange in enumerate(lengthOfTimeRanges)]
                # report.add(IsIn(validityTime, [21, 24]))
                # report.add(Eq(validityDate, dame_validityDate))

            elif Eq(stream, "moda"):

                report = Report("CRRA Check Validity Datetime - monthly means")
                report.add(Eq(message["productDefinitionTemplateNumber"], 8))

                numberOfTimeRanges = message["numberOfTimeRanges"]
                typeOfStatisticalProcessing = message["typeOfStatisticalProcessing"]
                moda_lotr1 = [669, 693, 717, 741]
                moda_lotr2 = [672, 696, 720, 744]

                last_date_in_month = datetime.date(year.value() + int(month.value() / 12), (month.value() % 12) + 1, 1) - datetime.timedelta(days=1)
                first_date_next_month = datetime.date(year.value() + int(month.value() / 12), (month.value() % 12) + 1, 1)


                # FIX(maee):
                # if int(typeOfTimeIncrement[0]) != 1:
                #     report.add( Fail( f"Invalid outer value of typeOfTimeIncrement({int(typeOfTimeIncrement[0])}) (Should be 1)"))
                [report.add(Eq(typeOfTimeIncrement, 1, f'idx={idx}')) for idx, typeOfTimeIncrement in enumerate(typeOfTimeIncrements)]

                if Eq(numberOfTimeRanges, 1):
                    # FIX(maee):
                    # if int(lengthOfTimeRange[0]) not in moda_lotr1:
                    #     report.add( Fail( f"Invalid outer value of lengthOfTimeRange({int(lengthOfTimeRange[0])}) (Should be in {moda_lotr1})"))
                    [report.add(IsIn(lengthOfTimeRange, moda_lotr1)) for lengthOfTimeRange in lengthOfTimeRanges]

                    moda_validityDate = str(last_date_in_month).replace('-', '')

                    # Fix(maee):
#                   report.add(Eq(message["validityDate"], moda_validityDate)) #xxx
                    # if str(validityDateBefore.value()) != moda_validityDate:
                    #     report.add( Fail( f"Invalid {validityDateBefore} (Should be {moda_validityDate})"))
                    report.add(Eq(validityDateBefore, moda_validityDate))

                elif Eq(numberOfTimeRanges, 2):

                    if typeOfStatisticalProcessing in [1, 2, 3]:
                        moda_validityDate = str(first_date_next_month).replace('-', '')

                elif Eq(numberOfTimeRanges, 3):

                    # Fix(maee):
                    # if int(lengthOfTimeRange[0]) not in moda_lotr2:
                    #     report.add( Fail( f"Invalid outer value of lengthOfTimeRange({int(lengthOfTimeRange[0])}) (Should be in {moda_lotr2})"))

                    [report.add(IsIn(lengthOfTimeRange, moda_lotr2, f'idx={idx}')) for idx, lengthOfTimeRange in enumerate(lengthOfTimeRanges)]
                    if Eq(month, 11):
                        month_next = 1
                        year_next = year.value() + 1
                    elif Eq(month, 12):
                        month_next = 2
                        year_next = year.value() + 1
                    else:
                        month_next = month.value() + 2
                        year_next = year
                    moda_validityDate = str(year_next) + str(month_next).zfill(2) + "01"
                    # Fix(maee):
                    # if str(validityDateBefore.value()) != moda_validityDate:
                    #     report.add( Fail( f"Invalid {validityDateBefore} (Should be {moda_validityDate})"))
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

                # Fix(maee):
                # if validityDate != validityDateBefore or validityTime != validityTimeBefore:
                #     # print("warning: %s, field %d [%s]: invalid validity Date/Time (Should be %ld and %ld)" % (cfg['filename'], cfg['field'], cfg['param'], validityDate, validityTime))
                #     report.add( Fail( f"Invalid validity Date({validityDateBefore})/Time({validityTimeBefore}) (Should be {validityDate} and {validityTime})"))
                #     # cfg['warning'] += 1
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
