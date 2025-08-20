import unittest
from Grib import Grib
from Assert import Eq
from KeyValue import KeyValue

class TestAssert(unittest.TestCase):
    def test_and(self):
        kv1 = KeyValue("stream", "eefo")
        kv2 = KeyValue("stream", "nai")

        eq1 = Eq(kv1, kv1)
        eq2 = Eq(kv1, kv2)

        self.assertTrue(eq1.status())
        self.assertFalse(eq2.status())

        a = eq1 & eq2
        self.assertFalse(a.status())
        self.assertEqual(f"{eq1} and {eq2}", a.as_string())

        a = eq1 & eq1
        self.assertTrue(a.status())
        self.assertEqual(f"{eq1} and {eq1}", a.as_string())

    def test_or(self):
        kv1 = KeyValue("stream", "eefo")
        kv2 = KeyValue("stream", "nai")

        eq1 = Eq(kv1, kv1)
        eq2 = Eq(kv1, kv2)

        self.assertTrue(eq1.status())
        self.assertFalse(eq2.status())

        a = eq1 | eq2
        self.assertTrue(a.status())
        self.assertEqual(f"{eq1} or {eq2}", a.as_string())

        a = eq1 | eq1
        self.assertTrue(a.status())
        self.assertEqual(f"{eq1} or {eq1}", a.as_string())

    def test_eq(self):
        from Assert import Eq
        kv1 = KeyValue("stream", "eefo")
        kv2 = KeyValue("stream", "nai")

        eq = Eq(kv1, kv1)
        self.assertTrue(eq.status())
        self.assertEqual(f"{kv1} == {kv1}", eq.as_string())

        eq = Eq(kv1, kv2)
        self.assertFalse(eq.status())
        self.assertEqual(f"{kv1} == {kv2}", eq.as_string())

        eq = Eq(kv1, "eefo")
        self.assertTrue(eq.status())
        self.assertEqual(f"{kv1} == eefo", eq.as_string())

        eq = Eq("eefo", kv1)
        self.assertTrue(eq.status())
        self.assertEqual(f"eefo == {kv1}", eq.as_string())

        eq = Eq(kv2, "nai")
        self.assertTrue(eq.status())
        self.assertEqual(f"{kv2} == nai", eq.as_string())

        eq = Eq("nai", kv2)
        self.assertTrue(eq.status())
        self.assertEqual(f"nai == {kv2}", eq.as_string())

        eq = Eq("eefo", "eefo")
        self.assertTrue(eq.status())
        self.assertEqual("eefo == eefo", eq.as_string())

        eq = Eq("eefo", "nai")
        self.assertFalse(eq.status())
        self.assertEqual("eefo == nai", eq.as_string())

    def test_isin(self):
        from Assert import IsIn
        kv = KeyValue("stream", "eefo")

        isin = IsIn(kv, ["eefo", "nai"])
        self.assertTrue(isin.status())
        self.assertEqual("stream(eefo) in ['eefo', 'nai']", isin.as_string())

        isin = IsIn(kv, ["nai", "dgov"])
        self.assertFalse(isin.status())
        self.assertEqual("stream(eefo) in ['nai', 'dgov']", isin.as_string())

    def test_multiple_of(self):
        from Assert import IsMultipleOf

        multiple_of = IsMultipleOf(KeyValue("test", 12), 6)
        self.assertTrue(multiple_of.status())
        self.assertEqual("test(12) % 6 == 0", multiple_of.as_string())

        multiple_of = IsMultipleOf(KeyValue("test", 12), 7)
        self.assertFalse(multiple_of.status())
        self.assertEqual("test(12) % 7 == 0", multiple_of.as_string())

    def test_exists(self):
        from Assert import Exists

        grib = Grib("tests/dgov-data/od_eefo_fcmean_sfc_2024_0001_reduced_gg.grib2")
        message = grib.__next__()

        exists = Exists(message, "stream")
        self.assertTrue(exists.status())
        self.assertEqual("stream exists(True) and has a non-missing value(True)", exists.as_string())

        exists = Exists(message, "non_existent_key")
        self.assertFalse(exists.status())
        self.assertEqual("non_existent_key exists(False) and has a non-missing value(None)", exists.as_string())

        exists = Exists(message, "hoursAfterDataCutoff")
        self.assertFalse(exists.status())
        self.assertEqual("hoursAfterDataCutoff exists(True) and has a non-missing value(False)", exists.as_string())

    def test_missing(self):
        from Assert import Missing

        grib = Grib("tests/dgov-data/od_eefo_fcmean_sfc_2024_0001_reduced_gg.grib2")
        message = grib.__next__()

        missing = Missing(message, "stream")
        self.assertFalse(missing.status())
        self.assertEqual("stream exists(True) and has a missing value(False)", missing.as_string())

        missing = Missing(message, "non_existent_key")
        self.assertFalse(missing.status())
        self.assertEqual("non_existent_key exists(False) and has a missing value(None)", missing.as_string())

        missing = Missing(message, "hoursAfterDataCutoff")
        self.assertEqual("hoursAfterDataCutoff exists(True) and has a missing value(True)", missing.as_string())
        self.assertTrue(missing.status())

    def test_eq_double(self):
        from Assert import EqDbl

        kv = KeyValue("test", 6.0001)
        eq = EqDbl(kv, 6.0, 0.01)
        self.assertTrue(eq.status())
        self.assertEqual("test(6.0001) == 6.0 within 0.01", eq.as_string())

        eq = EqDbl(kv, 6.0, 0.00001)
        self.assertFalse(eq.status())
        self.assertEqual("test(6.0001) == 6.0 within 1e-05", eq.as_string())

        eq = EqDbl(kv, 7.0, 0.01)
        self.assertFalse(eq.status())
        self.assertEqual("test(6.0001) == 7.0 within 0.01", eq.as_string())

        # TODO(maee): Add functionality to compare KeyValue with KeyValue
        
        # eq = EqDbl(6.0001, 6.0, 0.01)
        # self.assertTrue(eq.status())
        # self.assertEqual("6.0001 == 6.0 within 0.01", eq.as_string())

        # eq = EqDbl(6, kv, 0.00001)
        # self.assertFalse(eq.status())
        # self.assertEqual("6 == test(6.0001) within 1e-05", eq.as_string())

        # eq = EqDbl(6, 6, 0.01)
        # self.assertTrue(eq.status())
        # self.assertEqual("6 == 6 within 0.01", eq.as_string())

    def test_ne(self):
        from Assert import Ne

        kv1 = KeyValue("test", 6)
        kv2 = KeyValue("test", 7)
        ne = Ne(kv1, kv2)
        self.assertTrue(ne.status())
        self.assertEqual("test(6) != test(7)", ne.as_string())

        ne = Ne(kv1, 6)
        self.assertFalse(ne.status())
        self.assertEqual("test(6) != 6", ne.as_string())

        ne = Ne(kv1, 7)
        self.assertTrue(ne.status())
        self.assertEqual("test(6) != 7", ne.as_string())

        ne = Ne(6, 7)
        self.assertTrue(ne.status())
        self.assertEqual("6 != 7", ne.as_string())  

        ne = Ne(6, 6)
        self.assertFalse(ne.status())
        self.assertEqual("6 != 6", ne.as_string())  

        ne = Ne(6, kv1)
        self.assertFalse(ne.status())
        self.assertEqual("6 != test(6)", ne.as_string())

        ne = Ne(7, kv1)
        self.assertTrue(ne.status())
        self.assertEqual("7 != test(6)", ne.as_string())

    def test_ge(self):
        from Assert import Ge

        kv1 = KeyValue("test", 6)
        kv2 = KeyValue("test", 7)
        ge = Ge(kv1, kv2)
        self.assertFalse(ge.status())
        self.assertEqual("test(6) >= test(7)", ge.as_string())

        ge = Ge(kv1, 6)
        self.assertTrue(ge.status())
        self.assertEqual("test(6) >= 6", ge.as_string())

        ge = Ge(kv1, 5)
        self.assertTrue(ge.status())
        self.assertEqual("test(6) >= 5", ge.as_string())

        ge = Ge(6, 7)
        self.assertFalse(ge.status())
        self.assertEqual("6 >= 7", ge.as_string())  

        ge = Ge(6, 6)
        self.assertTrue(ge.status())
        self.assertEqual("6 >= 6", ge.as_string())  

        ge = Ge(7, kv1)
        self.assertTrue(ge.status())
        self.assertEqual("7 >= test(6)", ge.as_string())

        ge = Ge(5, kv1)
        self.assertFalse(ge.status())
        self.assertEqual("5 >= test(6)", ge.as_string())


    def test_le(self):
        from Assert import Le

        kv1 = KeyValue("test", 6)
        kv2 = KeyValue("test", 7)
        le = Le(kv1, kv2)
        self.assertTrue(le.status())
        self.assertEqual("test(6) <= test(7)", le.as_string())

        le = Le(kv1, 6)
        self.assertTrue(le.status())
        self.assertEqual("test(6) <= 6", le.as_string())

        le = Le(kv1, 5)
        self.assertFalse(le.status())
        self.assertEqual("test(6) <= 5", le.as_string())

        le = Le(6, 7)
        self.assertTrue(le.status())
        self.assertEqual("6 <= 7", le.as_string())  

        le = Le(6, 6)
        self.assertTrue(le.status())
        self.assertEqual("6 <= 6", le.as_string())  

        le = Le(7, kv1)
        self.assertFalse(le.status())
        self.assertEqual("7 <= test(6)", le.as_string())

        le = Le(5, kv1)
        self.assertTrue(le.status())
        self.assertEqual("5 <= test(6)", le.as_string())

    def test_gt(self):
        from Assert import Gt

        kv1 = KeyValue("test", 6)
        kv2 = KeyValue("test", 7)
        gt = Gt(kv1, kv2)
        self.assertFalse(gt.status())
        self.assertEqual("test(6) > test(7)", gt.as_string())

        gt = Gt(kv1, 6)
        self.assertFalse(gt.status())
        self.assertEqual("test(6) > 6", gt.as_string())

        gt = Gt(kv1, 5)
        self.assertTrue(gt.status())
        self.assertEqual("test(6) > 5", gt.as_string())

        gt = Gt(6, 7)
        self.assertFalse(gt.status())
        self.assertEqual("6 > 7", gt.as_string())  

        gt = Gt(6, 6)
        self.assertFalse(gt.status())
        self.assertEqual("6 > 6", gt.as_string())  

        gt = Gt(7, kv1)
        self.assertTrue(gt.status())
        self.assertEqual("7 > test(6)", gt.as_string())

        gt = Gt(5, kv1)
        self.assertFalse(gt.status())
        self.assertEqual("5 > test(6)", gt.as_string())

    def test_lt(self):
        from Assert import Lt

        kv1 = KeyValue("test", 6)
        kv2 = KeyValue("test", 7)
        lt = Lt(kv1, kv2)
        self.assertTrue(lt.status())
        self.assertEqual("test(6) < test(7)", lt.as_string())

        lt = Lt(kv1, 6)
        self.assertFalse(lt.status())
        self.assertEqual("test(6) < 6", lt.as_string())

        lt = Lt(kv1, 5)
        self.assertFalse(lt.status())
        self.assertEqual("test(6) < 5", lt.as_string())

        lt = Lt(6, 7)
        self.assertTrue(lt.status())
        self.assertEqual("6 < 7", lt.as_string())  

        lt = Lt(6, 6)
        self.assertFalse(lt.status())
        self.assertEqual("6 < 6", lt.as_string())  

        lt = Lt(7, kv1)
        self.assertFalse(lt.status())
        self.assertEqual("7 < test(6)", lt.as_string())

        lt = Lt(5, kv1)
        self.assertTrue(lt.status())
        self.assertEqual("5 < test(6)", lt.as_string())
        

    def test_fail(self):
        from Assert import Fail

        fail = Fail("This is a failure")
        self.assertFalse(fail.status())
        self.assertEqual("This is a failure", fail.as_string())

        fail = Fail("Another failure")
        self.assertFalse(fail.status())
        self.assertEqual("Another failure", fail.as_string())


    def test_pass(self):
        from Assert import Pass

        pas = Pass("This is a pass")
        self.assertTrue(pas.status())
        self.assertEqual("This is a pass", pas.as_string())

        pas = Pass("Another pass")
        self.assertTrue(pas.status())
        self.assertEqual("Another pass", pas.as_string())

if __name__ == '__main__':
    unittest.main()
