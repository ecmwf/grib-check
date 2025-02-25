from CheckEngine import CheckEngine
from Grib import Grib
from Test import Test, TiggeTest
from Message import Message
from Assert import Le, Ne, Eq, Exists, Missing
from Report import Report
from TiggeChecker import TiggeChecker


class Uerra(TiggeChecker):
    def __init__(
        self,
        valueflg=False,
        warnflg=False,
        verbosity=3,
    ):

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


        if topd == 0: # Analysis
            # CHECK('eq(h,"productDefinitionTemplateNumber",0) or eq(h,"productDefinitionTemplateNumber",1)', eq(h,"productDefinitionTemplateNumber",0) or eq(h,"productDefinitionTemplateNumber",1))

        elif topd == 1: # Forecast
            CHECK('eq(h,"productDefinitionTemplateNumber",0) or eq(h,"productDefinitionTemplateNumber",1)', eq(h,"productDefinitionTemplateNumber",0) or eq(h,"productDefinitionTemplateNumber",1))
        elif topd == 2: # Analysis and forecast products
            pass
        elif topd == 3: # Control forecast products 
            CHECK('eq(h,"productDefinitionTemplateNumber",1)', eq(h,"productDefinitionTemplateNumber",1))
        elif topd == 4: # Perturbed forecast products
            # Is there always cf in tigge global datasets??
            CHECK('le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble")-1)', le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble")-1))
        else:
            print("Unsupported typeOfProcessedData %ld" % get(h,"typeOfProcessedData"))
            CHECK('0', 0)

        if(get(h,"indicatorOfUnitOfTimeRange") == 1): #hourly
            fc1 = Eq(message, "forecastTime", 1)
            fc2 = Eq(message, "forecastTime", 2)
            fc4 = Eq(message, "forecastTime", 4)
            fc5 = Eq(message, "forecastTime", 5)
            fc3 = (message.get("forecastTime") % 3) == 0

            results.append((fc1 or fc2 or fc4 or fc5 or fc3).result(), 'eq(h,"forecastTime",1) or eq(h,"forecastTime",2) or eq(h,"forecastTime",4) or eq(h,"forecastTime",5) or (get(h,"forecastTime") % 3) == 0')





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
