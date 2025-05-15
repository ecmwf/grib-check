import unittest
from Grib import Grib
from checker.Wmo import Wmo
from LookupTable import SimpleLookupTable
    
class TestWmoChecker(unittest.TestCase):
    def test_load_data_from_file(self):
        # checker = WmoChecker(param_file="./tests/WmoParameters.json")
        checker = Wmo(SimpleLookupTable("./tests/test_parameters.json"))

        for message in Grib("./tests/dgov-data/od_eefo_taes_sfc_2024_0001_reduced_gg.grib2"):
            checker.validate(message)


if __name__ == '__main__':
    unittest.main()
