from CheckEngine import CheckEngine
from LookupTable import SimpleLookupTable
from Test import Test, WmoTest
from Report import Report
from Assert import Fail, Eq
from Message import Message


class WmoChecker(CheckEngine):
    def __init__(
        self,
        param_file="WmoParameters.json",
    ):
        self.__check_map = {
            "basic_checks": self.__basic_checks,
            "product_definition_template_number": self.__product_definition_template_number,
            "derived_forecast": self.__derived_forecast
        }
        parameters = SimpleLookupTable(param_file)
        super().__init__(tests=parameters)

    def _create_test(self, message: Message, parameters: dict) -> Test:
        return WmoTest(message, parameters, self.__check_map)

    def __basic_checks(self, message, data):
        report = Report()
        report.add(Eq(message, "edition", 2))
        sub_report = Report() # Anonymous report
        # sub_report = Report("SUB REPORT") # Named report
        sub_report.add(Eq(message, "centre", 98))
        sub_report.add(Eq(message, "subCentre", 0))

        report.add(sub_report)
        return report

    def __product_definition_template_number(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy product_definition_template_number()"))
        return report

    def __derived_forecast(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy derived_forecast()"))
        return report
