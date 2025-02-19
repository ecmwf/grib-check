from CheckEngine import CheckEngine
from IndexedLookupTable import IndexedLookupTable
from Grib import Grib
from Test import Test, TiggeTest
from Message import Message
from Assert import Ne, Eq, Exists, Missing


class TiggeChecker(CheckEngine):
    def __init__(
        self,
        valueflg=False,
        warnflg=False,
        verbosity=3,
    ):
        self.__verbosity = verbosity
        self.__check_map = {
            "daily_average": self.__daily_average,
            "from_start": self.__from_start,
            "given_level": self.__given_level,
            "given_thickness": self.__given_thickness,
            "has_bitmap": self.__has_bitmap,
            "has_soil_layer": self.__has_soil_layer,
            "has_soil_level": self.__has_soil_level,
            "height_level": self.__height_level,
            "point_in_time": self.__point_in_time,
            "potential_temperature_level": self.__potential_temperature_level,
            "potential_vorticity_level": self.__potential_vorticity_level,
            "predefined_level": self.__predefined_level,
            "predefined_thickness": self.__predefined_thickness,
            "pressure_level": self.__pressure_level,
            "resolution_s2s": self.__resolution_s2s,
            "resolution_s2s_ocean": self.__resolution_s2s_ocean,
            "since_prev_pp": self.__since_prev_pp,
            "six_hourly": self.__six_hourly,
            "three_hourly": self.__three_hourly,
        }

        parameters = IndexedLookupTable("TiggeParameters.json")
        super().__init__(tests=parameters, valueflg=valueflg, warnflg=warnflg)

    def _create_test(self, message: Message, parameters: dict) -> Test:
        assert parameters is not None
        return TiggeTest(message, parameters, self.__check_map)


    def __daily_average(self, handle, p):
        msgs = ["Not implemented: dummy daily_average()"]
        return [False, msgs]

    def __from_start(self, handle, p):
        msgs = ["Not implemented: dummy from_start()"]
        return [False, msgs]

    def __point_in_time(self, handle, p):
        msgs = ["Not implemented: dummy point_in_time()"]
        return [False, msgs]

    def __given_thickness(self, handle, p):
        msgs = ["Not implemented: dummy given_thickness()"]
        return [False, msgs]

    def __has_bitmap(self, handle, p):
        msgs = ["Not implemented: dummy has_bitmap()"]
        return [False, msgs]

    def __has_soil_layer(self, handle, p):
        msgs = ["Not implemented: dummy has_soil_layer()"]
        return [False, msgs]

    def __has_soil_level(self, handle, p):
        msgs = ["Not implemented: dummy has_soil_level()"]
        return [False, msgs]

    def __height_level(self, handle, p):
        msgs = ["Not implemented: dummy height_level()"]
        return [False, msgs]

    def __given_level(self, message, p):
        assertion = [
            Ne(message, "typeOfFirstFixedSurface", 255, 'ne(h,"typeOfFirstFixedSurface",255)'),
            Exists(message, "scaleFactorOfFirstFixedSurface", 'missing(h,"scaleFactorOfFirstFixedSurface")'),
            Exists(message, "scaledValueOfFirstFixedSurface", 'missing(h,"scaledValueOfFirstFixedSurface")'),
            Eq(message, "typeOfFirstFixedSurface", 103, 'eq(h,"typeOfFirstFixedSurface",103)'),
            Missing(message, "scaleFactorOfFirstFixedSurface", 'missing(h,"scaleFactorOfFirstFixedSurface")'),
            Missing(message, "scaledValueOfFirstFixedSurface", 'missing(h,"scaledValueOfFirstFixedSurface")'),
        ]
        if self.__verbosity >= 3:
            msgs = [a.__str__() for a in assertion]
        else:
            msgs = None

        return [all([a.evaluate() for a in assertion]), msgs]

    def __potential_temperature_level(self, handle, p):
        msgs = ["Not implemented: dummy potential_temperature_level()"]
        return [False, msgs]

    def __potential_vorticity_level(self, handle, p):
        msgs = ["Not implemented: dummy potential_vorticity_level()"]
        return [False, msgs]

    def __predefined_level(self, handle, p):
        msgs = ["Not implemented: dummy predefined_level()"]
        return [False, msgs]

    def __predefined_thickness(self, handle, p):
        msgs = ["Not implemented: dummy predefined_thickness()"]
        return [False, msgs]

    def __pressure_level(self, handle, p):
        msgs = ["Not implemented: dummy pressure_level()"]
        return [False, msgs]

    def __resolution_s2s(self, handle, p):
        msgs = ["Not implemented: dummy resolution_s2s()"]
        return [False, msgs]

    def __resolution_s2s_ocean(self, handle, p):
        msgs = ["Not implemented: dummy resolution_s2s_ocean()"]
        return [False, msgs]

    def __since_prev_pp(self, handle, p):
        msgs = ["Not implemented: dummy since_prev_pp()"]
        return [False, msgs]

    def __six_hourly(self, handle, p):
        msgs = ["Not implemented: dummy six_hourly()"]
        return [False, msgs]

    def __three_hourly(self, handle, p):
        msgs = ["Not implemented: dummy three_hourly()"]
        return [False, msgs]
