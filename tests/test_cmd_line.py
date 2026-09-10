#!/usr/bin/env python3

import subprocess


class TestCmdLine:
    def test_cmd_line_pass(self):
        result = subprocess.run(
            ["python3", "-m", "grib_check.GribCheck", "-c", "./tests/tigge/tigge_ecmf_sfc_10v.grib", "-C", "tigge"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0

    def test_cmd_line_fail(self):
        result = subprocess.run(
            ["python3", "-m", "grib_check.GribCheck", "-c", "./tests/tigge/tigge_ecmf_sfc_10v.grib", "-C", "crra"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 1
