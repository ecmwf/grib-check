import unittest
from grib_check import GribCheck

class Config:
    def __init__(self):
        self.verbosity = 0
        self.grib_type = "tigge"
        self.warnflg = False
        self.valueflg = False
        self.zeroflg = False
        self.good = None
        self.bad = None
        self.report_verbosity = 3
        # self.path = ["./tests/tigge_small/tigge_all.grib2"]
        self.path = ["./tests/tigge_small/tigge_cf_ecmwf.grib2"]
        self.debug = True
        

class TestGribCheck(unittest.TestCase):
    def test_grib_check(self):
        config = Config()
        grib_check = GribCheck(config)
        grib_check.run()


if __name__ == '__main__':
    unittest.main()
