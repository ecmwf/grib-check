from CheckEngine import CheckEngine
from LookupTable import SimpleLookupTable
from Grib import Grib
from Test import Test, TiggeTest
from Message import Message
from Assert import Le, Ne, Eq, Exists, Missing
from Report import Report


class TiggeChecker(CheckEngine):
    def __init__(
        self,
        valueflg=False,
        warnflg=False,
        verbosity=3,
    ):
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

        parameters = SimpleLookupTable("TiggeParameters.json")
        super().__init__(tests=parameters, valueflg=valueflg, warnflg=warnflg)

    def _create_test(self, message: Message, parameters: dict) -> Test:
        assert parameters is not None
        return TiggeTest(message, parameters, self.__check_map)


    def __daily_average(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy daily_average()")
        return (False, report)

    def __from_start(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy from_start()")
        return (False, report)

    def __point_in_time(self, message, p):
        report = Report()
        topd = message.get("typeOfProcessedData", int)

        results = list()
        if topd == 0: # Analysis
            if message.get("productDefinitionTemplateNumber") == 1:
                results.append(Ne(message, "numberOfForecastsInEnsemble", 0, 'ne(h,"numberOfForecastsInEnsemble",0)').result())
                results.append(Le(message, "perturbationNumber", message.get("numberOfForecastsInEnsemble", int), 'le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble"))').result())
        elif topd == 1: # Forecast
            if message.get("productDefinitionTemplateNumber") == 1:
                results.append(Ne(message, "numberOfForecastsInEnsemble", 0, 'ne(h,"numberOfForecastsInEnsemble",0)').result())
                results.append(Le(message, "perturbationNumber", message.get("numberOfForecastsInEnsemble", int), 'le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble"))').result())
        elif topd == 2: # Analysis and forecast products
            results.append(Eq(message, "productDefinitionTemplateNumber", 0, 'eq(h,"productDefinitionTemplateNumber",0)').result())
            results.append(Eq(message, "perturbationNumber", 0, 'eq(h,"perturbationNumber",0)').result())
        elif topd == 3: # Control forecast products 
            results.append(Ne(message, "numberOfForecastsInEnsemble", 0, 'ne(h,"numberOfForecastsInEnsemble",0)').result())
        elif topd == 4: # Perturbed forecast products
            results.append(Ne(message, "perturbationNumber", 0, 'ne(h,"perturbationNumber",0)').result())
            results.append(Ne(message, "numberOfForecastsInEnsemble", 0, 'ne(h,"numberOfForecastsInEnsemble",0)').result())
        else:
            results.append((False, "Unsupported typeOfProcessedData %ld" % message.get("typeOfProcessedData", int)))


        [report.add(msg) for _, msg in results]
        evals = [eval for eval, _ in results]
        return (all(evals), report)

    def __given_thickness(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy given_thickness()")
        return (False, report)

    def __has_bitmap(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy has_bitmap()")
        return (False, report)

    def __has_soil_layer(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy has_soil_layer()")
        return (False, report)

    def __has_soil_level(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy has_soil_level()")
        return (False, report)

    def __height_level(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy height_level()")
        return (False, report)

    def __given_level(self, message, p):
        assertion = [
            Ne(message, "typeOfFirstFixedSurface", 255, 'ne(h,"typeOfFirstFixedSurface",255)'),
            Exists(message, "scaleFactorOfFirstFixedSurface", 'missing(h,"scaleFactorOfFirstFixedSurface")'),
            Exists(message, "scaledValueOfFirstFixedSurface", 'missing(h,"scaledValueOfFirstFixedSurface")'),
            Eq(message, "typeOfSecondFixedSurface", 255, 'eq(h,"typeOfSecondFixedSurface",103)'),
            Missing(message, "scaleFactorOfSecondFixedSurface", 'missing(h,"scaleFactorOfSecondFixedSurface")'),
            Missing(message, "scaledValueOfSecondFixedSurface", 'missing(h,"scaledValueOfSecondFixedSurface")'),
        ]

        report = Report()
        for a in assertion:
            report.add(a.__str__())

        return (all([a.evaluate() for a in assertion]), report)

    def __potential_temperature_level(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy potential_temperature_level()")
        return (False, report)

    def __potential_vorticity_level(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy potential_vorticity_level()")
        return (False, report)

    def __predefined_level(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy predefined_level()")
        return (False, report)

    def __predefined_thickness(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy predefined_thickness()")
        return (False, report)

    def __pressure_level(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy pressure_level()")
        return (False, report)

    def __resolution_s2s(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy resolution_s2s()")
        return (False, report)

    def __resolution_s2s_ocean(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy resolution_s2s_ocean()")
        return (False, report)

    def __since_prev_pp(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy since_prev_pp()")
        return (False, report)

    def __six_hourly(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy six_hourly()")
        return (False, report)

    def __three_hourly(self, handle, p):
        report = Report()
        report.add("Not implemented: dummy three_hourly()")
        return (False, report)
