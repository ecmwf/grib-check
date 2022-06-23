#!/usr/bin/env python3

from pathlib import Path
import os

def scan(name, validate):
    if os.path.isdir(name):
        for path in Path(os.path.dirname(name)).rglob('/*'):
            scan(path, validate)
    else:
        validate(name);
