import unittest
from Grib import Grib
from Test import WmoTest

def dummy(a, b):
    print("dummy")

class TestTest(unittest.TestCase):
    def test_create_test(self):
        check_map = {
            # "product_definition_template_number": self.__product_definition_template_number,
            # "derived_forecast": self.__derived_forecast
            "product_definition_template_number": dummy,
            "derived_forecast": dummy
        }

        parameter = {
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
        }

        for message in Grib("dgov-data/od_eefo_taes_sfc_2024_0001_reduced_gg.grib2"):
            test = WmoTest(message, parameter, check_map)
            test.run()



if __name__ == '__main__':
    unittest.main()

