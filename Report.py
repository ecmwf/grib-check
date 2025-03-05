import logging
from Assert import Assert
from TermColor import TermColor


class Report:
    def __init__(self):
        self.__entries = list()
        self.logger = logging.getLogger(__name__)
        self.pass_str = "PASS" 
        self.fail_str = "FAIL"

    def __summary(self, entries, level, max_level, color):
        all_evals = True
        output = ""
        if color:
            pass_str = f"{TermColor.OKGREEN}{self.pass_str}{TermColor.ENDC}"
            fail_str = f"{TermColor.FAIL}{self.fail_str}{TermColor.ENDC}"
        else:
            pass_str = self.pass_str
            fail_str = self.fail_str

        if max_level is None or level <= max_level:
            for entry in entries:
                if isinstance(entry, Report):
                    status, summary = self.__summary(entry.__entries, level + 1, max_level, color)
                    output += summary
                    all_evals = all_evals and status
                elif isinstance(entry, Assert):
                    status, msg = entry.result(color)
                    output += "  " * level + f'{pass_str if status else fail_str}: {msg}\n'
                    all_evals = all_evals and status
                else:
                    raise NotImplementedError

        return all_evals, output

    def summary(self, max_level=None, color=False):
        return self.__summary(self.__entries, 0, max_level, color)

    def __str__(self):
        _, summary =  self.__summary(entries=self.__entries, level=0, max_level=None, color=False)
        return summary

    def add(self, entry):
        assert isinstance(entry, Assert) or type(entry) is Report
        self.__entries.append(entry)


