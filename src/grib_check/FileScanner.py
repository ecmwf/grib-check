#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import logging
import os


class FileScanner:
    def __init__(self, paths):
        self.fns = []
        self.logger = logging.getLogger(__class__.__name__)
        for path in paths:
            if os.path.isdir(path):
                self.logger.debug(f"Scanning {path}")
                for root, dirs, fns in os.walk(path):
                    for fn in fns:
                        self.fns.append(root + "/" + fn)
            else:
                self.fns.append(path)

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self) -> str:
        if self.pos < len(self.fns):
            fn = self.fns[self.pos]
            self.pos += 1
            return fn
        else:
            raise StopIteration
