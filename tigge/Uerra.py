from CheckEngine import CheckEngine
from Grib import Grib
from Test import Test, TiggeTest
from Message import Message
from Assert import Le, Ne, Eq, Exists, Missing, Fail
from Report import Report
from TiggeChecker import TiggeChecker


class Uerra(TiggeChecker):
    def __init__(
        self,
        valueflg=False,
        warnflg=False,
        verbosity=3,
    ):
        super().__init__(valueflg, warnflg, verbosity)

    # def __daily_average(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy daily_average()")
    #     return (False, report)
    #
    # def __from_start(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy from_start()")
    #     return (False, report)

    def __point_in_time(self, message, p):
        report = Report()
        results = list()

        topd = message.get("typeOfProcessedData", int)
        if topd == 0: # Analysis
            pdtn0 = Eq(message, "productDefinitionTemplateNumber", 0)
            pdtn1 = Eq(message, "productDefinitionTemplateNumber", 1)
            results.append((pdtn0 or pdtn1).result())
        elif topd == 1: # Forecast
            pdtn0 = Eq(message, "productDefinitionTemplateNumber", 0)
            pdtn1 = Eq(message, "productDefinitionTemplateNumber", 1)
            results.append((pdtn0 or pdtn1).result())
        elif topd == 2: # Analysis and forecast products
            pass
        elif topd == 3: # Control forecast products 
            results.append(Eq(message, "productDefinitionTemplateNumber", 1))
        elif topd == 4: # Perturbed forecast products
            # Is there always cf in tigge global datasets??
            results.append(Le(message, "perturbationNumber", message.get("numberOfForecastsInEnsemble") - 1))
        else:
            results.append(Fail(message, f"Unsupported typeOfProcessedData {message.get("typeOfProcessedData")}"))

        if(message.get("indicatorOfUnitOfTimeRange") == 1): #hourly
            ft1 = Eq(message, "forecastTime", 1)
            ft2 = Eq(message, "forecastTime", 2)
            ft4 = Eq(message, "forecastTime", 4)
            ft5 = Eq(message, "forecastTime", 5)
            ft3 = (message.get("forecastTime") % 3) == 0
            results.append((ft1 or ft2 or ft4 or ft5 or ft3).result())

        [report.add(msg) for _, msg in results]
        evals = [eval for eval, _ in results]
        return (all(evals), report)

    # def __given_thickness(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy given_thickness()")
    #     return (False, report)
    #
    # def __has_bitmap(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy has_bitmap()")
    #     return (False, report)
    #
    # def __has_soil_layer(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy has_soil_layer()")
    #     return (False, report)
    #
    # def __has_soil_level(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy has_soil_level()")
    #     return (False, report)
    #
    # def __height_level(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy height_level()")
    #     return (False, report)
    #
    # def __given_level(self, message, p):
    #     assertion = [
    #         Ne(message, "typeOfFirstFixedSurface", 255, 'ne(h,"typeOfFirstFixedSurface",255)'),
    #         Exists(message, "scaleFactorOfFirstFixedSurface", 'missing(h,"scaleFactorOfFirstFixedSurface")'),
    #         Exists(message, "scaledValueOfFirstFixedSurface", 'missing(h,"scaledValueOfFirstFixedSurface")'),
    #         Eq(message, "typeOfSecondFixedSurface", 255, 'eq(h,"typeOfSecondFixedSurface",103)'),
    #         Missing(message, "scaleFactorOfSecondFixedSurface", 'missing(h,"scaleFactorOfSecondFixedSurface")'),
    #         Missing(message, "scaledValueOfSecondFixedSurface", 'missing(h,"scaledValueOfSecondFixedSurface")'),
    #     ]
    #
    #     report = Report()
    #     for a in assertion:
    #         report.add(a.__str__())
    #
    #     return (all([a.evaluate() for a in assertion]), report)
    #
    # def __potential_temperature_level(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy potential_temperature_level()")
    #     return (False, report)
    #
    # def __potential_vorticity_level(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy potential_vorticity_level()")
    #     return (False, report)
    #
    # def __predefined_level(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy predefined_level()")
    #     return (False, report)
    #
    # def __predefined_thickness(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy predefined_thickness()")
    #     return (False, report)
    #
    # def __pressure_level(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy pressure_level()")
    #     return (False, report)
    #
    # def __resolution_s2s(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy resolution_s2s()")
    #     return (False, report)
    #
    # def __resolution_s2s_ocean(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy resolution_s2s_ocean()")
    #     return (False, report)
    #
    # def __since_prev_pp(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy since_prev_pp()")
    #     return (False, report)
    #
    # def __six_hourly(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy six_hourly()")
    #     return (False, report)
    #
    # def __three_hourly(self, handle, p):
    #     report = Report()
    #     report.add("Not implemented: dummy three_hourly()")
    #     return (False, report)
