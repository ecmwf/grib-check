#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#


class TermColor:
    """
    ANSIescapecodesforterminalcolors.
    """

    # ANSI escape codes for text colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # ANSI escape codes for background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    # Bright colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    # Bright background colors
    BRIGHT_BG_BLACK = "\033[100m"
    BRIGHT_BG_RED = "\033[101m"
    BRIGHT_BG_GREEN = "\033[102m"
    BRIGHT_BG_YELLOW = "\033[103m"
    BRIGHT_BG_BLUE = "\033[104m"
    BRIGHT_BG_MAGENTA = "\033[105m"
    BRIGHT_BG_CYAN = "\033[106m"
    BRIGHT_BG_WHITE = "\033[107m"

    # ANSI escape code to reset color│
    RESET = "\033[0m"

    # ANSI escape codes for text styles
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    REVERSED = "\033[7m"

    OKGREEN = BRIGHT_GREEN
    OKCYAN = BRIGHT_MAGENTA
    OKBLUE = BRIGHT_BLUE
    FAIL = BRIGHT_RED
    ENDC = RESET
    SEP = WHITE
