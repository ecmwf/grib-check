#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from grib_check.Grib import Grib
from grib_check.LookupTable import SimpleLookupTable


class TestIndexedLookupTable:
    def test_get_element(self):
        table = SimpleLookupTable("tests/test_parameters.json")
        grib = Grib("tests/wmo/od_eefo_fcmean_sfc_2024_0001_reduced_gg.grib2")
        message = next(grib)
        element, lookup_table_report = table.get_element(message)
        expected = {
            "name": "param_1",
            "pairs": [
                {"key": "stream", "value": "eefo"},
                {"key": "dataType", "value": "fcmean"},
            ],
            "expected": [
                {"key": "productDefinitionTemplateNumber", "value": 11},
                {"key": "paramId", "value": "228004"},
                {"key": "shortName", "value": "mean2t"},
                {"key": "name", "value": "Mean 2 metre temperature"},
            ],
            "checks": ["basic_checks"],
        }
        assert expected == element
