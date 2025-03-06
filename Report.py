import logging
from Assert import Assert
from TermColor import TermColor


class Report:
    def __init__(self, name=None):
        self.__entries = list()
        self.__logger = logging.getLogger(__name__)
        self.__pass_str = "PASS" 
        self.__fail_str = "FAIL"
        self.__none_str = "NONE"
        self.__status = None
        self.__name = name

    def __as_string(self, entries, level, max_level, color):
        shift = 0
        output = ""
        if color:
            pass_str = f"{TermColor.OKGREEN}{self.__pass_str}{TermColor.ENDC}"
            fail_str = f"{TermColor.FAIL}{self.__fail_str}{TermColor.ENDC}"
            none_str = f"{TermColor.OKCYAN}{self.__none_str}{TermColor.ENDC}"
        else:
            pass_str = self.__pass_str
            fail_str = self.__fail_str
            none_str = self.__none_str


        if max_level is None or level <= max_level:
            if self.__name is not None:
                if self.__status is None:
                    output = "  " * level + f'{none_str}: {self.__name}\n'
                elif self.__status is True:
                    output = "  " * level + f'{pass_str}: {self.__name}\n'
                elif self.__status is False:
                    output = "  " * level + f'{fail_str}: {self.__name}\n'
                else:
                    raise NotImplementedError

                shift = 1

            if max_level is None or level + shift <= max_level:
                for entry in entries:
                    if isinstance(entry, Report):
                        output += entry.__as_string(entry.__entries, level + shift, max_level, color)
                    elif isinstance(entry, Assert):
                        msg = entry.as_string(color)
                        status = entry.status()
                        output += "  " * (level + shift) + f'{pass_str if status else fail_str}: {msg}\n'
                    elif type(entry) is str:
                        output += "  " * (level + shift) + f"{entry}\n"
                    else:
                        raise NotImplementedError

        return output

    def rename(self, name):
        self.__name = name

    def as_string(self, max_level=None, color=False):
        return self.__as_string(self.__entries, 0, max_level, color)

    def status(self):
        return self.__status

    def __str__(self):
        return self.__as_string(entries=self.__entries, level=0, max_level=None, color=False)

    def add(self, entry):
        assert isinstance(entry, Assert) or type(entry) is Report or type(entry) is str
        if isinstance(entry, Assert):
            if self.__status is None:
                self.__status = entry.status()
            else:
                if entry.status() is not None:
                    self.__status = self.__status and entry.status()
        elif isinstance(entry, Report):
            if self.__status is None:
                self.__status = entry.status()
            else:
                if entry.status() is not None:
                    self.__status = self.__status and entry.status()
        elif type(entry) is str:
            pass

        self.__entries.append(entry)


