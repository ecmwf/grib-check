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
    ):
        check_map = {
            # "daily_average": self.__daily_average,
            # "from_start": self.__from_start,
            "given_level": self.__given_level,
            # "given_thickness": self.__given_thickness,
            # "has_bitmap": self.__has_bitmap,
            # "has_soil_layer": self.__has_soil_layer,
            # "has_soil_level": self.__has_soil_level,
            # "height_level": self.__height_level,
            "point_in_time": self.__point_in_time,
            # "potential_temperature_level": self.__potential_temperature_level,
            # "potential_vorticity_level": self.__potential_vorticity_level,
            # "predefined_level": self.__predefined_level,
            # "predefined_thickness": self.__predefined_thickness,
            # "pressure_level": self.__pressure_level,
            # "resolution_s2s": self.__resolution_s2s,
            # "resolution_s2s_ocean": self.__resolution_s2s_ocean,
            # "since_prev_pp": self.__since_prev_pp,
            # "six_hourly": self.__six_hourly,
            # "three_hourly": self.__three_hourly,
        }

        # parameters = IndexedLookupTable("TiggeParameters.json")
        parameters = IndexedLookupTable("test_tigge_data.json")
        super().__init__(tests=parameters, valueflg=valueflg, warnflg=warnflg, check_map=check_map)

    def _create_test(self, message: Message, parameters: dict) -> Test:
        return TiggeTest(message, parameters, self._check_map)

    def __given_level(self, message, p):
        print(Ne(message, "typeOfFirstFixedSurface", 255, 'ne(h,"typeOfFirstFixedSurface",255)'))
        print(Exists(message, "scaleFactorOfFirstFixedSurface", 'missing(h,"scaleFactorOfFirstFixedSurface")'))
        print(Exists(message, "scaledValueOfFirstFixedSurface", 'missing(h,"scaledValueOfFirstFixedSurface")'))
        print(Eq(message, "typeOfFirstFixedSurface", 103, 'eq(h,"typeOfFirstFixedSurface",103)'))
        print(Missing(message, "scaleFactorOfFirstFixedSurface", 'missing(h,"scaleFactorOfFirstFixedSurface")'))
        print(Missing(message, "scaledValueOfFirstFixedSurface", 'missing(h,"scaledValueOfFirstFixedSurface")'))

    def __point_in_time(self, handle, p):
        print("dummy point_in_time()")
