#!/usr/bin/env python3

import subprocess


class TestCmdLine:
    def test_cmd_line_pass(self):
        result = subprocess.run(
            ["python3", "-m", "grib_check.GribCheck", "-c", "./tests/crra/crra_an_no-ar-pa_pl_ws.grib", "-C", "crra"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0

    def test_cmd_line_fail(self):
        result = subprocess.run(
            ["python3", "-m", "grib_check.GribCheck", "-c", "./tests/crra/crra_an_no-ar-pa_pl_ws.grib", "-C", "uerra"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 1
