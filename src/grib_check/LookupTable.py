#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import json
import sys

# import pandas as pd
import _jsonnet

from .Message import Message
from .Report import Report


class LookupTable:
    def __init__(self, filename: str):
        raise NotImplementedError

    def get_element(self, message: Message):
        raise NotImplementedError


class SimpleLookupTable(LookupTable):
    """
    A simple lookup table that uses a JSON file to store the data.
    """

    def __init__(self, filename: str, ignore_keys=None):
        assert filename is not None
        try:
            jresult = _jsonnet.evaluate_file(filename)
            self.data = json.loads(jresult)
        except ValueError as e:
            print(f"ERROR: Couldn't read JSON file {filename}: {e}", file=sys.stderr)
            sys.exit(1)

        self.ignore_keys = ignore_keys

    def get_element(self, message: Message):
        report = Report("Matched parameter")
        params = list()
        for row in self.data:
            count = 0
            count_ignore = 0
            for pair in row["pairs"]:
                if self.ignore_keys is not None and pair["key"] in self.ignore_keys:
                    count_ignore += 1
                    continue
                if message.get(pair["key"], type(pair["value"])) == pair["value"]:
                    count += 1
            if count == len(row["pairs"]) - count_ignore:
                params.append((count, row))
        if len(params) > 0:
            params.sort(key=lambda x: x[0], reverse=True)
            if "name" in params[0][1]:
                report.rename(f"Matched parameter: {params[0][1]['name']}")
            for pair in params[0][1]["pairs"]:
                report.add(pair["key"] + ": " + str(pair["value"]))
            return params[0][1], report

        return (None, report)


class IndexedLookupTable(LookupTable):
    """
    A lookup table that uses a dictionary to store the data.
    The dictionary is indexed by the keys in the data.

    TODO: Implement and replace SimpleLookupTable with this class.
    """

    def __init__(self, filename: str):
        raise NotImplementedError

    def get_element(self, message: Message):
        raise NotImplementedError
