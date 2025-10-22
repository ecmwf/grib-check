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

from grib_check.Assert import Eq, IsIn, IsMultipleOf, Le, Ne
from grib_check.Report import Report

from .GeneralChecks import GeneralChecks


class Wpmip(GeneralChecks):
    def __init__(self, lookup_table, check_limits=False, check_validity=True):
        super().__init__(lookup_table, check_limits=check_limits, check_validity=check_validity)
        self.logger = logging.getLogger(__class__.__name__)
        self.register_checks(
            {
                "pressure_level": self._pressure_level,
            }
        )

    def _basic_checks(self, message, p):
        report = Report("Wpmip Basic Checks")

        # WPMIP prod/test data
        report.add(IsIn(message["productionStatusOfProcessedData"], [16, 17]))

        # WPMIP centre/subCentre DGOV-577
        report.add(Eq(message["centre"], "323"))
        report.add(Ne(message["subCentre"], 0))

        # to use MARS new key "model"
        report.add(Le(message["backgroundProcess"], 255))
        report.add(Le(message["generatingProcessIdentifier"], 4))

        # CCSDS compression
        # https://codes.ecmwf.int/grib/format/grib2/ctables/5/0/
        report.add(Eq(message["dataRepresentationTemplateNumber"], 42))

        #       # Only 00, 06 12 and 18 Cycle OK
        #       report.add(IsIn(message["hour"], [0, 6, 12, 18]))

        report.add(Le(message["endStep"], 10 * 36))
        report.add(IsMultipleOf(message["step"], 6))
        report.add(self._check_date(message, p))

        return super()._basic_checks(message, p).add(report)
        # return report

    def _pressure_level(self, message, p):
        report = Report("WPMIP Pressure level")
        levels = [
            10,
            50,
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
        report = Report("WPMIP Statistical Process")

        if message.get("indicatorOfUnitOfTimeRange") == 11:  # six hours
            # Six hourly is OK
            pass
        else:
            report.add(Eq(message["indicatorOfUnitOfTimeRange"], 1))
            report.add(IsMultipleOf(message["forecastTime"], 6))

        report.add(Eq(message["timeIncrementBetweenSuccessiveFields"], 0))
        report.add(IsMultipleOf(message["endStep"], 6))

        return super()._statistical_process(message, p).add(report)

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
