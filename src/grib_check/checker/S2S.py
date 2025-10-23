#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from grib_check.Assert import (
    Eq,
    EqDbl,
    Fail,
    Ge,
    Gt,
    IsIn,
    IsMultipleOf,
    Le,
    Lt,
    Ne,
    Pass,
)
from grib_check.KeyValue import KeyValue
from grib_check.Report import Report

from .GeneralChecks import GeneralChecks


class S2S(GeneralChecks):
    def __init__(self, lookup_table, check_limits=False, check_validity=True):
        super().__init__(lookup_table, check_limits=check_limits, check_validity=check_validity)

    def _basic_checks(self, message, p) -> Report:
        report = Report("S2S Basic Checks")
        report.add(IsIn(message["productionStatusOfProcessedData"], [6, 7]))
        report.add(IsMultipleOf(message.get("step", int), 6))

        report.add(Eq(message["versionNumberOfGribLocalTables"], 0))

        return super()._basic_checks(message, p).add(report)

    # not registered in the lookup table
    def _statistical_process(self, message, p) -> Report:
        report = Report("S2S Statistical Process")

        topd = message.get("typeOfProcessedData", int)

        if topd in [0, 1, 2]:  # Analysis, Forecast, Analysis and forecast products
            pass
        elif topd in [3, 4]:  # Control forecast products, Perturbed forecast products
            report.add(
                Eq(message["productDefinitionTemplateNumber"], 11, f"topd={topd}")
            )
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return report

        if message["indicatorOfUnitOfTimeRange"] == 11:  # six hours
            # Six hourly is OK
            pass
        else:
            report.add(Eq(message["indicatorOfUnitOfTimeRange"], 1))
            report.add(IsMultipleOf(message["forecastTime"], 6))

        tosp = message.get("typeOfStatisticalProcessing", int)
        if tosp == 0:  # Statistical processing not applied
            report.add(IsIn(message["timeIncrementBetweenSuccessiveFields"], [1, 4]))
        else:
            report.add(Eq(message["timeIncrementBetweenSuccessiveFields"], 0))
        report.add(IsMultipleOf(message["endStep"], 6))

        return super()._statistical_process(message, p).add(report)

    def _from_start(self, message, p) -> Report:
        report = Report("S2S From Start")
        endStep = message["endStep"]
        if endStep == 0:
            min_value, max_value = message.minmax()
            if min_value == 0 and max_value == 0:
                report.add(Pass(f"min and max are both {KeyValue(None, 0)} for {endStep}"))
            else:
                report.add(Fail(f"min and max should both be {KeyValue(None, 0)} for {endStep} but are {KeyValue(None, min_value)} and {KeyValue(None, max_value)}"))

        return super()._from_start(message, p).add(report)

    def _point_in_time(self, message, p) -> Report:
        report = Report("S2S Point In Time")
        topd = message.get("typeOfProcessedData", int)
        if topd in [0, 1]:  # Analysis, Forecast
            if message["productDefinitionTemplateNumber"] == 1:
                report.add(
                    Ne(message["numberOfForecastsInEnsemble"], 0, f"topd={topd}")
                )
                report.add(
                    Le(
                        message["perturbationNumber"],
                        message["numberOfForecastsInEnsemble"],
                        f"topd={topd}",
                    )
                )
        elif topd == 2:  # Analysis and forecast products
            pass
        elif topd == 3:  # Control forecast products
            # check.add(IsIn(message["productDefinitionTemplateNumber"], [60, 11, 1]))
            report.add(
                Eq(message["productDefinitionTemplateNumber"], 1, f"topd={topd}")
            )
        elif topd == 4:  # Perturbed forecast products
            # check.add(IsIn(message["productDefinitionTemplateNumber"], [60, 11, 1]))
            report.add(
                Eq(message["productDefinitionTemplateNumber"], 1, f"topd={topd}")
            )
            report.add(
                Le(
                    message["perturbationNumber"],
                    message["numberOfForecastsInEnsemble"] - 1,
                    f"topd={topd}",
                )
            )
        else:
            report.add(
                Fail(
                    f'Unsupported typeOfProcessedData {message["typeOfProcessedData"]}'
                )
            )

        if message["indicatorOfUnitOfTimeRange"] == 11:
            # Six hourly is OK
            pass
        else:
            report.add(Eq(message["indicatorOfUnitOfTimeRange"], 1))
            report.add(IsMultipleOf(message["forecastTime"], 6))

        return super()._point_in_time(message, p).add(report)

    def _latlon_grid(self, message):
        report = Report(f"{__class__.__name__}.latlon_grid")

        tolerance = 1.0 / 1000000.0  # angular tolerance for grib2: micro degrees
        meridian = message["numberOfPointsAlongAMeridian"]
        parallel = message["numberOfPointsAlongAParallel"]

        north = message["latitudeOfFirstGridPoint"]
        south = message["latitudeOfLastGridPoint"]
        west = message["longitudeOfFirstGridPoint"]
        east = message["longitudeOfLastGridPoint"]

        ns = message["jDirectionIncrement"]
        we = message["iDirectionIncrement"]

        dnorth = message.get("latitudeOfFirstGridPointInDegrees", float)
        dsouth = message.get("latitudeOfLastGridPointInDegrees", float)
        dwest = message.get("longitudeOfFirstGridPointInDegrees", float)
        deast = message.get("longitudeOfLastGridPointInDegrees", float)

        dns = message.get("jDirectionIncrementInDegrees", float)
        dwe = message.get("iDirectionIncrementInDegrees", float)

        if message["iScansNegatively"] != 0:
            east, west = west, east
            deast, dwest = dwest, deast

        if message["jScansPositively"] != 0:
            north, south = south, north
            dnorth, dsouth = dsouth, dnorth

        report.add(Gt(north, south, "north > south"))
        report.add(Gt(east, west, "east > west"))

        # Check that the grid is symmetrical */
        report.add(Eq(north, -south, "north == -south"))
        report.add(EqDbl(dnorth, -dsouth, tolerance, "dnorth == -dsouth"))
        report.add(
            Eq(parallel, (east - west) / we + 1, "parallel == (east - west) / we + 1")
        )
        report.add(
            Lt(
                ((deast - dwest) / dwe + 1 - parallel).abs(),
                1e-10,
                "math.fabs((deast - dwest) / dwe + 1 - parallel) < 1e-10",
            )
        )
        report.add(
            Eq(
                meridian,
                (north - south) / ns + 1,
                "meridian == (north - south) / ns + 1",
            )
        )
        report.add(
            Lt(
                ((dnorth - dsouth) / dns + 1 - meridian).abs(),
                1e-10,
                "math.fabs((dnorth - dsouth) / dns + 1 - meridian) < 1e-10 ",
            )
        )

        # Check that the field is global */
        area = (dnorth - dsouth) * (deast - dwest)
        globe = 360.0 * 180.0
        report.add(Le(area, globe, "area <= globe"))
        report.add(Ge(area, globe * 0.95, "area >= globe*0.95"))

        return super()._latlon_grid(message).add(report)

    def _pressure_level(self, message, p) -> Report:
        report = Report("S2S Pressure Level")
        levels = [1000, 925, 850, 700, 500, 300, 200, 100, 50, 10]
        report.add(IsIn(message["level"], levels, "check pressure level"))
        return report
