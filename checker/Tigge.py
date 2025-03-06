from checker.TiggeBasicChecks import TiggeBasicChecks
from Assert import Le, Ne, Eq, Fail, AssertTrue
from Report import Report
import logging


class Tigge(TiggeBasicChecks):
    def __init__( self, param_file=None):
        self.logger = logging.getLogger(__class__.__name__)
        super().__init__(param_file)

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
            checks.add(AssertTrue(pn < nofe - 1, "perturbationNumber == numberOfForecastsInEnsemble - 1"))

        report = self._make_sub_report(__class__.__name__, checks)
        report.add(checks)

        return super_reports + [report]

    def _height_level(self, message, p):
        checks = Report()
        checks.add(Fail("Not implemented: dummy height_level()"))
        return [checks]
