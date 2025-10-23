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

from grib_check.checker.Wpmip import Wpmip
from grib_check.Grib import Grib
from grib_check.LookupTable import SimpleLookupTable

src_path = f"{os.path.dirname(os.path.realpath(__file__))}/../src/grib_check"


class TestWpmip:
    def test_wpmip_param_ssr_good(self):
        wpmip_params = (f"{src_path}/checker/WpmipParameters.jsonnet")
        checker = Wpmip(SimpleLookupTable(wpmip_params), check_limits=False, check_validity=False)
        grib = Grib("./tests/wpmip/wpmip_ecmf_sfc_ssr.grib")
        message = next(grib)
        report = checker.validate(message)
        assert report.status() is True

    def test_wpmip_param_tp_ranges_good(self):
        wpmip_params = (f"{src_path}/checker/WpmipParameters.jsonnet")
        checker = Wpmip(SimpleLookupTable(wpmip_params), check_limits=True, check_validity=False)
        grib = Grib("./tests/wpmip/wpmip_cwao_sfc_tp.grib")
        message = next(grib)
        report = checker.validate(message)
        assert report.status() is True
