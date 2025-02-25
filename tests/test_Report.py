import unittest
from Report import Report

class TestAssert(unittest.TestCase):

    def test_level_1(self):
        report = Report()
        report.add("level 1")
        output = str(report)
        self.assertEqual(output, "level 1\n")

        report.add("level 1")
        output = str(report)
        self.assertEqual(output, "level 1\nlevel 1\n")

    def test_nested_report(self):
        report = Report()
        report.add("level 1")

        nested = Report()
        nested.add("level 2")
        report.add(nested)

        output = str(report)
        self.assertEqual(output, "level 1\n  level 2\n")

            
if __name__ == '__main__':
    unittest.main()
