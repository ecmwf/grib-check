#!/usr/bin/env python3

import os
import glob

def scan(name, validate):
    if os.path.isdir(name):
        for path in glob.glob(name + '/*'):
            scan(path, validate)
    else:
        validate(name);
