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

import numpy as np

from .Assert import Assert
from .TermColor import TermColor


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
        self.__none_str = "----"
        self.__status = None
        self.__name = name

    def __as_string_tree(self, entries, level, max_level, color, failed_only):
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
                        output = "  " * level + f"{none_str}: {self.__name}\n"
                elif self.__status is True or self.__status is np.bool_(True):
                    if not failed_only:
                        output = "  " * level + f"{pass_str}: {self.__name}\n"
                elif self.__status is False or self.__status is np.bool_(False):
                    output = "  " * level + f"{fail_str}: {self.__name}\n"
                else:
                    print(f"self.__status={self.__status}, type={type(self.__status)}")
                    raise NotImplementedError

                shift = 1

            if max_level is None or level + shift <= max_level:
                for entry in entries:
                    if isinstance(entry, Report):
                        output += entry.__as_string_tree(
                            entry.__entries,
                            level + shift,
                            max_level,
                            color,
                            failed_only,
                        )
                    elif isinstance(entry, Assert):
                        msg = entry.as_string(color)
                        status = bool(entry)
                        if not failed_only or not status:
                            # output += "  " * (level + shift) + f'{pass_str if status else fail_str}: {msg}\n'
                            tmp = (
                                "  " * (level + shift)
                                + f"{pass_str if status else fail_str}: {msg}"
                            )
                            tmp = tmp.replace("\n", f'\n      {"  " * (level + shift)}')
                            output += f"{tmp}\n"
                    elif type(entry) is str:
                        if not failed_only:
                            output += "  " * (level + shift) + f"{entry}\n"
                    else:
                        raise NotImplementedError

        return output

    def __as_string_short(self, report, color, failed_only, path):
        output = ""
        sep = " <- "

        if color:
            pass_str = f"{TermColor.OKGREEN}{self.__pass_str}{TermColor.ENDC}"
            fail_str = f"{TermColor.FAIL}{self.__fail_str}{TermColor.ENDC}"
            none_str = f"{TermColor.OKCYAN}{self.__none_str}{TermColor.ENDC}"
        else:
            pass_str = self.__pass_str
            fail_str = self.__fail_str
            none_str = self.__none_str

        if report.__name is not None:
            if color:
                path += f"{TermColor.OKCYAN}{report.__name}{TermColor.ENDC}{TermColor.SEP}{sep}{TermColor.ENDC}"
            else:
                path += f"{report.__name}{sep}"

        for entry in report.__entries:
            if isinstance(entry, Report):
                output += self.__as_string_short(entry, color, failed_only, path)
            elif isinstance(entry, Assert):
                status = bool(entry)
                if not failed_only or not status:
                    if status is True:
                        if color:
                            output += (
                                f"{pass_str}: {path}{entry.as_string(color, 'right')}\n"
                            )
                        else:
                            output += (
                                f"{pass_str}: {path}{entry.as_string(color, 'right')}\n"
                            )
                    elif status is False:
                        if color:
                            output += (
                                f"{fail_str}: {path}{entry.as_string(color, 'right')}\n"
                            )
                        else:
                            output += (
                                f"{fail_str}: {path}{entry.as_string(color, 'right')}\n"
                            )
                    else:
                        raise NotImplementedError
                # output += f"{path}{entry.as_string(color, comment_position='right')}\n"
            elif type(entry) is str:
                if not failed_only:
                    output += f"{none_str}: {path}{entry}\n"
            else:
                raise NotImplementedError

        return output

    def rename(self, name):
        self.__name = name

    def rename_anonymous_report(self, name):
        if self.__name is None:
            self.__name = name

    def as_string(self, max_level=None, color=False, failed_only=False, output_type=None):
        if output_type == "short":
            return self.__as_string_short(self, color, failed_only, "")
        elif output_type == "tree":
            return self.__as_string_tree(
                self.__entries, 0, max_level, color, failed_only
            )
        else:
            raise NotImplementedError(f"Unknown format: {output_type}")

    def status(self):
        return self.__status

    def __str__(self):
        return self.__as_string_tree(
            entries=self.__entries,
            level=0,
            max_level=None,
            color=False,
            failed_only=False,
        )

    def add(self, entry):
        if not (
            isinstance(entry, Assert) or type(entry) is Report or type(entry) is str
        ):
            print(f"entry={entry}, type={type(entry)}")
        assert isinstance(entry, Assert) or type(entry) is Report or type(entry) is str
        if isinstance(entry, Assert):
            if self.__status is None:
                self.__status = bool(entry)
            else:
                if bool(entry) is False:
                    self.__status = False
        elif isinstance(entry, Report):
            if self.__status is None:
                self.__status = entry.status()
            elif entry.status() is False:
                self.__status = False
            else:
                if entry.status() is not None:
                    self.__status = self.__status and entry.status()
        elif type(entry) is str:
            pass

        assert type(self.__status) is bool or type(self.__status) is np.bool_ or self.__status is None, f"self.__status={self.__status}, type={type(self.__status)}"

        self.__entries.append(entry)

        return self

    def error(self, msg):
        # TODO: Implement error handling
        self.add(RError(msg))

    def warning(self, entry):
        # TODO: Implement warning handling
        self.add(RWarning(entry))
