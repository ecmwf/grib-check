from CheckEngine import CheckEngine
from IndexedLookupTable import IndexedLookupTable
from Grib import Grib
from Test import Test, WmoTest
from Message import Message


class WmoChecker(CheckEngine):
    def __init__(
        self,
        valueflg=False,
        warnflg=False,
        verbosity=0,
    ):
        self.__check_map = {
            "product_definition_template_number": self.__product_definition_template_number,
            "derived_forecast": self.__derived_forecast
        }
        parameters = IndexedLookupTable("WmoParameters.json")
        super().__init__(tests=parameters, valueflg=valueflg, warnflg=warnflg)

    def _create_test(self, message: Message, parameters: dict) -> Test:
        return WmoTest(message, parameters, self.__check_map)

    def __product_definition_template_number(self, handle, p):
        msgs = ["Not implemented: dummy product_definition_template_number()"]
        return [True, msgs]

    def __derived_forecast(self, handle, p):
        msg = ["Not implemented: dummy derived_forecast()"]
        return [True, msg]
