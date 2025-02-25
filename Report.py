import logging

logger = logging.getLogger(__name__)

class Report:
    def __init__(self):
        self.__entries = list()
   
    def __print(self, entries, level):
        output = ""
        for entry in entries:
            if isinstance(entry, Report):
                output += self.__print(entry.__entries, level + 1)
            else:
                output += "  " * level + entry + "\n"
        return output

    def __str__(self):
        return self.__print(self.__entries, 0)

    def add(self, entry):
        assert type(entry) is str or type(entry) is Report
        self.__entries.append(entry)


