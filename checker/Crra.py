from Assert import IsIn
from Report import Report
from checker.Uerra import Uerra


class Crra(Uerra):
    def __init__(self, param_file=None):
        super().__init__(param_file)

    def _pressure_level(self, message, p):
        checks = Report()
        levels = [1000, 975, 950, 925, 900, 875, 850, 825, 800, 750, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 10, 7, 5, 3, 2, 1]
        checks.add(IsIn(message, 'level', levels, 'invalid pressure level'))
        return checks
