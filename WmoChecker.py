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
        good=None,
        bad=None,
    ):
        check_map = {
            "product_definition_template_number": self.__product_definition_template_number,
            "derived_forecast": self.__derived_forecast
        }
        parameters = IndexedLookupTable("WmoParameters.json")
        super().__init__(tests=parameters, valueflg=valueflg, warnflg=warnflg, good=good, bad=bad, check_map=check_map)

        self.__last_n = 0
        self.__values = None

        self.__filename = ""
        self.__error = 0
        self.__warning = 0
        self.__field = 0
        self.__param = "unknown"


    def _create_test(self, message: Message, parameters: dict) -> Test:
        return WmoTest(message, parameters, self._check_map)

    def __product_definition_template_number(self, handle, p):
        print("dummy product_definition_template_number()")
        # TODO: Implement this method

    def __derived_forecast(self, handle, p):
        print("dummy derived_forecast()")
        # TODO: Implement this method
