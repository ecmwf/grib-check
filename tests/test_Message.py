#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import pytest
from eccodes import CODES_PRODUCT_GRIB, codes_new_from_samples

from grib_check.Message import Message


class TestMessage:
    def test_position(self):
        handle = codes_new_from_samples("GRIB2", product_kind=CODES_PRODUCT_GRIB)
        with pytest.raises(Exception):
            Message(handle=handle, position=0)

    # def test_type(self):
    #     handle = codes_new_from_samples("GRIB2", product_kind=CODES_PRODUCT_GRIB)
    #     msg = Message(handle=handle, position=1)
    #
    #     # Native type is str
    #     kv = msg.get("identifier")
    #     assert kv.type() is str
    #
    #     # Value can be converted to int
    #     kv = msg.get("identifier", datatype=int)
    #     assert kv.type() is int
    #
    #     # Value cannot be converted to float
    #     kv = msg.get("identifier", datatype=float)
    #     assert kv.type() is type(None)
