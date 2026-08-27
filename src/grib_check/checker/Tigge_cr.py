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

from grib_check.Assert import Eq, Missing
from grib_check.Report import Report

from .Tigge import Tigge


class Tigge_cr(Tigge):
    def __init__(self, lookup_table, check_limits=False, check_validity=True):
        super().__init__(lookup_table, check_limits=check_limits, check_validity=check_validity)
        self.logger = logging.getLogger(__class__.__name__)

    def _basic_checks(self, message, p):
        report = Report("Tigge_cr Basic :Checks")

        # CCSDS compression
        # https://codes.ecmwf.int/grib/format/grib2/ctables/5/0/
        report.add(Eq(message["dataRepresentationTemplateNumber"], 42))

        return super()._basic_checks(message, p).add(report)

    def _latlon_grid(self, message):
        report = Report(f"{__class__.__name__}.latlon_grid")

        report.add(Eq(message["scanningMode"], 0))
        report.add(Eq(message["shapeOfTheEarth"], 6))
        report.add(Eq(message["basicAngleOfTheInitialProductionDomain"], 0))
        report.add(Eq(message["resolutionAndComponentFlags"], 48))
        report.add(Missing(message, "subdivisionsOfBasicAngle"))

        levtype = message.get("levtype")
        if levtype == "sfc":
          report.add(Eq(message["Ni"], 1440))
          report.add(Eq(message["Nj"], 721))
          report.add(Eq(message["latitudeOfFirstGridPoint"], 90000000))
          report.add(Eq(message["longitudeOfFirstGridPoint"], 0))
          report.add(Eq(message["latitudeOfLastGridPoint"], -90000000))
          report.add(Eq(message["longitudeOfLastGridPoint"], 359750000))
          report.add(Eq(message["iDirectionIncrement"], 250000))
          report.add(Eq(message["jDirectionIncrement"], 250000))
        else:
          report.add(Eq(message["Ni"], 720))
          report.add(Eq(message["Nj"], 361))
          report.add(Eq(message["latitudeOfFirstGridPoint"], 90000000))
          report.add(Eq(message["longitudeOfFirstGridPoint"], 0))
          report.add(Eq(message["latitudeOfLastGridPoint"], -90000000))
          report.add(Eq(message["longitudeOfLastGridPoint"], 359500000))
          report.add(Eq(message["iDirectionIncrement"], 500000))
          report.add(Eq(message["jDirectionIncrement"], 500000))

        return super()._latlon_grid(message).add(report)
