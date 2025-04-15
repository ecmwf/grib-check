import unittest
from LookupTable import SimpleLookupTable, IndexedLookupTable
from Grib import Grib
from Message import Message

class TestIndexedLookupTable(unittest.TestCase):
    def test_get_element(self):
        table = SimpleLookupTable("tests/test_parameters.json")
        grib = Grib("tests/wmo/od_eefo_fcmean_sfc_2024_0001_reduced_gg.grib2")
        message = next(grib)
        element, lookup_table_report = table.get_element(message)
        print(element)
        self.assertEqual(
                {
                "pairs": [
                    {"key": "stream", "value": "eefo"},
                    {"key": "dataType", "value": "fcmean"}
                ], 
                "expected": [
                    {"key": "productDefinitionTemplateNumber", "value": 11}, 
                    {"key": "paramId", "value": "228004"}, 
                    {"key": "shortName", "value": "mean2t"}, 
                    {"key": "name", "value": "Mean 2 metre temperature"}
                ],
                "checks": ["product_definition_template_number"]
                }, element)
            
if __name__ == '__main__':
    unittest.main()
