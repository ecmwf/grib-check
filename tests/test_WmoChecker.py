import unittest
from Grib import Grib
from WmoChecker import WmoChecker
    
class TestWmoChecker(unittest.TestCase):
    def test_load_data_from_file(self):
        checker = WmoChecker()

        for message in Grib("dgov-data/od_eefo_taes_sfc_2024_0001_reduced_gg.grib2"):
            checker.validate(message)


if __name__ == '__main__':
    unittest.main()
