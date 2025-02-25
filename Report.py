import logging

logger = logging.getLogger(__name__)

class Report:
    def __init__(self):
        self.__entries = list()
   
    def __summary(self, entries, level, max_level):
        output = ""
        if max_level is None or level <= max_level:
            for entry in entries:
                if isinstance(entry, Report):
                    output += self.__summary(entry.__entries, level + 1, max_level)
                else:
                    output += "  " * level + entry + "\n"
        return output

    def summary(self, max_level=None):
        return self.__summary(self.__entries, 0, max_level)

    def __str__(self):
        return self.__summary(self.__entries, 0, None)

    def add(self, entry):
        assert type(entry) is str or type(entry) is Report
        self.__entries.append(entry)


