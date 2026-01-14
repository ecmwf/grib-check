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
from grib_check.Assert import Eq, IsIn, IsMultipleOf, Missing, Exists, OverallDateMatches
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
                "pt_level_era6":self._pt_level_era6,
                "pv_level_era6":self._pv_level_era6,
                "overall_time_era6":self._overall_time_era6,
                "check_expected_paramid_era6": self._check_expected_paramid_era6,
                "check_range": self._check_range,
                "topd_era6": self._topd_era6,
            }
        )

    def _basic_checks_era6(self, message, p) -> Report:
        report = Report("ERA6 Basic Checks")
        marsType = message.get("marsType", str)
        #typeOfTimeIncrement = message.get("typeOfTimeIncrement",int)
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
            #if (typeOfTimeIncrement == 2):
            report.add(Eq(message["step"], 0))
            #else:
            #    report.add(Report("typeOfTimeIncrement = 2, can't check the step!"))
        else:
            #if (typeOfTimeIncrement == 2):
            report.add(
                IsIn(message["step"], list(range(0, 19))) | IsMultipleOf(message["step"], 1)
            )
            #else:
            #    report.add(Report("typeOfTimeIncrement == 2, can't check the step!"))
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
        levtype = message.get("levtype",str)
        if (ty1stfxsfc == 103 or ty1stfxsfc == 102) and levtype == 'hl' :
            levels = [15, 30, 50, 75, 100, 150, 200, 250, 300, 400, 500]
            report.add(IsIn(message["level"], levels))
            #paramIds=[10,54,130,157,246,247,3031]
            #report.add(IsIn(message["paramId"],paramIds))
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

    def _pt_level_era6(self, message, p) -> Report:
        report = Report("ERA6 potential temperature Level")
        ty1stfxsfc = message.get("typeOfFirstFixedSurface", int)
        if ty1stfxsfc == 107:
            levels = [265,275,285,300,315,320,330,350,370,395,430,475,530,600,700,850]
            report.add(IsIn(message["level"], levels))
        else:
            report.add(Report("No potential temperature level data"))
        return report

    def _pv_level_era6(self, message, p) -> Report:
        report = Report("ERA6 potential vorticity Level")
        ty1stfxsfc = message.get("typeOfFirstFixedSurface", int)
        if ty1stfxsfc == 109:
            levels = [1500,2000]
            report.add(IsIn(message["level"], levels))
        else:
            report.add(Report("No potential vorticity level data"))
        return report

    def _check_expected_paramid_era6(self, message, p):
        report = Report("ERA6 expected paramIds")
        mars_stream = message.get("stream", str)
        mars_type = message.get("type", str)
        mars_levtype = message.get("levtype", str)
        mars_timespan = message.get("timespan", str)
        mars_paramtype = message.get("paramtype", str)
        if mars_levtype == 'hl':
            paramids = [10,54,130,157,246,247,3031]
            report.add(IsIn(message["paramId"], paramids))
        if mars_levtype == 'o2d':
            paramids = [
                262000,
                262001,
                262002,
                262003,
                262004,
                262005,
                262006,
                262008,
                262009,
                262011,
                262014,
                262015,
                262017,
                262100,
                262101,
                262102,
                262103,
                262104,
                262105,
                262106,
                262108,
                262109,
                262110,
                262113,
                262118,
                262119,
                262120,
                262121,
                262122,
                262123,
                262124,
                262139,
                262140,
                262141,
                262143,
                262900,
                262906,
                262907]
            report.add(IsIn(message["paramId"], paramids))
        if mars_levtype == 'o3d':
            paramids = [262500,262501,262505,262506,262507]
            report.add(IsIn(message["paramId"], paramids))
        if mars_levtype == 'sol':
            paramids = [33,238,228038,228141,260199,260360]
            report.add(IsIn(message["paramId"], paramids))
       	if mars_levtype == 'pv':
            paramids = [3,54,129,131,132,133,203]
            report.add(IsIn(message["paramId"], paramids))
       	if mars_levtype == 'pt':
            paramids = [53,54,60,131,132,133,138,155,203]
            report.add(IsIn(message["paramId"], paramids))
        if mars_type == '4i':
            paramids = [130,131,132,133,138,152,155,203]
            report.add(IsIn(message["paramId"], paramids))
        if mars_type == 'me':
            paramids = [130,131,132,138,152,155]
            report.add(IsIn(message["paramId"], paramids))
        if mars_paramtype == 'wave_spectra':
            paramids = [140251]
            report.add(IsIn(message["paramId"], paramids))
        if mars_paramtype == 'wave' and (mars_stream != 'sttd' and mars_stream != 'stte'):
            paramids = [
                     140098,
                     140099,
                     140100,
                     140101,
                     140102,
                     140103,
                     140104,
                     140105,
                     140112,
                     140113,
                     140114,
                     140115,
                     140116,
                     140117,
                     140118,
                     140119,
                     140120,
                     140121,
                     140122,
                     140123,
                     140124,
                     140125,
                     140126,
                     140127,
                     140128,
                     140129,
                     140131,
                     140132,
                     140133,
                     140134,
                     140207,
                     140208,
                     140209,
                     140211,
                     140212,
                     140214,
                     140215,
                     140216,
                     140217,
                     140218,
                     140219,
                     140220,
                     140221,
                     140222,
                     140223,
                     140224,
                     140225,
                     140226,
                     140227,
                     140228,
                     140229,
                     140230,
                     140231,
                     140232,
                     140233,
                     140234,
                     140235,
                     140236,
                     140237,
                     140238,
                     140239,
                     140244,
                     140245,
                     140246,
                     140247,
                     140249,
                     140252,
                     140253,
                     140254]
            report.add(IsIn(message["paramId"], paramids))
        if mars_stream == 'sttd' or mars_stream == 'stte':
            mars_stattype = message.get("stattype", str)
            if mars_stattype in ['daac', 'daav', 'damn', 'damx', 'dasd']:
                report.add(IsIn(message["timespan"], ['1h','none']))
            else:
               	report.add(IsIn(message["timespan"], ['24h']))
            paramids = [
               228004,
               228005,
               228143,
               235033,
               235041,
               235042,
               235043,
               235078,
               235079,
               235080,
               235083,
               235084,
               235085,
               235086,
               235087,
               235088,
               235089,
               235090,
               235091,
               235099,
               235107,
               235108,
               235109,
               235110,
               235111,
               235129,
               235134,
               235136,
               235137,
               235151,
               235159,
               235165,
               235166,
               235168,
               235238,
               235244,
               235245,
               235261,
               235263,
               235281,
               235282,
               235283,
               235284,
               235285,
               235288,
               235289,
               235290,
               235291,
               235292,
               235293,
               235294,
               235295,
               235296,
               235297,
               235298,
               235299,
               235300,
               235301,
               235302,
               235305,
               235306,
               235307,
               235308,
               235309,
               235320,
               235328,
               235329,
               235396,
               235411,
               237033,
               237041,
               237042,
               237043,
               237078,
               237079,
               237080,
               237083,
               237084,
               237085,
               237086,
               237087,
               237088,
               237089,
               237090,
               237091,
               237099,
               237107,
               237108,
               237109,
               237110,
               237111,
               237129,
               237134,
               237136,
               237137,
               237151,
               237159,
               237165,
               237166,
               237167,
               237168,
               237207,
               237238,
               237244,
               237245,
               237261,
               237263,
               237281,
               237282,
               237283,
               237284,
               237285,
               237288,
               237289,
               237290,
               237291,
               237292,
               237293,
               237294,
               237295,
               237296,
               237297,
               237298,
               237299,
               237300,
               237301,
               237302,
               237305,
               237306,
               237307,
               237308,
               237309,
               237320,
               237328,
               237329,
               237396,
               237411,
               238033,
               238041,
               238042,
               238043,
               238078,
               238079,
               238080,
               238083,
               238084,
               238085,
               238086,
               238087,
               238088,
               238089,
               238090,
               238091,
               238099,
               238107,
               238108,
               238109,
               238110,
               238111,
               238129,
               238134,
               238136,
               238137,
               238151,
               238159,
               238165,
               238166,
               238167,
               238168,
               238207,
               238238,
               238244,
               238245,
               238261,
               238263,
               238281,
               238282,
               238283,
               238284,
               238285,
               238288,
               238289,
               238290,
               238291,
               238292,
               238293,
               238294,
               238295,
               238296,
               238297,
               238298,
               238299,
               238300,
               238301,
               238302,
               238305,
               238306,
               238307,
               238308,
               238309,
               238320,
               238328,
               238329,
               238396,
               238411,
               239033,
               239041,
               239042,
               239043,
               239078,
               239079,
               239080,
               239083,
               239084,
               239085,
               239086,
               239087,
               239088,
               239089,
               239090,
               239091,
               239099,
               239107,
               239108,
               239109,
               239110,
               239111,
               239129,
               239134,
               239136,
               239137,
               239151,
               239159,
               239165,
               239166,
               239167,
               239168,
               239207,
               239238,
               239244,
               239245,
               239261,
               239263,
               239281,
               239282,
               239283,
               239284,
               239285,
               239288,
               239289,
               239290,
               239291,
               239292,
               239293,
               239294,
               239295,
               239296,
               239297,
               239298,
               239299,
               239300,
               239301,
               239302,
               239305,
               239306,
               239307,
               239308,
               239309,
               239320,
               239328,
               239329,
               239396,
               239411,
               263139,
               263140,
               265139,
               265140,
               266139,
               266140,
               267139,
               267140]
            report.add(IsIn(message["paramId"], paramids))
        return report

    def _overall_time_era6(self, message, p):
        report = Report("ERA6 overall time")
        pdtn = message.get("productDefinitionTemplateNumber", int)
        if pdtn in [8,11]:
            timeunit = message.get_long_array("indicatorOfUnitForTimeRange")[0]
            if timeunit == 1:
                dataDate = message.get("dataDate", int)
                dataTime = message.get("dataTime", int)
                forecastTime = message.get("forecastTime", int)
                # we need the most outer loop
                lengthOfTimeRange = message.get_long_array("lengthOfTimeRange")[0]
                yearOfEndOfOverallTimeInterval = message.get("yearOfEndOfOverallTimeInterval", int)
                monthOfEndOfOverallTimeInterval = message.get("monthOfEndOfOverallTimeInterval", int)
                dayOfEndOfOverallTimeInterval = message.get("dayOfEndOfOverallTimeInterval", int)
                hourOfEndOfOverallTimeInterval = message.get("hourOfEndOfOverallTimeInterval", int)
                minuteOfEndOfOverallTimeInterval = message.get("minuteOfEndOfOverallTimeInterval", int)
                secondOfEndOfOverallTimeInterval= message.get("secondOfEndOfOverallTimeInterval", int)
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
                report.add(Report("Time-unit of statistical unit not hours, can't check"))
        else:
            report.add(Report("No time-statistical data !"))
        return report

    def _topd_era6(self, message, p):
        report = Report("typeOfProcessedData")
        topd = message.get("typeOfProcessedData", int)
        marsStream = message.get("stream", str)
        marsType = message.get("type", str)
        if marsStream == "oper" or marsStream == "lwda" or marsStream == "sttd":
            if marsType == "an":
                report.add(Eq(topd, 0))
            elif marsType == "4i" or marsType == "4v":
                report.add(Eq(topd, 2))
            else:
                report.add(Eq(topd, 1))
        elif marsStream == "enda" or marsStream == "elda" or marsStream == "stte":
            if marsType == "an":
                report.add(Eq(topd, 0))
            elif marsType == "4i" or marsType == "4v":
                report.add(Eq(topd, 2))
            else:
                report.add(Eq(topd, 5))
        return report
