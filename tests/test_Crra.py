#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import os

from grib_check.checker.Crra import Crra
from grib_check.Grib import Grib
from grib_check.LookupTable import SimpleLookupTable

src_path = f"{os.path.dirname(os.path.realpath(__file__))}/../src/grib_check"


class TestCrra:
    def test_crra_param_ws_good(self):
        crra_params = (f"{src_path}/checker/CrraParameters.jsonnet")
        checker = Crra(SimpleLookupTable(crra_params), check_limits=False, check_validity=False)
        grib = Grib("./tests/crra/crra_an_no-ar-pa_pl_ws.grib")
        message = next(grib)
        report = checker.validate(message)
        assert report.status() is True
