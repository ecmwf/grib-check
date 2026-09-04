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

from grib_check.Assert import Eq, IsIn
from grib_check.Report import Report

from .GeneralChecks import GeneralChecks


class Lcgcr(GeneralChecks):
    def __init__(self, lookup_table, check_limits=False, check_validity=True):
        super().__init__(lookup_table, check_limits=check_limits, check_validity=check_validity)
        self.logger = logging.getLogger(__class__.__name__)

    def _basic_checks(self, message, p):
        report = Report("LC-GCR Basic Checks")

        # WPMIP prod/test data
        report.add(IsIn(message["productionStatusOfProcessedData"], [14, 15]))

        # WPMIP centre/subCentre DGOV-577
        report.add(IsIn(message["centre"], ["ecmf", "babj", "rjtd", "nasa", "ncep"]))

        # WPMIP model ECC-2297
        report.add(IsIn(message["model"], ["ERA5", "CMA-40", "JRA-3Q", "MERRA-2", "CORe"]))

        # to use MARS new key "model"
        report.add(IsIn(message["backgroundProcess"], [1, 2, 3, 4, 255]))
        report.add(IsIn(message["generatingProcessIdentifier"], [1, 146]))

        # CCSDS compression
        # https://codes.ecmwf.int/grib/format/grib2/ctables/5/0/
        report.add(Eq(message["dataRepresentationTemplateNumber"], 42))

        report.add(Eq(message["bitsPerValue"], 16))
        report.add(self._check_date(message, p))

        return super()._basic_checks(message, p).add(report)

    def _monthly_mean_of_daily_means(self, message, p) -> Report:
        report = Report("LC-GCR Monthly mean of daily means")

        # The monthly means of the instantaneous variables (2t and mslp) are calculated from 6-hourly data (00, 06, 12 18),
        # as this is the minimum temporal frequency across all datasets.
        # For precipitation rate, which is an accumulation divided by time step, all available time steps are used.

        timeIncrements = message.get_array("timeIncrement")
        paramId = message["paramId"]

        if paramId != 235055:
          [report.add(Eq(timeIncrements[1], 6))]

        return super()._monthly_mean_of_daily_means(message, p).add(report)

    def _latlon_grid(self, message):
        report = Report(f"{__class__.__name__}.latlon_grid")

        report.add(Eq(message["Ni"], 288))
        report.add(Eq(message["Nj"], 145))
        report.add(Eq(message["scanningMode"], 0))
        report.add(Eq(message["shapeOfTheEarth"], 6))

        report.add(Eq(message["basicAngleOfTheInitialProductionDomain"], 0))
        # report.add(Missing(message, "subdivisionsOfBasicAngle"))
        report.add(Eq(message["latitudeOfFirstGridPoint"], 90000000))
        report.add(Eq(message["longitudeOfFirstGridPoint"], 0))
        report.add(Eq(message["latitudeOfLastGridPoint"], -90000000))
        report.add(Eq(message["longitudeOfLastGridPoint"], 358750000))
        report.add(Eq(message["iDirectionIncrement"], 1250000))
        report.add(Eq(message["jDirectionIncrement"], 1250000))

        return super()._latlon_grid(message).add(report)
