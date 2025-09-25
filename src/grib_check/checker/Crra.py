#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from grib_check.Assert import Eq, IsIn, IsMultipleOf, Fail
from grib_check.Report import Report

from .Uerra import Uerra


class Crra(Uerra):
    def __init__(self, lookup_table, valueflg=False):
        super().__init__(lookup_table, valueflg=valueflg)

    def basic_checks_2(self, message, p) -> Report:
        report = Report("Crra Basic Checks")
        report.add(IsIn(message["productionStatusOfProcessedData"], [10, 11]))
        report.add(
            IsIn(message["typeOfProcessedData"], [0, 1])
        )  # 0 = analysis , 1 = forecast
        if message["typeOfProcessedData"] == 0:
            report.add(Eq(message["step"], 0))
        else:
            report.add(
                IsIn(message["step"], [1, 2, 4, 5]) | IsMultipleOf(message["step"], 3)
            )
        return report

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

        # not registered in the lookup table
    def _check_validity_datetime(self, message):
        # If we just set the stepRange (for non-instantaneous fields) to its
        # current value, then this causes the validity date and validity time
        # keys to be correctly computed.
        # Then we can compare the previous (possibly wrongly coded) value with
        # the newly computed one

        report = Report("CRRA Check Validity Datetime")
        stepType = message.get("stepType", str)

        stream = message.get("stream", str) #xxx
        print("1 ",stream) #xxx

        if stepType != "instant":  # not instantaneous
            # Check only applies to accumulated, max etc.
            stepRange = message.get("stepRange", str)

            saved_validityDate = message["validityDate"]
            saved_validityTime = message["validityTime"]

            message.set("stepRange", stepRange)

            validityDate = message["validityDate"]
            validityTime = message["validityTime"]

            print("2 ",stream) #xxx
            # monthly/daily averages are archived under instant paramIds as param-db was not ready for all time-mean proper ones..
            stream = message.get("stream", str) #xxx
            print("3 ",stream) #xxx
            if stream == "dame":
                typeOfTimeIncrement = message.get_double_array("typeOfTimeIncrement")
                print(typeOfTimeIncrement)
                print(type(typeOfTimeIncrement))
                lengthOfTimeRange = message.get_double_array("lengthOfTimeRange")

                report.add(Eq(message["productDefinitionTemplateNumber"], 8))
                report.add(Eq(message["typeOfTimeIncrement"], 1))
                report.add(IsIn(message["lengthOfTimeRange"], [21, 24]))
                if validityDate != saved_validityDate:
                    report.add(
                        Fail(
                            f"Invalid validity Date/Time (Should be {validityDate} and {validityTime})"
                        )
                    )
            elif stream == "moda":
                print (message["lengthOfTimeRange"])
                pass
                report.add(Eq(message["productDefinitionTemplateNumber"], 8))
                report.add(Eq(message["typeOfTimeIncrement"], 1))
                month = message.get("month", int)
                month = month.value()
                year = message.get("year", int)
                year = year.value()
                print(year)
                print(type(year))
                if month in [1,3,5,7,8,10,12]:
                    day=31
                elif month in [4,6,9,11]:
                    day=30
                elif month == 2:
                    if year in [1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032]:
                        day=29
                    else:
                        day=28
                moda_validityDate = str(year) + str(month).zfill(2) + str(day)
                validityDate = "19911231"
                if validityDate != moda_validityDate or validityTime != saved_validityTime:
                    # print("warning: %s, field %d [%s]: invalid validity Date/Time (Should be %ld and %ld)" % (cfg['filename'], cfg['field'], cfg['param'], validityDate, validityTime))
                    report.add(
                        Fail(
                            f"Invalid validity Date/Time (Should be {moda_validityDate} and {validityTime})"
                        )
                    )
            else:
                if validityDate != saved_validityDate or validityTime != saved_validityTime:
                    # print("warning: %s, field %d [%s]: invalid validity Date/Time (Should be %ld and %ld)" % (cfg['filename'], cfg['field'], cfg['param'], validityDate, validityTime))
                    report.add(
                        Fail(
                            f"Invalid validity Date/Time (Should be {validityDate} and {validityTime})"
                        )
                    )
                    # cfg['warning'] += 1

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
