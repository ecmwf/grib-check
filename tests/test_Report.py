import unittest
from Report import Report
from Assert import Le, Ne, Eq, Exists, Missing, Fail, Pass

class TestAssert(unittest.TestCase):

    def test_level_1(self):
        report = Report()
        report.add(Pass("level 1"))
        self.assertEqual(str(report), "PASS: level 1\n")

        report.add(Fail("level 1"))
        self.assertEqual(str(report), "PASS: level 1\nFAIL: level 1\n")

    def test_nested_report(self):
        report = Report()
        report.add(Pass("level 1"))

        nested = Report()
        nested.add(Pass("level 2"))
        report.add(nested)

        self.assertEqual(str(report), "PASS: level 1\n  PASS: level 2\n")

    def test_assertions(self):
        report1 = Report()
        report1.add(Fail("Some error message"))
        self.assertEqual(str(report1), "FAIL: Some error message\n")

        f = Fail("Some error message")
        p = Pass("Some success message")
        report2 = Report()
        report2.add(f & p)
        self.assertEqual(str(report2), "FAIL: Some error message and Some success message\n")

            
if __name__ == '__main__':
    unittest.main()
