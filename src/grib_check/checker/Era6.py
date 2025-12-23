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

from grib_check.CheckEngine import CheckEngine
from grib_check.Assert import Eq, IsIn, IsMultipleOf, Missing, Exists
from grib_check.Report import Report

from .GeneralChecks import GeneralChecks

class era6(GeneralChecks):
    def __init__(self, lookup_table, check_limits=False, check_validity=True):
        super().__init__(lookup_table, check_limits=check_limits, check_validity=check_validity)
        self.logger = logging.getLogger(__class__.__name__)
        self.register_checks(
            {
                "basic_checks_era6": self._basic_checks_era6,
                "level_keys_era6": self._level_keys_era6,
                "pressure_level_era6": self._pressure_level_era6,
                "height_level_era6": self._height_level_era6,
                "model_level_era6": self._model_level_era6,
            }
        )

    def _basic_checks_era6(self, message, p) -> Report:
        report = Report("ERA6 Basic Checks")
        marsType = message.get("marsType", str)
        # re-analysis regarding code table 1.3
        report.add(IsIn(message["productionStatusOfProcessedData"], [3]))
        report.add(IsIn(message.get("centre",int), [98]))
        report.add(IsIn(message.get("subCentre",int), [0]))
        # IFS cycle cy49r2
        report.add(IsIn(message["backgroundProcess"], [255]))
        report.add(IsIn(message["generatingProcessIdentifier"], [159]))
        report.add(IsIn(message["dataRepresentationTemplateNumber"], [42]))
        report.add(Missing(message, "hoursAfterDataCutoff"))
        report.add(Missing(message, "minutesAfterDataCutoff"))
        report.add(IsIn(message["indicatorOfUnitForForecastTime"], [1]))
        if marsType == "an": # 0 - Analysis
            report.add(IsIn(message["significanceOfReferenceTime"], [0]))
        else: # 1 - Start of forecast
            report.add(IsIn(message["significanceOfReferenceTime"], [1]))

        report.add(
            IsIn(message.get("typeOfProcessedData", int), [0, 1, 2])
        )  # 0 = analysis , 1 = forecast, 2 = Analysis and forecast products
        if message["typeOfProcessedData"] == 0:
            report.add(Eq(message["step"], 0))
        else:
            report.add(
                IsIn(message["step"], list(range(0, 19))) | IsMultipleOf(message["step"], 1)
            )
        return report

    def _level_keys_era6(self, message, p):
        report = Report("ERA6 level keys")
        ty1stfxsfc = message.get("typeOfFirstFixedSurface", int)
        ty2ndfxsfc = message.get("typeOfSecondFixedSurface", int)
        # for these entries we expect the level keys (sv,sf) to be missing
        if ty1stfxsfc in [1,2,3,5,7,8,10,11,12,14,15,166,174,175,176,177,188,188,189,255]:
            report.add(Missing(message, "scaleFactorOfFirstFixedSurface"))
            report.add(Missing(message, "scaledValueOfFirstFixedSurface"))
        if ty2ndfxsfc in [1,2,3,5,7,8,10,11,12,14,15,166,174,175,176,177,188,188,189,255]:
            report.add(Missing(message, "scaleFactorOfSecondFixedSurface"))
            report.add(Missing(message, "scaledValueOfSecondFixedSurface"))
       	if ty1stfxsfc in [20,100,102,103,105,106,160,168]:
            report.add(Exists(message, "scaleFactorOfFirstFixedSurface"))
            report.add(Exists(message, "scaledValueOfFirstFixedSurface"))
        if ty2ndfxsfc in [20,100,102,103,105,106,160,168]:
            report.add(Exists(message, "scaleFactorOfSecondFixedSurface"))
            report.add(Exists(message, "scaledValueOfSecondFixedSurface"))
        return report

    def _pressure_level_era6(self, message, p) -> Report:
        report = Report("ERA6 Pressure Level")
        ty1stfxsfc = message.get("typeOfFirstFixedSurface", int)
        if ty1stfxsfc == 100:
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
            report.add(IsIn(message["level"], levels))
        else:
            report.add(Report("No pressure level data"))
        return report

    def _height_level_era6(self, message, p) -> Report:
        report = Report("ERA6 Height Level")
        ty1stfxsfc = message.get("typeOfFirstFixedSurface", int)
        if ty1stfxsfc == 103 or ty1stfxsfc == 102 :
            levels = [15, 30, 50, 75, 100, 150, 200, 250, 300, 400, 500]
            report.add(IsIn(message["level"], levels))
            paramIds=[10,54,130,157,246,247,3031]
            report.add(IsIn(message["paramId"],paramIds))
        else:
            report.add(Report("No height level data"))
        return report

    def _model_level_era6(self, message, p) -> Report:
        report = Report("ERA6 model Level")
        ty1stfxsfc = message.get("typeOfFirstFixedSurface", int)
        if ty1stfxsfc == 105:
            levels = list(range(1, 138))
            report.add(IsIn(message["level"], levels))
        else:
            report.add(Report("No model level data"))
        return report
