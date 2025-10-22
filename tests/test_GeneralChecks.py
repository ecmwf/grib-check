#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from grib_check.checker.GeneralChecks import GeneralChecks
from grib_check.Grib import Grib
from grib_check.LookupTable import SimpleLookupTable


class TestWmoChecker:
    def test_load_data_from_file(self):
        # checker = WmoChecker(param_file="./tests/WmoParameters.json")
        checker = GeneralChecks(SimpleLookupTable("./tests/test_parameters.json"))

        for message in Grib(
            "./tests/dgov-data/od_eefo_taes_sfc_2024_0001_reduced_gg.grib2"
        ):
            checker.validate(message)
