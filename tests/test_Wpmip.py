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
from grib_check.checker.Wpmip import Wpmip
from grib_check.Grib import Grib
from grib_check.Report import Report


def dummy(a, b):
    report = Report()
    report.add(Fail("dummy"))
    return report


class TestWpmip:

    def test_wpmip_paramId_176(self):
        check_map = {
            "from_start": dummy,
            "predefined_level": dummy,
        }

        parameter = {
            "name": "time_integrated_surface_net_solar_radiation_sfc.wpmip",
            "min1": -1e+5,
            "min2": 1e+05,
            "max1": 1e+05,
            "max2": 8e+06,
            "pairs": [
                {"key": "paramId", "key_type": "int", "value_long": 176},
                {"key": "discipline", "key_type": "int", "value_long": 0},
                {"key": "parameterCategory", "key_type": "int", "value_long": 4},
                {"key": "parameterNumber", "key_type": "int", "value_long": 9},
                {
                    "key": "typeOfFirstFixedSurface",
                    "key_type": "int",
                    "value_long": 1,
                },
            ],
            "checks": ["from_start", "predefined_level"],
        }

        for message in Grib("./tests/wpmip/wpmip_ecmf_sfc_ssr.grib"):
            test = Wpmip.DefaultTest(message, parameter, check_map)
            test.run()
