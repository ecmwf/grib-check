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

        # self.__valueflg = valueflg
        # self.__warnflg = warnflg

    # def __product_definition_template_number(self, handle, p, min_value, max_value):
    def __product_definition_template_number(self, handle, p):
        print("dummy product_definition_template_number()")
        # do some crazy stuff here
        # if stream in [enfo]
        #     if type in [fcmean,…]
        #         Ex 1 should have 11
        #         if type in [taem,taes,….]
        #         Ex 2,3 should have 12
        #     else
        #         Ex 4, should have 1
        pass

    def __derived_forecast(self, handle, p):
    # def __derived_forecast(self, handle, p, min_value, max_value):
        print("dummy derived_forecast()")
        # do some crazy stuff
        # if type in [taem]
        #     Ex 2 should have 0
        # if type in [taes]
        #     Ex 3 should have 4
        pass
