import unittest
from Grib import Grib
from Message import Message
from Assert import Eq

class TestAssert(unittest.TestCase):
    def test_eq(self):
        grib = Grib("tests/dgov-data/od_eefo_fcmean_sfc_2024_0001_reduced_gg.grib2")
        message = grib.__next__()
        eq = Eq(message["stream"], "eefo")
        self.assertTrue(eq.status())
        self.assertEqual("stream(eefo) == eefo", eq.as_string())

    def test_and(self):
        grib = Grib("tests/dgov-data/od_eefo_fcmean_sfc_2024_0001_reduced_gg.grib2")
        message = grib.__next__()
        eq1 = Eq(message["stream"], "eefo")
        eq2 = Eq(message["stream"], "eefo")

        self.assertTrue(eq1.status())
        self.assertTrue(eq2.status())

        a = eq1 & eq2
        self.assertTrue(a.status())
        self.assertEqual(f"{eq1} and {eq2}", a.as_string())
            
if __name__ == '__main__':
    unittest.main()
