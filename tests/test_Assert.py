#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from grib_check.Assert import Eq
from grib_check.Grib import Grib
from grib_check.KeyValue import KeyValue


class TestAssert:
    def test_and(self):
        kv1 = KeyValue("stream", "eefo")
        kv2 = KeyValue("stream", "nai")

        eq1 = Eq(kv1, kv1)
        eq2 = Eq(kv1, kv2)

        assert eq1
        assert not eq2

        a = eq1 & eq2
        assert not a
        assert f"{eq1} and {eq2}" == a.as_string()

        a = eq1 & eq1
        assert a
        assert f"{eq1} and {eq1}" == a.as_string()

    def test_or(self):
        kv1 = KeyValue("stream", "eefo")
        kv2 = KeyValue("stream", "nai")

        eq1 = Eq(kv1, kv1)
        eq2 = Eq(kv1, kv2)

        assert eq1
        assert not eq2

        a = eq1 | eq2
        assert a
        assert f"{eq1} or {eq2}" == a.as_string()

        a = eq1 | eq1
        assert a
        assert f"{eq1} or {eq1}" == a.as_string()

    def test_eq(self):
        from grib_check.Assert import Eq

        kv1 = KeyValue("stream", "eefo")
        kv2 = KeyValue("stream", "nai")

        eq = Eq(kv1, kv1)
        assert eq
        assert f"{kv1} == {kv1}" == eq.as_string()

        eq = Eq(kv1, kv2)
        assert not eq
        assert f"{kv1} == {kv2}" == eq.as_string()

        eq = Eq(kv1, "eefo")
        assert eq
        assert f"{kv1} == eefo" == eq.as_string()

        eq = Eq("eefo", kv1)
        assert eq
        assert f"eefo == {kv1}" == eq.as_string()

        eq = Eq(kv2, "nai")
        assert eq
        assert f"{kv2} == nai" == eq.as_string()

        eq = Eq("nai", kv2)
        assert eq
        assert f"nai == {kv2}" == eq.as_string()

        eq = Eq("eefo", "eefo")
        assert eq
        assert "eefo == eefo" == eq.as_string()

        eq = Eq("eefo", "nai")
        assert not eq
        assert "eefo == nai" == eq.as_string()

    def test_isin(self):
        from grib_check.Assert import IsIn

        kv = KeyValue("stream", "eefo")

        isin = IsIn(kv, ["eefo", "nai"])
        assert isin
        assert "stream(eefo) in ['eefo', 'nai']" == isin.as_string()

        isin = IsIn(kv, ["nai", "dgov"])
        assert not isin
        assert "stream(eefo) in ['nai', 'dgov']" == isin.as_string()

    def test_multiple_of(self):
        from grib_check.Assert import IsMultipleOf

        multiple_of = IsMultipleOf(KeyValue("test", 12), 6)
        assert multiple_of
        assert "test(12) % 6 == 0" == multiple_of.as_string()

        multiple_of = IsMultipleOf(KeyValue("test", 12), 7)
        assert not multiple_of
        assert "test(12) % 7 == 0" == multiple_of.as_string()

    def test_exists(self):
        from grib_check.Assert import Exists

        grib = Grib("tests/dgov-data/od_eefo_fcmean_sfc_2024_0001_reduced_gg.grib2")
        message = grib.__next__()

        exists = Exists(message, "stream")
        assert exists
        assert (
            "stream exists(True) and has a non-missing value(True)"
            == exists.as_string()
        )

        exists = Exists(message, "non_existent_key")
        assert not exists
        assert (
            "non_existent_key exists(False) and has a non-missing value(None)"
            == exists.as_string()
        )

        exists = Exists(message, "hoursAfterDataCutoff")
        assert not exists
        assert (
            "hoursAfterDataCutoff exists(True) and has a non-missing value(False)"
            == exists.as_string()
        )

    def test_missing(self):
        from grib_check.Assert import Missing

        grib = Grib("tests/dgov-data/od_eefo_fcmean_sfc_2024_0001_reduced_gg.grib2")
        message = grib.__next__()

        missing = Missing(message, "stream")
        assert not missing
        assert (
            "stream exists(True) and has a missing value(False)" == missing.as_string()
        )

        missing = Missing(message, "non_existent_key")
        assert not missing
        assert (
            "non_existent_key exists(False) and has a missing value(None)"
            == missing.as_string()
        )

        missing = Missing(message, "hoursAfterDataCutoff")
        assert (
            "hoursAfterDataCutoff exists(True) and has a missing value(True)"
            == missing.as_string()
        )
        assert missing

    def test_eq_double(self):
        from grib_check.Assert import EqDbl

        kv = KeyValue("test", 6.0001)
        eq = EqDbl(kv, 6.0, 0.01)
        assert eq
        assert "test(6.0001) == 6.0 within 0.01" == eq.as_string()

        eq = EqDbl(kv, 6.0, 0.00001)
        assert not eq
        assert "test(6.0001) == 6.0 within 1e-05" == eq.as_string()

        eq = EqDbl(kv, 7.0, 0.01)
        assert not eq
        assert "test(6.0001) == 7.0 within 0.01" == eq.as_string()

        # TODO(maee): Add functionality to compare KeyValue with KeyValue

        # eq = EqDbl(6.0001, 6.0, 0.01)
        # assert eq
        # assert "6.0001 == 6.0 within 0.01" == eq.as_string()

        # eq = EqDbl(6, kv, 0.00001)
        # assert not eq
        # assert "6 == test(6.0001) within 1e-05" == eq.as_string()

        # eq = EqDbl(6, 6, 0.01)
        # assert eq
        # assert "6 == 6 within 0.01" == eq.as_string()

    def test_ne(self):
        from grib_check.Assert import Ne

        kv1 = KeyValue("test", 6)
        kv2 = KeyValue("test", 7)
        ne = Ne(kv1, kv2)
        assert ne
        assert "test(6) != test(7)" == ne.as_string()

        ne = Ne(kv1, 6)
        assert not ne
        assert "test(6) != 6" == ne.as_string()

        ne = Ne(kv1, 7)
        assert ne
        assert "test(6) != 7" == ne.as_string()

        ne = Ne(6, 7)
        assert ne
        assert "6 != 7" == ne.as_string()

        ne = Ne(6, 6)
        assert not ne
        assert "6 != 6" == ne.as_string()

        ne = Ne(6, kv1)
        assert not ne
        assert "6 != test(6)" == ne.as_string()

        ne = Ne(7, kv1)
        assert ne
        assert "7 != test(6)" == ne.as_string()

    def test_ge(self):
        from grib_check.Assert import Ge

        kv1 = KeyValue("test", 6)
        kv2 = KeyValue("test", 7)
        ge = Ge(kv1, kv2)
        assert not ge
        assert "test(6) >= test(7)" == ge.as_string()

        ge = Ge(kv1, 6)
        assert ge
        assert "test(6) >= 6" == ge.as_string()

        ge = Ge(kv1, 5)
        assert ge
        assert "test(6) >= 5" == ge.as_string()

        ge = Ge(6, 7)
        assert not ge
        assert "6 >= 7" == ge.as_string()

        ge = Ge(6, 6)
        assert ge
        assert "6 >= 6" == ge.as_string()

        ge = Ge(7, kv1)
        assert ge
        assert "7 >= test(6)" == ge.as_string()

        ge = Ge(5, kv1)
        assert not ge
        assert "5 >= test(6)" == ge.as_string()

    def test_le(self):
        from grib_check.Assert import Le

        kv1 = KeyValue("test", 6)
        kv2 = KeyValue("test", 7)
        le = Le(kv1, kv2)
        assert le
        assert "test(6) <= test(7)" == le.as_string()

        le = Le(kv1, 6)
        assert le
        assert "test(6) <= 6" == le.as_string()

        le = Le(kv1, 5)
        assert not le
        assert "test(6) <= 5" == le.as_string()

        le = Le(6, 7)
        assert le
        assert "6 <= 7" == le.as_string()

        le = Le(6, 6)
        assert le
        assert "6 <= 6" == le.as_string()

        le = Le(7, kv1)
        assert not le
        assert "7 <= test(6)" == le.as_string()

        le = Le(5, kv1)
        assert le
        assert "5 <= test(6)" == le.as_string()

    def test_gt(self):
        from grib_check.Assert import Gt

        kv1 = KeyValue("test", 6)
        kv2 = KeyValue("test", 7)
        gt = Gt(kv1, kv2)
        assert not gt
        assert "test(6) > test(7)" == gt.as_string()

        gt = Gt(kv1, 6)
        assert not gt
        assert "test(6) > 6" == gt.as_string()

        gt = Gt(kv1, 5)
        assert gt
        assert "test(6) > 5" == gt.as_string()

        gt = Gt(6, 7)
        assert not gt
        assert "6 > 7" == gt.as_string()

        gt = Gt(6, 6)
        assert not gt
        assert "6 > 6" == gt.as_string()

        gt = Gt(7, kv1)
        assert gt
        assert "7 > test(6)" == gt.as_string()

        gt = Gt(5, kv1)
        assert not gt
        assert "5 > test(6)" == gt.as_string()

    def test_lt(self):
        from grib_check.Assert import Lt

        kv1 = KeyValue("test", 6)
        kv2 = KeyValue("test", 7)
        lt = Lt(kv1, kv2)
        assert lt
        assert "test(6) < test(7)" == lt.as_string()

        lt = Lt(kv1, 6)
        assert not lt
        assert "test(6) < 6" == lt.as_string()

        lt = Lt(kv1, 5)
        assert not lt
        assert "test(6) < 5" == lt.as_string()

        lt = Lt(6, 7)
        assert lt
        assert "6 < 7" == lt.as_string()

        lt = Lt(6, 6)
        assert not lt
        assert "6 < 6" == lt.as_string()

        lt = Lt(7, kv1)
        assert not lt
        assert "7 < test(6)" == lt.as_string()

        lt = Lt(5, kv1)
        assert lt
        assert "5 < test(6)" == lt.as_string()

    def test_fail(self):
        from grib_check.Assert import Fail

        fail = Fail("This is a failure")
        assert not fail
        assert "This is a failure" == fail.as_string()

        fail = Fail("Another failure")
        assert not fail
        assert "Another failure" == fail.as_string()

    def test_pass(self):
        from grib_check.Assert import Pass

        pas = Pass("This is a pass")
        assert pas
        assert "This is a pass" == pas.as_string()

        pas = Pass("Another pass")
        assert pas
        assert "Another pass" == pas.as_string()
