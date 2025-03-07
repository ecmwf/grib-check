from checker.TiggeBasicChecks import TiggeBasicChecks
from Assert import Le, Ne, Eq, Fail, AssertTrue, DBL_EQUAL
from Report import Report
import logging
import math


class Tigge(TiggeBasicChecks):
    def __init__( self, param_file=None):
        self.logger = logging.getLogger(__class__.__name__)
        super().__init__(param_file)

    # not registered in the lookup table
    def _statistical_process(self, message, p):
        report = Report(f"{__class__.__name__}.statistical_process")

        topd = message.get("typeOfProcessedData", int)

        if topd in [0, 1, 2]: # Analysis, Forecast, Analysis and forecast products
            pass
        elif topd in [3, 4]: # Control forecast products, Perturbed forecast products
            report.add(Eq(message, "productDefinitionTemplateNumber", 11))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
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
        super_reports = super()._point_in_time(message, p)

        checks = Report(__class__.__name__)
        topd = message.get("typeOfProcessedData", int)
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
            checks.add(AssertTrue(pn < nofe - 1, "perturbationNumber == numberOfForecastsInEnsemble - 1"))
        else:
            checks.add(Fail(f"Unsupported typeOfProcessedData {topd}"))

        return super_reports + [checks]

    def _height_level(self, message, p):
        checks = Report()
        checks.add(Fail("Not implemented: dummy height_level()"))
        return [checks]
