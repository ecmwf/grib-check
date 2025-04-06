import logging
from Assert import Assert
from TermColor import TermColor
import numpy as np

class RWarning:
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return self.__msg


class RError:
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return self.__msg


class Report:
    def __init__(self, name=None):
        self.__entries = list()
        self.__logger = logging.getLogger(__name__)
        self.__pass_str = "PASS" 
        self.__fail_str = "FAIL"
        self.__none_str = "NONE"
        self.__status = None
        self.__name = name

    def __as_string(self, entries, level, max_level, color, failed_only):
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
                    if not failed_only:
                        output = "  " * level + f'{none_str}: {self.__name}\n'
                elif self.__status is True:
                    if not failed_only:
                        output = "  " * level + f'{pass_str}: {self.__name}\n'
                elif self.__status is False:
                    output = "  " * level + f'{fail_str}: {self.__name}\n'
                else:
                    print(f"self.__status={self.__status}, type={type(self.__status)}")
                    raise NotImplementedError

                shift = 1

            if max_level is None or level + shift <= max_level:
                for entry in entries:
                    if isinstance(entry, Report):
                        output += entry.__as_string(entry.__entries, level + shift, max_level, color, failed_only)
                    elif isinstance(entry, Assert):
                        msg = entry.as_string(color)
                        status = entry.status()
                        if not failed_only or not status:
                            # output += "  " * (level + shift) + f'{pass_str if status else fail_str}: {msg}\n'
                            tmp = "  " * (level + shift) + f'{pass_str if status else fail_str}: {msg}'
                            tmp = tmp.replace("\n", f'\n      {"  " * (level + shift)}')
                            output += f"{tmp}\n"
                    elif type(entry) is str:
                        if not failed_only:
                            output += "  " * (level + shift) + f"{entry}\n"
                    else:
                        raise NotImplementedError

        return output


    def __as_string_long(self, entries, color, failed_only, path):
        output = ""
        sep = " <- "

        for entry in entries:
            if isinstance(entry, Report):
                if entry.__name is not None:
                    if color:
                        path += f"{TermColor.SEP}{sep}{TermColor.ENDC}{TermColor.SEP}{TermColor.OKCYAN}{entry.__name}{TermColor.ENDC}"
                    else:
                        path += f"{sep}{entry.__name}"
                    # path += f"{sep}{entry.__name}"
                output += self.__as_string_long(entry.__entries, color, failed_only, path)
            elif isinstance(entry, Assert):
                if color:
                    output += f"{path}{TermColor.SEP}{sep}{TermColor.ENDC}{entry.as_string(color)}\n"
                elif entry.status() is True:
                    output += f"{path}{sep}{entry.as_string(color)}\n"
            elif type(entry) is str:
                if color:
                    output += f"{path}{TermColor.SEP}{sep}{TermColor.ENDC}{entry}\n"
                else:
                    output += f"{path}{sep}{entry}\n"
            else:
                raise NotImplementedError

        return output


    def rename(self, name):
        self.__name = name

    def rename_anonymous_report(self, name):
        if self.__name is None:
            self.__name = name

    def as_string(self, max_level=None, color=False, failed_only=False, format=None):
        if format == "short":
            path = ""
            if color:
                pass_str = f"{TermColor.OKGREEN}{self.__pass_str}{TermColor.ENDC}"
                fail_str = f"{TermColor.FAIL}{self.__fail_str}{TermColor.ENDC}"
                none_str = f"{TermColor.OKCYAN}{self.__none_str}{TermColor.ENDC}"
            else:
                pass_str = self.__pass_str
                fail_str = self.__fail_str
                none_str = self.__none_str

            if self.__name is not None:
                if self.__status is None:
                    if not failed_only:
                        if color:
                            path = f'{none_str}: {TermColor.OKCYAN}{self.__name}{TermColor.ENDC}'
                        else:
                            path = f'{none_str}: {self.__name}'
                elif self.__status is True:
                    if not failed_only:
                        if color:
                            path = f'{pass_str}: {TermColor.OKCYAN}{self.__name}{TermColor.ENDC}'
                        else:
                            path = f'{pass_str}: {self.__name}'
                elif self.__status is False:
                    if color:
                        path = f'{fail_str}: {TermColor.OKCYAN}{self.__name}{TermColor.ENDC}'
                    else:
                        path = f'{fail_str}: {self.__name}'
                else:
                    print(f"self.__status={self.__status}, type={type(self.__status)}")
                    raise NotImplementedError


            return self.__as_string_long(self.__entries, color, failed_only, path)
        elif format == "tree":
            return self.__as_string(self.__entries, 0, max_level, color, failed_only)
        else:
            raise NotImplementedError(f"Unknown format: {format}")

    def status(self):
        return self.__status

    def __str__(self):
        return self.__as_string(entries=self.__entries, level=0, max_level=None, color=False, failed_only=False)

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
        elif type(entry) is RWarning:
            self.__status = self.__status or None
        elif type(entry) is RError:
            self.__status = self.__status or False
        elif type(entry) is str:
            self.__status = None
            pass

        assert type(self.__status) is bool or type(self.__status) is np.bool_ or self.__status is None
        self.__entries.append(entry)

    def error(self, msg):
        # TODO: Implement error handling
        self.add(RError(msg))

    def warning(self, entry):
        # TODO: Implement warning handling
        self.add(RWarning(entry))


