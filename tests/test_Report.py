#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from grib_check.Assert import Fail, Pass
from grib_check.Report import Report


class TestAssert:

    def test_level_1(self):
        report = Report("Report 1")
        report.add(Pass("Assertion 1"))
        assert str(report) == "PASS: Report 1\n  PASS: Assertion 1\n"

        report.add(Fail("Assertion 2"))
        assert (
            str(report) == "FAIL: Report 1\n  PASS: Assertion 1\n  FAIL: Assertion 2\n"
        )

    def test_nested_report(self):
        report = Report("Report 1")
        report.add(Pass("Assertion 1"))

        nested = Report("Report 2")
        nested.add(Pass("Assertion 2"))

        report.add(nested)

        assert (
            str(report)
            == "PASS: Report 1\n  PASS: Assertion 1\n  PASS: Report 2\n    PASS: Assertion 2\n"
        )

    def test_assertions(self):
        report1 = Report("Test report")
        report1.add(Fail("Some error message"))
        assert str(report1) == "FAIL: Test report\n  FAIL: Some error message\n"

        f = Fail("Some error message")
        p = Pass("Some success message")
        report2 = Report("Test report 2")
        report2.add(f & p)

        assert (
            str(report2)
            == "FAIL: Test report 2\n  FAIL: Some error message and Some success message\n"
        )

    def test_add_string(self):
        report = Report("Test report")
        report.add(Fail("Some error message"))
        report.add("A message")

        assert (report.status() is False)

    def test_add_failed_report(self):
        report1 = Report("Report 1")
        report1.add(Fail("Bad message"))
        report2 = Report("Report 2")
        report2.add(Pass("Good message"))

        report = Report("Top report")
        report.add(report1)
        report.add(report2)

        assert (report.status() is False)
