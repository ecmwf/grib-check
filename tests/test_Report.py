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

        # print("report:")
        # print(report)

        self.assertEqual(str(report), "PASS: level 1\n  PASS: level 2\n")

    def test_assertions(self):
        report = Report()
        report.add(Fail("Some error message"))
        self.assertEqual(str(report), "FAIL: Some error message\n")

            
if __name__ == '__main__':
    unittest.main()
