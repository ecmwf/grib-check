#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from grib_check.Assert import Fail
from grib_check.checker.Crra import Crra
from grib_check.Grib import Grib
from grib_check.Report import Report


def dummy(a, b):
    report = Report()
    report.add(Fail("dummy"))
    return report


class TestCrra:

    def test_crra_paramId_10(self):
        check_map = {
            "point_in_time": dummy,
            "given_level": dummy,
            "pressure_level": dummy,
        }

        parameter = {
            "name": "wind_speed_pl",
            "min1": 0,
            "min2": 10,
            "max1": 10,
            "max2": 150,
            "pairs": [
                {"key": "paramId", "key_type": "int", "value_long": 10},
                {"key": "discipline", "key_type": "int", "value_long": 0},
                {"key": "parameterCategory", "key_type": "int", "value_long": 2},
                {"key": "parameterNumber", "key_type": "int", "value_long": 1},
                {
                    "key": "typeOfFirstFixedSurface",
                    "key_type": "int",
                    "value_long": 100,
                },
                {
                    "key": "scaleFactorOfFirstFixedSurface",
                    "key_type": "int",
                    "value_long": 0,
                },
            ],
            "checks": ["point_in_time", "given_level", "pressure_level"],
        }

        for message in Grib("./tests/crra/crra_an_no-ar-pa_pl_ws.grib"):
            test = Crra.DefaultTest(message, parameter, check_map)
            test.run()
