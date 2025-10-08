#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from grib_check.KeyValue import KeyValue


class TestIndexedLookupTable:
    def test_init(self):
        a = KeyValue("a", 5)
        assert str(a) == "a(5)"

    def test_op(self):
        a = KeyValue("a", 5)
        b = KeyValue("b", 10)
        c = KeyValue("c", 15)

        x = a + b
        assert x.key() == "a(5) + b(10)"
        assert x.value() == 15

        x = a - b
        assert x.key() == "a(5) - b(10)"
        assert x.value() == -5

        x = c % 10
        assert x.key() == "c(15) % 10"
        assert x.value() == 5

        x = -a
        assert x.key() == "-(a(5))"
        assert x.value() == -5

    def test_parentheses(self):
        a = KeyValue("a", 5)
        b = KeyValue("b", 10)
        c = KeyValue("c", 15)

        x = a + b * c
        assert x.key() == "a(5) + b(10) * c(15)"
        assert x.value() == 5 + 10 * 15

        x = (a + b) * c
        assert x.key() == "(a(5) + b(10)) * c(15)"
        assert x.value() == (5 + 10) * 15

        x = (a + b) % 10
        assert x.key() == "(a(5) + b(10)) % 10"
        assert x.value() == (5 + 10) % 10

        x = -(a + b)
        assert x.key() == "-(a(5) + b(10))"
        assert x.value() == -(5 + 10)

    def test_key_suffix(self):
        a = KeyValue("a", 5, key_suffix="[0]")
        b = KeyValue("b", 10, key_suffix="[1]")
        c = KeyValue("c", 15, key_suffix="[2]")

        x = a + b * c
        assert x.key() == "a[0](5) + b[1](10) * c[2](15)"
        assert x.value() == 5 + 10 * 15
