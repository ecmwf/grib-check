from checker.Wmo import Wmo
from Assert import Le, Lt, Ne, Eq, Fail, IsIn, IsMultipleOf
from Report import Report
import logging


class DestinE(Wmo):
    def __init__( self, lookup_table, valueflg=False):
        super().__init__(lookup_table, valueflg=valueflg)
        self.register_checks({
            "destine_limits": self._destine_limits
        })

    # Reuse / override checks
    def _point_in_time(self, message, p) -> Report:
        report = Report("Point In Time (DestinE)")
        report.add(IsMultipleOf(message["step"], 3))
        return super()._point_in_time(message, p).add(report)

    # Create new checks
    def _destine_limits(self, message, p) -> Report:
        report = Report("DestinE Limits")
        report.add(Le(message["step"], 30))
        report.add(IsIn(message["forecastTime"], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        report.add(IsIn(message["indicatorOfUnitOfTimeRange"], [0, 1]))
        report.add(IsIn(message["timeIncrementBetweenSuccessiveFields"], [0, 1]))
        return report


