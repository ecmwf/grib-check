from CheckEngine import CheckEngine
from LookupTable import SimpleLookupTable
from Test import Test, TiggeTest
from Message import Message
from Assert import Le, Ne, Eq, Exists, Missing, Fail, Pass, AssertTrue, IsIn
from Report import Report
import logging


class TiggeBasicChecks(CheckEngine):
    def __init__(self, param_file=None):
        self.logger = logging.getLogger(__class__.__name__)
        self.__check_map = {
            "daily_average": self._daily_average,
            "from_start": self._from_start,
            "given_level": self._given_level,
            "given_thickness": self._given_thickness,
            "has_bitmap": self._has_bitmap,
            "has_soil_layer": self._has_soil_layer,
            "has_soil_level": self._has_soil_level,
            "height_level": self._height_level,
            "point_in_time": self._point_in_time,
            "potential_temperature_level": self._potential_temperature_level,
            "potential_vorticity_level": self._potential_vorticity_level,
            "predefined_level": self._predefined_level,
            "predefined_thickness": self._predefined_thickness,
            "pressure_level": self._pressure_level,
            "resolution_s2s": self._resolution_s2s,
            "resolution_s2s_ocean": self._resolution_s2s_ocean,
            "since_prev_pp": self._since_prev_pp,
            "six_hourly": self._six_hourly,
            "three_hourly": self._three_hourly,
        }

        parameters = SimpleLookupTable(param_file if param_file is not None else"checker/TiggeParameters.json")
        super().__init__(tests=parameters)

    def _make_sub_report(self, title, checks):
        report = Report()
        status, _ = checks.summary()
        if status:
            report.add(Pass(title))
        else:
            report.add(Fail(title))
        report.add(checks)
        return report

    def _create_test(self, message: Message, parameters: dict) -> Test:
        assert parameters is not None
        return TiggeTest(message, parameters, self.__check_map)

    # not registered in the lookup table
    def _statistical_process(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy statistical_process()"))
        return [report]

    # not registered in the lookup table
    def _check_range(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy check_range()"))
        return [report]

    # not registered in the lookup table
    def _gaussian_grid(self, message, p):
        report = Report()
        report.add(Fail("Not implemented: dummy gaussian_grid()"))
        return [report]

    # not registered in the lookup table
    def _latlon_grid(self, message, p):
        report = Report()
        report.add(Fail("Not implemented: dummy latlon_grid()"))
        return [report]

    # not registered in the lookup table
    def _check_validity_time(self, message, p):
        report = Report()
        report.add(Fail("Not implemented: dummy check_validity_time()"))
        return [report]

    def _daily_average(self, message, p):
        reports = list()
        report = Report()
        start_step = message.get("startStep")
        end_step = message.get("endStep")
        report.add(AssertTrue(start_step == end_step - 24, "startStep == endStep - 24"))
        min_value, max_value = message.minmax()
        if end_step == 0:
            report.add(AssertTrue(min_value == 0 and max_value() == 0, "min_value == 0 and max_value == 0"))
            pass
        else:
            reports += self._check_range(message, p)

        reports += self._statistical_process(message ,p)
        reports = [report] + reports

        return reports

    def _from_start(self, message, p):
        reports = list()
        checks = Report()
        checks.add(Eq(message, "startStep", 0))

        reports += self._statistical_process(message, p)
        reports = [checks] + reports

        return reports

    def _point_in_time(self, message, p):
        checks = Report()
        topd = message.get("typeOfProcessedData", int)
        if topd in [0, 1]: # Analysis, Forecast
            pass
        elif topd == 2: # Analysis and forecast products
            checks.add(Eq(message, "productDefinitionTemplateNumber", 0))
        elif topd in [3, 4]: # Control forecast products, Perturbed forecast products
            checks.add(Ne(message, "perturbationNumber", 0))
            checks.add(Ne(message, "numberOfForecastsInEnsemble", 0))
        else:
            checks.add(Fail("Unsupported typeOfProcessedData %ld" % message.get("typeOfProcessedData", int)))

        report = self._make_sub_report(__class__.__name__, checks)
        return [report]

    def _given_thickness(self, message, p):
        report = Report()
        report.add(Fail("Not implemented: dummy given_thickness()"))
        return [report]

    def _has_bitmap(self, message, p):
        report = Report()
        report.add(Fail("Not implemented: dummy has_bitmap()"))
        return [report]

    def _has_soil_layer(self, message, p):
        report = Report()
        report.add(AssertTrue(message.get("topLevel") == message.get("bottomLevel") - 1, "topLevel == bottomLevel - 1"))
        report.add(Le(message, "level", 14)) # max in UERRA
        return [report]

    def _has_soil_level(self, message, p):
        report = Report()
        report.add(AssertTrue(message.get("topLevel") == message.get("bottomLevel"), "topLevel == bottomLevel"))
        report.add(Le(message, "level", 14)) # max in UERRA
        return [report]

    def _height_level(self, message, p):
        report = Report()
        return [report]

    def _given_level(self, message, p):
        report = Report()
        report.add(Ne(message, "typeOfFirstFixedSurface", 255))
        report.add(Exists(message, "scaleFactorOfFirstFixedSurface"))
        report.add(Exists(message, "scaledValueOfFirstFixedSurface"))
        report.add(Eq(message, "typeOfSecondFixedSurface", 255))
        report.add(Missing(message, "scaleFactorOfSecondFixedSurface"))
        report.add(Missing(message, "scaledValueOfSecondFixedSurface"))
        return [report]

    def _potential_temperature_level(self, message, p):
        report = Report()
        report.add(Eq(message, 'level', 320, f'invalid potential temperature level {message.get("level")}' ))
        return [report]

    def _potential_vorticity_level(self, message, p):
        report = Report()
        report.add(Eq(message, 'level', 2, f'invalid potential vorticity level {message.get("level")}'))
        return [report]

    def _predefined_level(self, message, p):
        report = Report()
        report.add(Ne(message, "typeOfFirstFixedSurface", 255))
        report.add(Missing(message, "scaleFactorOfFirstFixedSurface"))
        report.add(Missing(message, "scaledValueOfFirstFixedSurface"))
        report.add(Eq(message, "typeOfSecondFixedSurface", 255))
        report.add(Missing(message, "scaleFactorOfSecondFixedSurface"))
        report.add(Missing(message, "scaledValueOfSecondFixedSurface"))
        return [report]

    def _predefined_thickness(self, message, p):
        report = Report()
        report.add(Ne(message, "typeOfFirstFixedSurface", 255))
        report.add(Missing(message, "scaleFactorOfFirstFixedSurface"))
        report.add(Missing(message, "scaledValueOfFirstFixedSurface"))
        report.add(Eq(message, "typeOfSecondFixedSurface", 255))
        report.add(Missing(message, "scaleFactorOfSecondFixedSurface"))
        report.add(Missing(message, "scaledValueOfSecondFixedSurface"))
        return [report]

    def _pressure_level(self, message, p):
        checks = Report()
        levels = [1000, 200, 250, 300, 500, 700, 850, 925, 50]
        checks.add(IsIn(message, 'level', levels, 'invalid pressure level'))
        return [checks]

    def _resolution_s2s(self, message, p):
        report = Report()
        report.add(Eq(message, "iDirectionIncrement", 1500000))
        report.add(Eq(message, "jDirectionIncrement", 1500000))
        return [report]

    def _resolution_s2s_ocean(self, message, p):
        report = Report()
        report.add(Eq(message, "iDirectionIncrement", 1000000))
        report.add(Eq(message, "jDirectionIncrement", 1000000))
        return [report]

    def _since_prev_pp(self, message, p):
        report = Report()
        # statistical_process(h,p,min_value,max_value)
        report.add(Eq(message, "indicatorOfUnitForTimeRange", 1))
        report.add(AssertTrue(message.get("endStep") == message.get("startStep") + message.get("lengthOfTimeRange"), "endStep == startStep + lengthOfTimeRange"))
        # check_range(h,p,min_value,max_value)
        return [report]

    def _six_hourly(self, message, p):
        report = Report()
        # statistical_process(h,p,min_value,max_value);

        if message.get("indicatorOfUnitForTimeRange") == 11:
            report.add(Eq(message, "lengthOfTimeRange", 1))
        else:
            report.add(Eq(message, "lengthOfTimeRange", 6))

        report.add(AssertTrue(message.get("endStep") == message.get("startStep") + 6, "endStep == startStep + 6"))
        # check_range(h,p,min_value,max_value)
        return [report]

    def _three_hourly(self, message, p):
        report = Report()
        # statistical_process(h,p,min_value,max_value)

        if message.get("indicatorOfUnitForTimeRange") == 11:
            report.add(Eq(message, "lengthOfTimeRange", 1))
        else:
            report.add(Eq(message, "lengthOfTimeRange", 3))

        report.add(AssertTrue(message.get("endStep") == message.get("startStep") + 3, "endStep == startStep + 3"))
        # check_range(h,p,min_value,max_value)
        return [report]
