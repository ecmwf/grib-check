from checker.TiggeBasicChecks import TiggeBasicChecks
from Assert import Le, Eq, Fail, IsIn, AssertTrue
from Report import Report


class Uerra(TiggeBasicChecks):
    def __init__(self, param_file=None):
        super().__init__(param_file)
    
    def _from_start(self, message, p):
        reports = super()._from_start(message, p)

        min_value, max_value = message.minmax()
        if message.get("endStep") == 0:
            checks = Report()
            checks.add(AssertTrue(min_value == 0 and max_value == 0, "min_value == 0 and max_value == 0"))
            report = self._make_sub_report(__class__.__name__, checks)
            return reports + [report]

        return reports

    def _point_in_time(self, message, p):
        reports = super()._point_in_time(message, p)

        checks= Report()
        topd = message.get("typeOfProcessedData", int)
        if topd == 0: # Analysis
            pdtn0 = Eq(message, "productDefinitionTemplateNumber", 0)
            pdtn1 = Eq(message, "productDefinitionTemplateNumber", 1)
            checks.add((pdtn0 or pdtn1).result())
        elif topd == 1: # Forecast
            pdtn0 = Eq(message, "productDefinitionTemplateNumber", 0)
            pdtn1 = Eq(message, "productDefinitionTemplateNumber", 1)
            checks.add((pdtn0 or pdtn1).result())
        elif topd == 2: # Analysis and forecast products
            pass
        elif topd == 3: # Control forecast products 
            checks.add(Eq(message, "productDefinitionTemplateNumber", 1))
        elif topd == 4: # Perturbed forecast products
            # Is there always cf in tigge global datasets??
            checks.add(Le(message, "perturbationNumber", message.get("numberOfForecastsInEnsemble") - 1))
        else:
            checks.add(Fail(f"Unsupported typeOfProcessedData {message.get("typeOfProcessedData")}"))

        if(message.get("indicatorOfUnitOfTimeRange") == 1): #hourly
            ft1 = Eq(message, "forecastTime", 1)
            ft2 = Eq(message, "forecastTime", 2)
            ft4 = Eq(message, "forecastTime", 4)
            ft5 = Eq(message, "forecastTime", 5)
            ft3 = (message.get("forecastTime") % 3) == 0
            checks.add(ft1 or ft2 or ft4 or ft5 or ft3)

        report = self._make_sub_report(__class__.__name__, checks)
        return reports + [report]


    def _pressure_level(self, message, p):
        checks = Report()
        levels = [1000, 975, 950, 925, 900, 875, 850, 825, 800, 750, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 10]
        checks.add(IsIn(message, 'level', levels, 'invalid pressure level'))
        return checks


    def _height_level(self, message, p):
        checks = Report()
        levels = [15, 30, 50, 75, 100, 150, 200, 250, 300, 400, 500]
        checks.add(IsIn(message, "level", levels, 'invalid height level'))
        return [checks]
