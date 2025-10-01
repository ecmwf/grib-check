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

from .Assert import Eq, Fail
from .LookupTable import LookupTable
from .Message import Message
from .Report import Report
from .Test import Test


class CheckEngine:
    class DefaultTest(Test):
        def __init__(self, message: Message, parameter: dict, check_map: dict):
            self.logger = logging.getLogger(__class__.__name__)
            assert parameter is not None
            assert message is not None
            assert check_map is not None

            self.__message = message
            self.__parameter = parameter
            self.__check_map = check_map

        def run(self) -> Report:
            data = self.__parameter
            report = Report(f"{data['name']}")
            for check_func in data["checks"]:
                try:
                    report.add(self.__check_map[check_func](self.__message, data))
                except KeyError:
                    report.add(Fail(f'Check function "{check_func}" not found'))
            return report

    def __init__(self, lookup_table: LookupTable):
        self.logger = logging.getLogger(__class__.__name__)
        assert lookup_table is not None
        self._test_store = lookup_table
        self._check_map = None

    def _create_test(self, message: Message, parameters: dict) -> Test:
        assert parameters is not None
        assert self._check_map is not None
        return self.DefaultTest(message, parameters, self._check_map)

    # def set_checks(self, check_map: dict):
    #     assert check_map is not None
    #     self._check_map = check_map

    def register_checks(self, check_funcs: dict):
        assert check_funcs is not None
        if self._check_map is None:
            self._check_map = dict()
        for name, func in check_funcs.items():
            if name in self._check_map:
                raise ValueError(f"Check function {name} already registered")
            self._check_map[name] = func

    def validate(self, message) -> Report:
        report = Report()
        kv, store_report = self._test_store.get_element(message)
        if kv is not None:
            test = self._create_test(message, kv)
            report.add(store_report)
            report.add(test.run())

            if "expected" in kv:
                expected_report = Report("Expected Values")
                for expected in kv["expected"]:
                    if "key" in expected and "value" in expected:
                        expected_report.add(
                            Eq(message[expected["key"]], expected["value"])
                        )
                report.add(expected_report)
        else:
            self.logger.debug(f"Could not find parameter for: {message}")
            report.add(Fail("Could not find parameter"))
            test_sub_report = Report()
            test_sub_report.add(message.get_report())
            report.add(test_sub_report)

        return report
