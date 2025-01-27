import unittest
from IndexedLookupTable import IndexedLookupTable

class TestIndexedLookupTable(unittest.TestCase):
    def test_load_data_from_file(self):
        IndexedLookupTable("test_data.json")

    def test_get_index(self):
        table = IndexedLookupTable("test_data.json")
        idx_keys = table.get_index_keys()
        self.assertEqual(["stream", "dataType"], idx_keys)

    def test_get_element(self):
        table = IndexedLookupTable("test_data.json")
        element = table.get_element({"stream": "eefo", "dataType": "fcmean"})
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
