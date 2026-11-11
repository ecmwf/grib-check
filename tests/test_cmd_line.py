#!/usr/bin/env python3

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"


def _run_grib_check(*args):
    # Run with the interpreter executing the tests and make the in-tree package importable,
    # so the test does not depend on grib_check being installed or on PYTHONPATH/cwd.
    env = os.environ.copy()
    env["PYTHONPATH"] = os.pathsep.join(p for p in [str(SRC_DIR), env.get("PYTHONPATH")] if p)
    return subprocess.run(
        [sys.executable, "-m", "grib_check.GribCheck", *args],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
        env=env,
    )


class TestCmdLine:
    def test_cmd_line_pass(self):
        result = _run_grib_check("-c", "./tests/tigge/tigge_ecmf_sfc_10v.grib", "-C", "tigge")
        assert result.returncode == 0, result.stderr

    def test_cmd_line_fail(self):
        result = _run_grib_check("-c", "./tests/tigge/tigge_ecmf_sfc_10v.grib", "-C", "crra")
        assert result.returncode == 1, result.stderr
        # Exit code 1 must come from failed checks, not from a crash (which also exits with 1).
        assert "Traceback" not in result.stderr, result.stderr
