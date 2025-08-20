#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.
#

import unittest
from Grib import Grib
from Report import Report
from Assert import Fail
from checker.Tigge import Tigge

def dummy(a, b):
    report = Report()
    report.add(Fail("dummy"))
    return report

class TestTest(unittest.TestCase):
    # def test_create_wmo_test(self):
    #     check_map = {
    #         # "product_definition_template_number": self.__product_definition_template_number,
    #         # "derived_forecast": self.__derived_forecast
    #         "product_definition_template_number": dummy,
    #         "derived_forecast": dummy
    #     }
    #
    #     parameter = {
    #         "pairs": [
    #             {"key": "stream", "value": "eefo"},
    #             {"key": "dataType", "value": "fcmean"}
    #         ], 
    #         "expected": [
    #             {"key": "productDefinitionTemplateNumber", "value": 11}, 
    #             {"key": "paramId", "value": "228004"}, 
    #             {"key": "shortName", "value": "mean2t"}, 
    #             {"key": "name", "value": "Mean 2 metre temperature"}
    #         ],
    #         "checks": ["product_definition_template_number"]
    #     }
    #
    #     for message in Grib("dgov-data/od_eefo_taes_sfc_2024_0001_reduced_gg.grib2"):
    #         test = WmoTest(message, parameter, check_map)
    #         test.run()

    def test_create_tigge_test(self):
        check_map = {
            "point_in_time": dummy,
            "given_level": dummy,
        }

        parameter = {
            "name": "10_meter_u_velocity_sfc.glob",
            "min1": -100,
            "min2": -1,
            "max1": 1,
            "max2": 100,
            "pairs": [
                {
                    "key": "model",
                    "key_type": "str",
                    "value_long": 0,
                    "value_string": "glob"
                },
                {
                    "key": "paramId",
                    "key_type": "int",
                    "value_long": 165
                },
                {
                    "key": "discipline",
                    "key_type": "int",
                    "value_long": 0
                },
                {
                    "key": "parameterCategory",
                    "key_type": "int",
                    "value_long": 2
                },
                {
                    "key": "parameterNumber",
                    "key_type": "int",
                    "value_long": 2
                },
                {
                    "key": "scaleFactorOfFirstFixedSurface",
                    "key_type": "int",
                    "value_long": 0
                },
                {
                    "key": "scaledValueOfFirstFixedSurface",
                    "key_type": "int",
                    "value_long": 10
                },
                {
                    "key": "typeOfFirstFixedSurface",
                    "key_type": "int",
                    "value_long": 103
                }
            ],
            "checks": [
                "point_in_time",
                "given_level"
            ]
        }

        for message in Grib("./tests/tigge/tigge_ecmf_sfc_10v.grib"):
            test = Tigge.DefaultTest(message, parameter, check_map)
            report = test.run()
            print(report)

if __name__ == '__main__':
    unittest.main()

