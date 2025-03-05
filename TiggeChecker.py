from CheckEngine import CheckEngine
from LookupTable import SimpleLookupTable
from Grib import Grib
from Test import Test, TiggeTest
from Message import Message
from Assert import Le, Ne, Eq, Exists, Missing, Fail
from Report import Report
import logging


class TiggeChecker(CheckEngine):
    def __init__(
        self,
        valueflg=False,
        warnflg=False,
        verbosity=3,
        param_file="TiggeParameters.json",
    ):
        self.logger = logging.getLogger(__class__.__name__)
        self.__verbosity = verbosity
        self.__check_map = {
            "daily_average": self.__daily_average,
            "from_start": self.__from_start,
            "given_level": self.__given_level,
            "given_thickness": self.__given_thickness,
            "has_bitmap": self.__has_bitmap,
            "has_soil_layer": self.__has_soil_layer,
            "has_soil_level": self.__has_soil_level,
            "height_level": self.__height_level,
            "point_in_time": self.__point_in_time,
            "potential_temperature_level": self.__potential_temperature_level,
            "potential_vorticity_level": self.__potential_vorticity_level,
            "predefined_level": self.__predefined_level,
            "predefined_thickness": self.__predefined_thickness,
            "pressure_level": self.__pressure_level,
            "resolution_s2s": self.__resolution_s2s,
            "resolution_s2s_ocean": self.__resolution_s2s_ocean,
            "since_prev_pp": self.__since_prev_pp,
            "six_hourly": self.__six_hourly,
            "three_hourly": self.__three_hourly,
        }

        parameters = SimpleLookupTable(param_file)
        super().__init__(tests=parameters, valueflg=valueflg, warnflg=warnflg)

    def _create_test(self, message: Message, parameters: dict) -> Test:
        assert parameters is not None
        return TiggeTest(message, parameters, self.__check_map)


    def __daily_average(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy daily_average()"))
        return report

    def __from_start(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy from_start()"))
        return report

    def __point_in_time(self, message, p):
        report = Report()
        topd = message.get("typeOfProcessedData", int)

        if topd == 0: # Analysis
            if message.get("productDefinitionTemplateNumber") == 1:
                report.add(Ne(message, "numberOfForecastsInEnsemble", 0, 'ne(h,"numberOfForecastsInEnsemble",0)'))
                report.add(Le(message, "perturbationNumber", message.get("numberOfForecastsInEnsemble", int), 'le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble"))'))
        elif topd == 1: # Forecast
            if message.get("productDefinitionTemplateNumber") == 1:
                report.add(Ne(message, "numberOfForecastsInEnsemble", 0, 'ne(h,"numberOfForecastsInEnsemble",0)'))
                report.add(Le(message, "perturbationNumber", message.get("numberOfForecastsInEnsemble", int), 'le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble"))'))
        elif topd == 2: # Analysis and forecast products
            report.add(Eq(message, "productDefinitionTemplateNumber", 0, 'eq(h,"productDefinitionTemplateNumber",0)'))
            report.add(Eq(message, "perturbationNumber", 0, 'eq(h,"perturbationNumber",0)'))
        elif topd == 3: # Control forecast products 
            report.add(Ne(message, "numberOfForecastsInEnsemble", 0, 'ne(h,"numberOfForecastsInEnsemble",0)'))
        elif topd == 4: # Perturbed forecast products
            report.add(Ne(message, "perturbationNumber", 0, 'ne(h,"perturbationNumber",0)').result())
            report.add(Ne(message, "numberOfForecastsInEnsemble", 0, 'ne(h,"numberOfForecastsInEnsemble",0)'))
        else:
            report.add((False, "Unsupported typeOfProcessedData %ld" % message.get("typeOfProcessedData", int)))

        return report

        # [report.add(msg) for _, msg in results]
        # evals = [eval for eval, _ in results]
        # return (all(evals), report)

    def __given_thickness(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy given_thickness()"))
        return report

    def __has_bitmap(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy has_bitmap()"))
        return report

    def __has_soil_layer(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy has_soil_layer()"))
        return report

    def __has_soil_level(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy has_soil_level()"))
        return report

    def __height_level(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy height_level()"))
        return report

    def __given_level(self, message, p):
        report = Report()
        report.add(Ne(message, "typeOfFirstFixedSurface", 255, 'ne(h,"typeOfFirstFixedSurface",255)'))
        report.add(Exists(message, "scaleFactorOfFirstFixedSurface", 'missing(h,"scaleFactorOfFirstFixedSurface")'))
        report.add(Exists(message, "scaledValueOfFirstFixedSurface", 'missing(h,"scaledValueOfFirstFixedSurface")'))
        report.add(Eq(message, "typeOfSecondFixedSurface", 255, 'eq(h,"typeOfSecondFixedSurface",103)'))
        report.add(Missing(message, "scaleFactorOfSecondFixedSurface", 'missing(h,"scaleFactorOfSecondFixedSurface")'))
        report.add(Missing(message, "scaledValueOfSecondFixedSurface", 'missing(h,"scaledValueOfSecondFixedSurface")'))
        return report

    def __potential_temperature_level(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy potential_temperature_level()"))
        return report

    def __potential_vorticity_level(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy potential_vorticity_level()"))
        return report

    def __predefined_level(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy predefined_level()"))
        return report

    def __predefined_thickness(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy predefined_thickness()"))
        return report

    def __pressure_level(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy pressure_level()"))
        return report

    def __resolution_s2s(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy resolution_s2s()"))
        return report

    def __resolution_s2s_ocean(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy resolution_s2s_ocean()"))
        return report

    def __since_prev_pp(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy since_prev_pp()"))
        return report

    def __six_hourly(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy six_hourly()"))
        return report

    def __three_hourly(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy three_hourly()"))
        return report
