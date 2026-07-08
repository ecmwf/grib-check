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

from grib_check.Assert import Eq, IsIn, IsMultipleOf, Le, OverallDateMatches
from grib_check.Report import Report

from .GeneralChecks import GeneralChecks


class Lcgcr(GeneralChecks):
    def __init__(self, lookup_table, check_limits=False, check_validity=True):
        super().__init__(lookup_table, check_limits=check_limits, check_validity=check_validity)
        self.logger = logging.getLogger(__class__.__name__)
        self.register_checks(
            {
                "overall_time_lcgcr": self._overall_time_lcgcr,
            }
        )

    def _basic_checks(self, message, p):
        report = Report("LC-GCR Basic Checks")

        # WPMIP prod/test data
        report.add(IsIn(message["productionStatusOfProcessedData"], [14, 15]))

        # WPMIP centre/subCentre DGOV-577
        report.add(IsIn(message["centre"], ["ecmf", "babj", "rjtd", "nasa"]))

        # to use MARS new key "model"
        report.add(Le(message["backgroundProcess"], 255))
        report.add(Le(message["generatingProcessIdentifier"], 146))

        # CCSDS compression
        # https://codes.ecmwf.int/grib/format/grib2/ctables/5/0/
        report.add(Eq(message["dataRepresentationTemplateNumber"], 42))

        report.add(Eq(message["step"], None))  # xxx
        report.add(Eq(message["bitsPerValue"], 16))
        report.add(self._check_date(message, p))

        return super()._basic_checks(message, p).add(report)
        # return report

    # not registered in the lookup table
    def _statistical_process(self, message, p) -> Report:
        report = Report("LC-GCR Statistical Process")

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

        report.add(Eq(message["Ni"], 288))
        report.add(Eq(message["Nj"], 145))
        report.add(Eq(message["scanningMode"], 0))

        report.add(Eq(message["basicAngleOfTheInitialProductionDomain"], 0))
        # report.add(Missing(message, "subdivisionsOfBasicAngle"))
        report.add(Eq(message["latitudeOfFirstGridPoint"], 90000000))
        report.add(Eq(message["longitudeOfFirstGridPoint"], 0))
        report.add(Eq(message["latitudeOfLastGridPoint"], -90000000))
        report.add(Eq(message["longitudeOfLastGridPoint"], 358750000))
        report.add(Eq(message["iDirectionIncrement"], 1250000))
        report.add(Eq(message["jDirectionIncrement"], 1250000))

        return super()._latlon_grid(message).add(report)

    def _overall_time_lcgcr(self, message, p):
        report = Report("LC-GCR overall time")
        pdtn = message.get("productDefinitionTemplateNumber", int)
        if pdtn in [8, 11]:
            timeunit = message.get_long_array("indicatorOfUnitForTimeRange")[0]
            if timeunit == 2:
                scaleIt = 24
            else:
                scaleIt = 1
            if timeunit in [1, 2]:
                dataDate = message.get("dataDate", int)
                dataTime = message.get("dataTime", int)
                forecastTime = message.get("forecastTime", int)
                # we need the most outer loop
                lengthOfTimeRange = message.get_long_array("lengthOfTimeRange")[0] * scaleIt
                yearOfEndOfOverallTimeInterval = message.get("yearOfEndOfOverallTimeInterval", int)
                monthOfEndOfOverallTimeInterval = message.get("monthOfEndOfOverallTimeInterval", int)
                dayOfEndOfOverallTimeInterval = message.get("dayOfEndOfOverallTimeInterval", int)
                hourOfEndOfOverallTimeInterval = message.get("hourOfEndOfOverallTimeInterval", int)
                minuteOfEndOfOverallTimeInterval = message.get("minuteOfEndOfOverallTimeInterval", int)
                secondOfEndOfOverallTimeInterval = message.get("secondOfEndOfOverallTimeInterval", int)
                report.add(OverallDateMatches(
                              dataDate=dataDate,
                              dataTime=dataTime,
                              forecastTime=forecastTime,
                              lengthOfTimeRange=lengthOfTimeRange,
                              yearOfEndOfOverallTimeInterval=yearOfEndOfOverallTimeInterval,
                              monthOfEndOfOverallTimeInterval=monthOfEndOfOverallTimeInterval,
                              dayOfEndOfOverallTimeInterval=dayOfEndOfOverallTimeInterval,
                              hourOfEndOfOverallTimeInterval=hourOfEndOfOverallTimeInterval,
                              minuteOfEndOfOverallTimeInterval=minuteOfEndOfOverallTimeInterval,
                              secondOfEndOfOverallTimeInterval=secondOfEndOfOverallTimeInterval))
            else:
                report.add(Report("Time-unit of statistical unit not hours or days, can't check"))
        else:
            report.add(Report("No time-statistical data !"))
        return report
