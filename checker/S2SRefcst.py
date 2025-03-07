from Assert import Le, Ne, Eq, Fail, AssertTrue
from Report import Report
from checker.TiggeBasicChecks import TiggeBasicChecks


class S2SRefcst(TiggeBasicChecks):
    def __init__(self, param_file=None):
        super().__init__(param_file)

    # not registered in the lookup table
    def _statistical_process(self, message, p):
        report = Report()

        topd = message.get("typeOfProcessedData")

        if topd in [0, 1, 2]: # Analysis, Forecast, Analysis and forecast products
            pass
        elif topd in [3, 4]: # Control forecast products, Perturbed forecast products
            report.add(Eq(message, "productDefinitionTemplateNumber", 61))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {message.get('typeOfProcessedData')}"))
            return [report]

        if message.get("indicatorOfUnitOfTimeRange") == 11: # six hours
            # Six hourly is OK
            pass
        else:
            report.add(Eq(message, "indicatorOfUnitOfTimeRange", 1))
            report.add(AssertTrue(message.get("forecastTime") % 6 == 0, "forecastTime % 6 == 0"))

        report.add(Eq(message, "timeIncrementBetweenSuccessiveFields", 0))
        report.add(AssertTrue(message.get("endStep") % 6 == 0, "endStep % 6 == 0")) # Every six hours

        reports = super()._statistical_process(message, p)
        return reports + [report]

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
            checks.add(Eq(message, "productDefinitionTemplateNumber", 60))
        elif topd == 4: # Perturbed forecast products
            checks.add(Eq(message, "productDefinitionTemplateNumber", 60))
            pn = message.get("perturbationNumber")
            nofe = message.get("numberOfForecastsInEnsemble")
            checks.add(AssertTrue(pn < nofe, "perturbationNumber < numberOfForecastsInEnsemble"))
        else:
            checks.add(Fail("Unsupported typeOfProcessedData %ld" % message.get("typeOfProcessedData")))

        if message.get("indicatorOfUnitOfTimeRange") == 11:
            # Six hourly is OK
            pass
        else:
            checks.add(Eq(message, "indicatorOfUnitOfTimeRange", 1))
            checks.add(AssertTrue(message.get("forecastTime") % 6 == 0, "forecastTime % 6 == 0"))

        return reports + [checks]
