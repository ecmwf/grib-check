from CheckEngine import CheckEngine
from LookupTable import SimpleLookupTable
from Test import Test
from Report import Report
from Assert import Fail, Eq, Le, Ge, Gt, Lt
from Message import Message
import logging


class WmoChecker(CheckEngine):
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
                op = kv.get("op", None)
                key = kv["key"]
                key_type = type(kv["key"])
                value = kv["value"]
                comment = kv.get("comment", None)
                try:
                    if op is None:
                        expected_report.add(Eq(self.__message.get(key, key_type), value, comment))
                    elif op == "eq":
                        expected_report.add(Eq(self.__message.get(key, key_type), value, comment))
                    elif op == "lt":
                        expected_report.add(Lt(self.__message.get(key, key_type), value, comment))
                    elif op == "le":
                        expected_report.add(Le(self.__message.get(key, key_type), value, comment))
                    elif op == "gt":
                        expected_report.add(Gt(self.__message.get(key, key_type), value, comment))
                    elif op == "ge":
                        expected_report.add(Ge(self.__message.get(key, key_type), value, comment))
                    else:
                        raise NotImplementedError(f"Operation {op} not implemented")

                except NotImplementedError:
                    raise NotImplementedError("Not implemented")
                except FloatingPointError:
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


    def __init__(self, param_file="WmoParameters.json"):
        self.__check_map = {
            "basic_checks": self.__basic_checks,
            "product_definition_template_number": self.__product_definition_template_number,
            "derived_forecast": self.__derived_forecast
        }
        parameters = SimpleLookupTable(param_file)
        super().__init__(tests=parameters)

    def _create_test(self, message: Message, parameters: dict) -> Test:
        return self.WmoTest(message, parameters, self.__check_map)

    def __basic_checks(self, message, data):
        report = Report()
        report.add(Eq(message, "edition", 2))
        sub_report = Report() # Anonymous report
        # sub_report = Report("SUB REPORT") # Named report
        sub_report.add(Eq(message, "centre", 98))
        sub_report.add(Eq(message, "subCentre", 0))

        report.add(sub_report)
        return report

    def __product_definition_template_number(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy product_definition_template_number()"))
        return report

    def __derived_forecast(self, handle, p):
        report = Report()
        report.add(Fail("Not implemented: dummy derived_forecast()"))
        return report
