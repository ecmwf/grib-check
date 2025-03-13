from Message import Message
import logging
from Assert import Eq
from Report import Report

        
class Test:
    def __init__(self, message: Message, key: str, value):
        raise NotImplementedError

    def run(self) -> Report:
        raise NotImplementedError


class WmoTest(Test):
    def __init__(self, message: Message, parameter: dict, check_map: dict):
        self.logger = logging.getLogger(__class__.__name__)
        self.__message = message
        self.__parameter = parameter
        self.__check_map = check_map

    def run(self) -> Report:
        data = self.__parameter
        expected_report = Report("Check expected values")
        for kv in data["expected"]:
            key = kv["key"]
            value = kv["value"]
            try:
                expected_report.add(Eq(self.__message, key, value))
            except NotImplementedError:
                raise NotImplementedError("Not implemented")
            except FloatingPointError as e:
                pass

        checks_report = Report("Checks")
        for check_func in data["checks"]:
            check_report = self.__check_map[check_func](self.__message, data)
            check_report.rename_anonymous_report(f"{check_func}")
            checks_report.add(check_report)

        report = Report()
        report.add(expected_report)
        report.add(checks_report)
        return report


class TiggeTest(Test):
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
        report = Report("Checks")
        for check_func in data["checks"]:
            check_reports = self.__check_map[check_func](self.__message, data)
            merged_report = Report(f'{check_func}')
            for check_report in check_reports:
                merged_report.add(check_report)


            report.add(merged_report)

        return report
