#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import numpy as np
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

    def test_get_array_double(self):
        handle = codes_new_from_samples("GRIB2", product_kind=CODES_PRODUCT_GRIB)
        msg = Message(handle=handle, position=1)

        kv = msg.get_array("values")
        assert kv.key() == "values"
        assert isinstance(kv.value(), np.ndarray)
        assert len(kv.value()) == 496
        # Default GRIB2 sample has all values = 273.0
        assert kv.value()[0] == 273.0

    def test_get_array_double_explicit_datatype(self):
        handle = codes_new_from_samples("GRIB2", product_kind=CODES_PRODUCT_GRIB)
        msg = Message(handle=handle, position=1)

        kv = msg.get_array("values", datatype=float)
        assert kv.key() == "values"
        assert isinstance(kv.value(), np.ndarray)
        assert len(kv.value()) == 496

    def test_get_array_double_string_datatype(self):
        handle = codes_new_from_samples("GRIB2", product_kind=CODES_PRODUCT_GRIB)
        msg = Message(handle=handle, position=1)

        kv = msg.get_array("values", datatype="double")
        assert kv.key() == "values"
        assert isinstance(kv.value(), np.ndarray)

    def test_get_array_long(self):
        handle = codes_new_from_samples(
            "reduced_gg_pl_32_grib2", product_kind=CODES_PRODUCT_GRIB
        )
        msg = Message(handle=handle, position=1)

        kv = msg.get_array("pl")
        assert kv.key() == "pl"
        assert isinstance(kv.value(), np.ndarray)
        assert len(kv.value()) == 64
        assert kv.value()[0] == 20

    def test_get_array_long_explicit_datatype(self):
        handle = codes_new_from_samples(
            "reduced_gg_pl_32_grib2", product_kind=CODES_PRODUCT_GRIB
        )
        msg = Message(handle=handle, position=1)

        kv = msg.get_array("pl", datatype=int)
        assert kv.key() == "pl"
        assert isinstance(kv.value(), np.ndarray)

    def test_get_array_long_string_datatype(self):
        handle = codes_new_from_samples(
            "reduced_gg_pl_32_grib2", product_kind=CODES_PRODUCT_GRIB
        )
        msg = Message(handle=handle, position=1)

        kv = msg.get_array("pl", datatype="long")
        assert kv.key() == "pl"
        assert isinstance(kv.value(), np.ndarray)

    def test_get_array_unsupported_datatype(self):
        handle = codes_new_from_samples("GRIB2", product_kind=CODES_PRODUCT_GRIB)
        msg = Message(handle=handle, position=1)

        with pytest.raises(Exception, match="Unsupported datatype"):
            msg.get_array("values", datatype=str)

    def test_get_array_indexing(self):
        handle = codes_new_from_samples(
            "reduced_gg_pl_32_grib2", product_kind=CODES_PRODUCT_GRIB
        )
        msg = Message(handle=handle, position=1)

        kv = msg.get_array("pl")
        elem = kv[0]
        assert elem.key() == "pl[0]"
        assert elem.value() == 20

        elem = kv[1]
        assert elem.key() == "pl[1]"
        assert elem.value() == 27
