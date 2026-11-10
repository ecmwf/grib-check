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

from grib_check.checker.Lcgcr import Lcgcr
from grib_check.Grib import Grib
from grib_check.LookupTable import SimpleLookupTable

src_path = f"{os.path.dirname(os.path.realpath(__file__))}/../src/grib_check"


class TestLcgcr:
    def test_lcgcr_param_an_good(self):
        lcgcr_params = (f"{src_path}/checker/LcgcrParameters.jsonnet")
        checker = Lcgcr(SimpleLookupTable(lcgcr_params), check_limits=False, check_validity=False)
        grib = Grib("./tests/lcgcr/ecmf.19910101.an.sfc.grib")
        message = next(grib)
        report = checker.validate(message)
        assert report.status() is True

    def test_lcgcr_param_fc_good(self):
        lcgcr_params = (f"{src_path}/checker/LcgcrParameters.jsonnet")
        checker = Lcgcr(SimpleLookupTable(lcgcr_params), check_limits=False, check_validity=False)
        grib = Grib("./tests/lcgcr/ecmf.19910101.fc.sfc.grib")
        message = next(grib)
        report = checker.validate(message)
        assert report.status() is True
