from Assert import IsIn, Eq, IsMultipleOf
from Report import Report
from checker.Uerra import Uerra


class Crra(Uerra):
    def __init__(self, param_file=None, valueflg=False):
        super().__init__(param_file, valueflg=valueflg)

    def basic_checks_2(self, message, p) -> Report:
        report = Report("Crra Basic Checks")
        report.add(IsIn(message["productionStatusOfProcessedData"], [10, 11]))
        report.add(IsIn(message["typeOfProcessedData"], [0, 1])) # 0 = analysis , 1 = forecast
        if message["typeOfProcessedData"] == 0:
            report.add(Eq(message["step"], 0))
        else:
            report.add(IsIn(message["step"], [1, 2, 4, 5]) | IsMultipleOf(message["step"], 3))
        return report

    def _pressure_level(self, message, p) -> Report:
        report = Report("Crra Pressure Level")
        levels = [1000, 975, 950, 925, 900, 875, 850, 825, 800, 750, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 10, 7, 5, 3, 2, 1]
        report.add(IsIn(message["level"], levels, 'invalid pressure level'))
        return report
