#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

# from grib_check.GribCheck import GribCheck


class Config:
    def __init__(self):
        self.verbosity = 0
        self.convention = "tigge"
        self.warnflg = False
        self.valueflg = False
        self.zeroflg = False
        self.good = None
        self.bad = None
        self.report_verbosity = 3
        self.parameters = None
        self.num_threads = 1
        self.color = False
        # self.path = ["./tests/tigge_small/tigge_all.grib2"]
        self.path = ["./tests/tigge_small/tigge_cf_ecmwf.grib2"]
        self.debug = True
        self.failed_only = False
        self.format = "tree"


# class TestGribCheck:
#     def test_grib_check(self):
#         config = Config()
#         grib_check = GribCheck(config)
#         grib_check.run()
