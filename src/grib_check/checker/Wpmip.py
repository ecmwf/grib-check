#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import logging

from grib_check.Assert import Eq, Fail, IsIn, IsMultipleOf, Le, Ne
from grib_check.Report import Report

from .Wmo import Wmo


class Wpmip(Wmo):
    def __init__(self, lookup_table, valueflg=False):
        super().__init__(lookup_table, valueflg=valueflg)
        self.logger = logging.getLogger(__class__.__name__)

    def _basic_checks(self, message, p):
        report = Report("Wpmip Basic Checks")

        # WPMIP prod/test data
        report.add(IsIn(message["productionStatusOfProcessedData"], [16, 17]))

        # to use MARS new key "model"
        report.add(Eq(message["backgroundProcess"], 1))
        report.add(Eq(message["generatingProcessIdentifier"], 3))

        # CCSDS compression
        # https://codes.ecmwf.int/grib/format/grib2/ctables/5/0/
        report.add(Eq(message["dataRepresentationTemplateNumber"], 42))

        #       # Only 00, 06 12 and 18 Cycle OK
        #       report.add(IsIn(message["hour"], [0, 6, 12, 18]))

        report.add(Le(message["endStep"], 10 * 24))
        report.add(IsMultipleOf(message["step"], 6))
        report.add(self._check_date(message, p))

        return super()._basic_checks(message, p).add(report)
        # return report

    def _pressure_level(self, message, p):
        report = Report("WPMIP Pressure level")
        levels = [
            1,
            10,
            20,
            30,
            50,
            70,
            100,
            150,
            200,
            250,
            300,
            400,
            500,
            700,
            850,
            925,
            1000,
        ]
        report.add(IsIn(message["level"], levels))
        return report

    # not registered in the lookup table
    def _statistical_process(self, message, p) -> Report:
        report = Report("Wpmip Statistical Process")

        topd = message.get("typeOfProcessedData", int)

        if topd in [0, 1, 2]:  # Analysis, Forecast, Analysis and forecast products
            pass
        elif topd in [3, 4]:  # Control forecast products, Perturbed forecast products
            report.add(Eq(message["productDefinitionTemplateNumber"], 11))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return report

        if message.get("indicatorOfUnitOfTimeRange") == 11:  # six hours
            # Six hourly is OK
            pass
        else:
            report.add(Eq(message["indicatorOfUnitOfTimeRange"], 1))
            report.add(IsMultipleOf(message["forecastTime"], 6))

        report.add(Eq(message["timeIncrementBetweenSuccessiveFields"], 0))
        report.add(IsMultipleOf(message["endStep"], 6))

        return super()._statistical_process(message, p).add(report)

    def _from_start(self, message, p) -> Report:
        report = Report("Wpmip From Start")
        if message.get("endStep") != 0:
            report.add(self._check_range(message, p))

        return super()._from_start(message, p).add(report)

    def _point_in_time(self, message, p) -> Report:
        report = Report("Wpmip Point in Time")

        topd = message.get("typeOfProcessedData", int)
        if topd in [0, 1]:  # Analysis, Forecast
            if message.get("productDefinitionTemplateNumber") == 1:
                report.add(
                    Ne(message["numberOfForecastsInEnsemble"], 0, f"topd = {topd}")
                )
                report.add(
                    Le(
                        message["perturbationNumber"],
                        message.get("numberOfForecastsInEnsemble"),
                        f"topd = {topd}",
                    )
                )
        elif topd == 2:  # Analysis and forecast products
            pass
        elif topd == 3:  # Control forecast products
            report.add(
                Eq(message["productDefinitionTemplateNumber"], 1, f"topd = {topd}")
            )
        elif topd == 4:  # Perturbed forecast products
            report.add(
                Eq(message["productDefinitionTemplateNumber"], 1, f"topd = {topd}")
            )
            report.add(
                Le(
                    message["perturbationNumber"],
                    message["numberOfForecastsInEnsemble"] - 1,
                    f"topd = {topd}",
                )
            )
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))

        return super()._point_in_time(message, p).add(report)

    def _latlon_grid(self, message):
        report = Report(f"{__class__.__name__}.latlon_grid")

        report.add(Eq(message["Ni"], 1440))
        report.add(Eq(message["Nj"], 721))
        report.add(Eq(message["scanningMode"], 0))

        report.add(Eq(message["basicAngleOfTheInitialProductionDomain"], 0))
        # report.add(Missing(message, "subdivisionsOfBasicAngle"))
        report.add(Eq(message["latitudeOfFirstGridPoint"], 90000000))
        report.add(Eq(message["longitudeOfFirstGridPoint"], 0))
        report.add(Eq(message["latitudeOfLastGridPoint"], -90000000))
        report.add(Eq(message["longitudeOfLastGridPoint"], 359750000))
        report.add(Eq(message["iDirectionIncrement"], 250000))
        report.add(Eq(message["jDirectionIncrement"], 250000))

        return super()._latlon_grid(message).add(report)
