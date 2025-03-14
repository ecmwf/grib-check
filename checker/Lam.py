from Assert import Le, Ne, Eq, Fail, AssertTrue, IsIn, IsMultipleOf
from Report import Report
from checker.TiggeBasicChecks import TiggeBasicChecks


class Lam(TiggeBasicChecks):
    def __init__(self, param_file=None, valueflg=False):
        super().__init__(param_file, valueflg=valueflg)

    def _basic_checks(self, message, p):
        reports = super()._basic_checks(message, p)
        report = Report(f"{__class__.__name__}._basic_checks")
        report.add(IsIn(message, "hour", [0, 3, 6, 9, 12, 15, 18, 21]))
        report.add(IsIn(message, "productionStatusOfProcessedData", [4, 5]))
        report.add(Le(message, "endStep", 30 * 24))
        report.add(IsMultipleOf(message, "step", 3))
        return reports + [report]

    # not registered in the lookup table
    def _statistical_process(self, message, p):
        report = Report(f"{__class__.__name__}.statistical_process")

        topd = message.get("typeOfProcessedData", int)

        if topd in [0, 1, 2] : # Analysis, Forecast, Analysis and forecast products
            pass
        elif topd in [3, 4]: # Control forecast products
            report.add(Eq(message, "productDefinitionTemplateNumber", 11))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return [report]

        if message.get("indicatorOfUnitOfTimeRange") == 10: # three hours
            # Three hourly is OK
            pass
        else:
            report.add(Eq(message, "indicatorOfUnitOfTimeRange", 1))
            report.add(AssertTrue(message.get("forecastTime") % 3 == 0, "forecastTime % 3 == 0"))

        report.add(Eq(message, "timeIncrementBetweenSuccessiveFields", 0))
        report.add(AssertTrue(message.get("endStep") % 3 == 0, "endStep % 3 == 0")) # Every three hours

        reports = super()._statistical_process(message, p)
        return reports + [report]

    def _from_start(self, message, p):
        reports = super()._from_start(message, p)
        if message.get("endStep") != 0:
            reports += self._check_range(message, p)

        return reports

    def _point_in_time(self, message, p):
        super_reports = super()._point_in_time(message, p)

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

        if message.get("indicatorOfUnitOfTimeRange") == 10:
            # Three hourly is OK
            pass
        else:
            checks.add(Eq(message, "indicatorOfUnitOfTimeRange", 1))
            checks.add(AssertTrue(message.get("forecastTime") % 3 == 0, "forecastTime % 3 == 0"))

        return super_reports + [checks]
