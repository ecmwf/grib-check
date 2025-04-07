from checker.TiggeBasicChecks import TiggeBasicChecks
from Assert import Le, Lt, Ne, Eq, Fail, IsIn, IsMultipleOf
from Report import Report
import logging


class Tigge(TiggeBasicChecks):
    def __init__( self, param_file=None, valueflg=False):
        self.logger = logging.getLogger(__class__.__name__)
        super().__init__(param_file, valueflg=valueflg)

    def _basic_checks(self, message, p):
        report = Report("Tigge Basic Checks")
        # Only 00, 06 12 and 18 Cycle OK 
        report.add(IsIn(message["hour"], [0, 6, 12, 18]))
        report.add(IsIn(message["productionStatusOfProcessedData"], [4, 5]))
        report.add(Le(message["endStep"], 30*24))
        report.add(IsMultipleOf(message["step"], 6))
        return report

    # not registered in the lookup table
    def _statistical_process(self, message, p) -> Report:
        report = Report("Tigge Statistical Process")

        topd = message.get("typeOfProcessedData", int)

        if topd in [0, 1, 2]: # Analysis, Forecast, Analysis and forecast products
            pass
        elif topd in [3, 4]: # Control forecast products, Perturbed forecast products
            report.add(Eq(message["productDefinitionTemplateNumber"], 11))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return report

        if message.get("indicatorOfUnitOfTimeRange") == 11: # six hours
            # Six hourly is OK
            pass
        else:
            report.add(Eq(message["indicatorOfUnitOfTimeRange"], 1))
            report.add(IsMultipleOf(message["forecastTime"], 6))

        report.add(Eq(message["timeIncrementBetweenSuccessiveFields"], 0))
        report.add(IsMultipleOf(message["endStep"], 6))

        return super()._statistical_process(message, p).add(report)

    def _from_start(self, message, p) -> Report:
        report = Report("Tigge From Start")
        if message.get("endStep") != 0:
            report.add(self._check_range(message, p))

        return super()._statistical_process(message, p).add(report)

    def _point_in_time(self, message, p) -> Report:
        report = Report("Tigge Point in Time")

        topd = message.get("typeOfProcessedData", int)
        if topd in [0, 1]: # Analysis, Forecast
            if message.get("productDefinitionTemplateNumber") == 1:
                report.add(Ne(message["numberOfForecastsInEnsemble"], 0, f"topd = {topd}"))
                report.add(Le(message["perturbationNumber"], message.get("numberOfForecastsInEnsemble"), f"topd = {topd}"))
        elif topd == 2: # Analysis and forecast products
            pass
        elif topd == 3: # Control forecast products 
            report.add(Eq(message["productDefinitionTemplateNumber"], 1, f"topd = {topd}"))
        elif topd == 4: # Perturbed forecast products
            report.add(Eq(message["productDefinitionTemplateNumber"], 1, f"topd = {topd}"))
            report.add(Le(message["perturbationNumber"], message["numberOfForecastsInEnsemble"] - 1, f"topd = {topd}"))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))

        return super()._statistical_process(message, p).add(report)

    def _height_level(self, message, p) -> Report:
        report = Report("Tigge Height Level")
        report.add(Fail("Not implemented: dummy height_level()"))
        return report
