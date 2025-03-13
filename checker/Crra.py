from Assert import IsIn, Eq, AssertTrue
from Report import Report
from checker.Uerra import Uerra


class Crra(Uerra):
    def __init__(self, param_file=None, valueflg=False):
        super().__init__(param_file, valueflg=valueflg)

    def basic_checks_2(self, message, p):
        report = Report()
        report.add(IsIn(message, "productionStatusOfProcessedData", [10, 11]))
         # 0 = analysis , 1 = forecast
        report.add(IsIn(message, "typeOfProcessedData", [0, 1]))
        if message.get("typeOfProcessedData") == 0:
            report.add(Eq(message, "step", 0))
        else:
            report.add(IsIn(message, "step", [1, 2, 4, 5]) or AssertTrue(message.get("step") % 3 == 0, "step % 3 == 0"))
        return [report]

    def _pressure_level(self, message, p):
        checks = Report()
        levels = [1000, 975, 950, 925, 900, 875, 850, 825, 800, 750, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 10, 7, 5, 3, 2, 1]
        checks.add(IsIn(message, 'level', levels, 'invalid pressure level'))
        return [checks]
