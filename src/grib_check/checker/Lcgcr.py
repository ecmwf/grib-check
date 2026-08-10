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

from grib_check.Assert import Eq, IsIn, IsMultipleOf, Le
from grib_check.DateTime import DataTime, TimeDelta
from grib_check.Report import Report
from grib_check.KeyValue import KeyValue

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
            timeRangeUnit = message.get_long_array("indicatorOfUnitForTimeRange")[0]
            # TODO(maee): is this correct?
            if timeRangeUnit in [0, 1, 2, 10, 11, 12, 13]:
                # we need the most outer loop
                lengthOfTimeRange = message.get_long_array("lengthOfTimeRange")[0]

                start = DataTime(message["dataDate"], message["dataTime"]).to_key_value()
                forecast_td = TimeDelta(message["forecastTime"], message["indicatorOfUnitForForecastTime"]).to_key_value()
                range_td = TimeDelta(KeyValue("lengthOfTimeRange", int(lengthOfTimeRange)), KeyValue("indicatorOfUnitForTimeRange", int(timeRangeUnit))).to_key_value()
                # TODO(maee): Please check if this is correct
                expected_end = start + forecast_td + range_td

                actual_end = DataTime(
                    year=message["yearOfEndOfOverallTimeInterval"],
                    month=message["monthOfEndOfOverallTimeInterval"],
                    day=message["dayOfEndOfOverallTimeInterval"],
                    hour=message["hourOfEndOfOverallTimeInterval"],
                    minute=message["minuteOfEndOfOverallTimeInterval"],
                    second=message["secondOfEndOfOverallTimeInterval"],
                ).to_key_value()
                report.add(Eq(expected_end, actual_end, f"start + forecast + range == end\n{expected_end.value()} == {actual_end.value()}"))
            else:
                report.add(Report("Time-unit of statistical unit not supported, can't check"))
        else:
            report.add(Report("No time-statistical data !"))
        return report
