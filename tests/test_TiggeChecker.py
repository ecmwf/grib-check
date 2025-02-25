import unittest
from Grib import Grib
from TiggeChecker import TiggeChecker
    
class TestWmoChecker(unittest.TestCase):
    def test_load_data_from_file(self):
        checker = TiggeChecker(verbosity=4)

        # for message in Grib("./tests/tigge/tigge_ecmf_sfc_10v.grib"):
        # for message in Grib("./tests/tigge_small/tigge_all.grib2"):
        for message in Grib("tests/tigge/tigge_egrr_sfc_str.grib"):
            result, report = checker.validate(message)
            print(report)

if __name__ == '__main__':
    unittest.main()
