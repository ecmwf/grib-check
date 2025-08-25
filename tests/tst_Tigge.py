#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.
#

from grib_check.checker.Tigge import Tigge
from grib_check.Grib import Grib


class TestWmoChecker:
    def test_load_data_from_file(self):
        checker = Tigge(
            "tests/tigge/tigge_egrr_sfc_str.grib",
        )

        # for message in Grib("./tests/tigge/tigge_ecmf_sfc_10v.grib"):
        # for message in Grib("./tests/tigge_small/tigge_all.grib2"):
        for message in Grib("tests/tigge/tigge_egrr_sfc_str.grib"):
            report = checker.validate(message)
            print(report)
