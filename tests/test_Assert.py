import unittest
from Grib import Grib
from Message import Message
from Assert import Eq

class TestAssert(unittest.TestCase):
    def test_eq(self):
        grib = Grib("tests/dgov-data/od_eefo_fcmean_sfc_2024_0001_reduced_gg.grib2")
        message = grib.__next__()
        eq = Eq(message, "stream", "eefo")
        status, msg = eq.result()
        self.assertTrue(status)
        self.assertEqual("stream: eefo == eefo", msg)

    def test_and(self):
        grib = Grib("tests/dgov-data/od_eefo_fcmean_sfc_2024_0001_reduced_gg.grib2")
        message = grib.__next__()
        eq1 = Eq(message, "stream", "eefo")
        status1, msg1 = eq1.result()

        eq2 = Eq(message, "stream", "eefo")
        status2, msg2 = eq2.result()

        status, msg = eq1 & eq2
        self.assertTrue(status == status1 and status2)
        self.assertEqual(f"{msg1} and {msg2}", msg)
            
if __name__ == '__main__':
    unittest.main()
