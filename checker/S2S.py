from Assert import Le, Ne, Eq, Fail, AssertTrue, IsIn
from Report import Report
from checker.TiggeBasicChecks import TiggeBasicChecks


class S2S(TiggeBasicChecks):
    def __init__(self, param_file=None):
        super().__init__(param_file)

    def _from_start(self, message, p):
        reports = super()._from_start(message, p)
        if message.get("endStep") != 0:
            reports += self._check_range(message, p)
        return reports

    def _point_in_time(self, message, p):
        reports = super()._point_in_time(message, p)

        checks = Report()
        topd = message.get("typeOfProcessedData")
        if topd in [0, 1]: # Analysis, Forecast
            if message.get("productDefinitionTemplateNumber") == 1:
                checks.add(Ne(message, "numberOfForecastsInEnsemble", 0))
                checks.add(Le(message, "perturbationNumber", message.get("numberOfForecastsInEnsemble")))
        elif topd == 2: # Analysis and forecast products
            pass
        elif topd == 3: # Control forecast products 
            checks.add(Eq(message, "productDefinitionTemplateNumber", 1))
        elif topd == 4: # Perturbed forecast products
            checks.add(Eq(message, "productDefinitionTemplateNumber", 1))
            pn = message.get("perturbationNumber")
            nofe = message.get("numberOfForecastsInEnsemble")
            checks.add(AssertTrue(pn == nofe - 1, "perturbationNumber == numberOfForecastsInEnsemble - 1"))
        else:
            checks.add(Fail("Unsupported typeOfProcessedData %ld" % message.get("typeOfProcessedData")))

        if message.get("indicatorOfUnitOfTimeRange") == 11:
            # Six hourly is OK
            pass
        else:
            checks.add(Eq(message, "indicatorOfUnitOfTimeRange", 1))
            checks.add(AssertTrue(message.get("forecastTime") % 6 == 0, "forecastTime % 6 == 0"))

        report = self._make_sub_report(__class__.__name__, checks)
        report.add(checks)

        return reports + [report]

    def _pressure_level(self, message, p):
        checks = Report()
        levels = [1000, 925, 850, 700, 500, 300, 200, 100, 50, 10]
        checks.add(IsIn(message, 'level', levels, 'invalid pressure level'))
        return [checks]
