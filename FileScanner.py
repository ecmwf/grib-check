#!/usr/bin/env python3

import os

class FileScanner:
    def __init__(self, paths):
        self.fns = []
        for path in paths:
            if os.path.isdir(path):
                for root, dirs, fns in os.walk(path):
                    for fn in fns:
                        self.fns.append(root + '/' + fn)
            else:
                self.fns.append(path)
        # print(self.fns)

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self) -> str:
        if self.pos < len(self.fns):
            fn = self.fns[self.pos]
            self.pos += 1
            return fn
        else:
            raise StopIteration
