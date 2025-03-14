from checker.TiggeBasicChecks import TiggeBasicChecks
from Assert import Le, Eq, Fail, IsIn, AssertTrue, IsMultipleOf
from Report import Report


class Uerra(TiggeBasicChecks):
    def __init__(self, param_file=None, valueflg=False):
        super().__init__(param_file, valueflg=valueflg)
  
    def _basic_checks_2(self, message, p):
        report = Report(f"{__class__.__name__}.{self._basic_checks_2.__name__}")
        report.add(IsIn(message["productionStatusOfProcessedData"], [8, 9]))
        report.add(Le(message["endStep"], 30))
        report.add(IsIn(message["typeOfProcessedData"], [0, 1])) # 0 = analysis, 1 = forecast
        if message["typeOfProcessedData"] == 0:
            report.add(Eq(message["step"], 0))
        else:
            report.add(IsIn(message["step"], [1, 2, 4, 5]) | IsMultipleOf(message["step"], 3))
        return [report]

    def _basic_checks(self, message, p):
        reports = super()._basic_checks(message, p)
        report = Report(f"{__class__.__name__}.{self._basic_checks.__name__}")
        report.add(Le(message["hour"], 24))
        report.add(IsIn(message["step"], [1, 2, 4, 5]) | IsMultipleOf(message["step"], 3))
        return reports + [report]

    def _from_start(self, message, p):
        reports = super()._from_start(message, p)

        min_value, max_value = message.minmax()
        if message["endStep"] == 0:
            report = Report(f"{__class__.__name__}")
            report.add(AssertTrue(bool(min_value == 0) and bool(max_value == 0), "min_value == 0 and max_value == 0"))
            return reports + [report]

        return reports

    def _statistical_process(self, message, p):
        report = Report(f"{__class__.__name__}.{self._statistical_process.__name__}")

        topd = message.get("typeOfProcessedData", int)
        if topd in [0, 1]: # Analysis, Forecast
            report.add(IsIn(message["productDefinitionTemplateNumber"], [8, 11]))
        elif topd == 2: # Analysis and forecast products
            pass
        elif topd in [3, 4]: # Control forecast products, Perturbed forecast products
            report.add(Eq(message["productDefinitionTemplateNumber"], 61))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return [report]

        #  forecastTime for uerra might be all steps decreased by 1 i.e 0,1,2,3,4,5,8,11...29 too many... */
        if message["indicatorOfUnitOfTimeRange"] == 1:
            report.add(Le(message["forecastTime"], 30))

        report.add(Eq(message["timeIncrementBetweenSuccessiveFields"], 0))
        report.add(IsIn(message["endStep"], [1, 2, 4, 5]) | IsMultipleOf(message["endStep"], 3))

        reports = super()._statistical_process(message, p)
        return reports + [report]

    def _point_in_time(self, message, p):
        reports = super()._point_in_time(message, p)

        report= Report(f"{__class__.__name__}.{self._point_in_time.__name__}")
        topd = message.get("typeOfProcessedData", int)
        if topd in [0, 1]: # Analysis, Forecast
            report.add(IsIn(message["productDefinitionTemplateNumber"], [0, 1]))
        elif topd == 2: # Analysis and forecast products
            pass
        elif topd == 3: # Control forecast products 
            report.add(Eq(message["productDefinitionTemplateNumber"], 1))
        elif topd == 4: # Perturbed forecast products
            # Is there always cf in tigge global datasets??
            report.add(Le(message["perturbationNumber"], message["numberOfForecastsInEnsemble"] - 1))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))

        if(message["indicatorOfUnitOfTimeRange"] == 1): #hourly
            report.add(IsIn(message["forecastTime"], [1, 2, 4, 5]) | IsMultipleOf(message["forecastTime"], 3))

        return reports + [report]

    def _pressure_level(self, message, p):
        report = Report(f"{__class__.__name__}.{self._pressure_level.__name__}")
        levels = [1000, 975, 950, 925, 900, 875, 850, 825, 800, 750, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 10]
        report.add(IsIn(message["level"], levels, 'invalid pressure level'))
        return [report]

    def _height_level(self, message, p):
        report = Report(f"{__class__.__name__}.{self._height_level.__name__}")
        levels = [15, 30, 50, 75, 100, 150, 200, 250, 300, 400, 500]
        report.add(IsIn(message["level"], levels, 'invalid height level'))
        return [report]
