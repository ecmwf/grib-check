from CheckEngine import CheckEngine
from LookupTable import SimpleLookupTable
from Test import Test, WmoTest
from Report import Report
from Assert import Fail
from Message import Message


class WmoChecker(CheckEngine):
    def __init__(
        self,
        param_file="WmoParameters.json",
    ):
        self.__check_map = {
            "product_definition_template_number": self.__product_definition_template_number,
            "derived_forecast": self.__derived_forecast
        }
        parameters = SimpleLookupTable(param_file)
        super().__init__(tests=parameters)

    def _create_test(self, message: Message, parameters: dict) -> Test:
        return WmoTest(message, parameters, self.__check_map)

    def __product_definition_template_number(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy product_definition_template_number()"))
        return report

    def __derived_forecast(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy derived_forecast()"))
        return report
