#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from .Message import Message
from .Report import Report


class Test:
    """
    This class determines the order in which the checks are executed.
    As a rule, it receives a "parameter" with a list of the checks to be executed and a "check_map"
    indicating where the code for the respective tests is located.
    The test is then applied to the "message".
    """

    def __init__(self, message: Message, parameter: dict, check_map: dict):
        raise NotImplementedError

    def run(self) -> Report:
        raise NotImplementedError
