from checker.Wmo import Wmo
from Assert import Le, Lt, Ne, Eq, Fail, IsIn, IsMultipleOf
from Report import Report
import logging


class Destiny(Wmo):
    def __init__( self, lookup_table, valueflg=False):
        super().__init__(lookup_table, valueflg=valueflg)

    def _point_in_time(self, message, p) -> Report:
        report = Report("Point In Time (Destiny)")
        report.add(IsMultipleOf(message["step"], 3))

        return super()._basic_checks(message, p).add(report)

