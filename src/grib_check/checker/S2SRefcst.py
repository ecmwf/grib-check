#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from grib_check.Assert import Eq, EqDbl, Fail, Ge, Gt, IsIn, IsMultipleOf, Le, Lt, Ne
from grib_check.Report import Report

from .GeneralChecks import GeneralChecks


class S2SRefcst(GeneralChecks):
    def __init__(self, lookup_table, check_limits=False):
        super().__init__(lookup_table, check_limits=check_limits)

    def _basic_checks(self, message, p) -> Report:
        report = Report("S2SRefcst Basic Checks")
        # Only 00, 06 12 and 18 Cycle OK
        report.add(IsIn(message["hour"], [0, 6, 12, 18]))
        report.add(
            IsIn(message["productionStatusOfProcessedData"], [4, 5])
        )  # TIGGE prod or test
        report.add(Le(message["endStep"], 30 * 24))
        report.add(IsMultipleOf(message["step"], 6))

        report.add(self._check_date(message, p))

        report.add(Eq(message["versionNumberOfGribLocalTables"], 0))

        return super()._basic_checks(message, p).add(report)

    def _latlon_grid(self, message) -> Report:
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

    # not registered in the lookup table
    def _statistical_process(self, message, p) -> Report:
        report = Report("S2SRefcst Statistical Process")

        topd = message.get("typeOfProcessedData", int)

        if topd in [0, 1, 2]:  # Analysis, Forecast, Analysis and forecast products
            pass
        elif topd in [3, 4]:  # Control forecast products, Perturbed forecast products
            report.add(Eq(message["productDefinitionTemplateNumber"], 61))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return report

        if message["indicatorOfUnitOfTimeRange"] == 11:  # six hours
            # Six hourly is OK
            pass
        else:
            report.add(Eq(message["indicatorOfUnitOfTimeRange"], 1))
            report.add(IsMultipleOf(message["forecastTime"], 6))

        report.add(Eq(message["timeIncrementBetweenSuccessiveFields"], 0))
        report.add(IsMultipleOf(message["step"], 6))

        return super()._statistical_process(message, p).add(report)

    # def _from_start(self, message, p) -> Report:
    #     report = Report("S2SRefcst From Start")
    #     if message["endStep"] != 0:
    #         report.add(self._check_range(message, p))
    #     return super()._from_start(message, p).add(report)

    def _point_in_time(self, message, p) -> Report:
        report = Report("S2SRefcst Point In Time")
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
            report.add(
                Eq(message["productDefinitionTemplateNumber"], 60, f"topd={topd}")
            )
        elif topd == 4:  # Perturbed forecast products
            report.add(
                Eq(message["productDefinitionTemplateNumber"], 60, f"topd={topd}")
            )
            report.add(
                Lt(
                    message["perturbationNumber"],
                    message["numberOfForecastsInEnsemble"],
                    f"topd={topd}",
                )
            )
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))

        if message["indicatorOfUnitOfTimeRange"] == 11:
            # Six hourly is OK
            pass
        else:
            report.add(Eq(message["indicatorOfUnitOfTimeRange"], 1))
            report.add(IsMultipleOf(message["forecastTime"], 6))

        return super()._point_in_time(message, p).add(report)
