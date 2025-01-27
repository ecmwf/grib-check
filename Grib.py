from eccodes import (
    codes_grib_new_from_file,
)

from Message import Message


class Grib:
    def __init__(self, path):
        self.__error = 0
        try:
            self.f = open(path, "rb")
        except Exception as e:
            print("%s: %s" % (path, str(e)))
            self.__error += 1
            return

    def __del__(self):
        self.f.close()

    def __iter__(self):
        self.position = 0
        return self

    def __next__(self):
        handle = codes_grib_new_from_file(self.f)
        if handle is not None:
            self.position += 1
            return Message(handle, self.position)
        else:
            raise StopIteration
