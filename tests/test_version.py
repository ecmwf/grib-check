#!/usr/bin/env python3
"""Version consistency and release-monotonicity checks.

These tests protect against forgetting to bump the version, or bumping it in
only one of the places it is declared.

They verify that:
    1. The version declared in ``pyproject.toml`` matches the version string
       hard-coded in the ``grib-check`` CLI (``GribCheck.py``).
    2. The version declared in ``pyproject.toml`` is strictly greater than the
       latest release tag in the git repository (i.e. the version has been
       bumped since the last release).
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path
from typing import Tuple

import pytest


REPO_ROOT = Path(__file__).resolve().parent.parent
PYPROJECT = REPO_ROOT / "pyproject.toml"
GRIBCHECK_PY = REPO_ROOT / "src" / "grib_check" / "GribCheck.py"


# Match a PEP 440-ish release version: N(.N)*, optionally followed by
# pre/post/dev segments. Kept intentionally simple – if we ever start using
# richer versioning we can swap in ``packaging.version.Version``.
_VERSION_RE = re.compile(r"\d+(?:\.\d+)+(?:[.\-]?(?:a|b|rc|dev|post)\d+)?")


def _version_tuple(version: str) -> Tuple[int, ...]:
    """Return a tuple of the numeric release components for comparison.

    This is deliberately conservative: it only looks at the numeric release
    segment (``1.2.3``) so that ``0.1.2`` and ``0.1.2.dev0`` compare as equal
    on the release segment. That's fine here because we only compare against
    release tags.
    """
    match = re.match(r"(\d+(?:\.\d+)*)", version)
    assert match, f"cannot parse version: {version!r}"
    return tuple(int(part) for part in match.group(1).split("."))


def _read_pyproject_version() -> str:
    text = PYPROJECT.read_text(encoding="utf-8")
    # Match a top-level ``version = "X.Y.Z"`` line in the [project] table.
    # We restrict to a single-line, double-quoted string, which is what the
    # current pyproject.toml uses.
    match = re.search(
        r'(?m)^\s*version\s*=\s*"([^"]+)"\s*$',
        text,
    )
    assert match, "could not find `version = \"...\"` in pyproject.toml"
    return match.group(1)


def _read_gribcheck_cli_version() -> str:
    text = GRIBCHECK_PY.read_text(encoding="utf-8")
    # Match the ``--version`` action, e.g. ``version="%(prog)s 0.1.2"``.
    match = re.search(
        r'version\s*=\s*"%\(prog\)s\s+([^"\s]+)"',
        text,
    )
    assert match, (
        "could not find argparse --version string in GribCheck.py; "
        "expected something like `version=\"%(prog)s X.Y.Z\"`"
    )
    return match.group(1)


def _latest_release_tag() -> str | None:
    """Return the latest release tag as a version string, or ``None``.

    Returns ``None`` (rather than failing) when git is unavailable, this is not
    a git checkout, or no tags are present (e.g. a shallow CI clone without
    ``fetch-tags``). The intent of this test is to catch forgotten version
    bumps in normal developer workflows; it should not block CI in
    environments where tag history is not available.
    """
    if shutil.which("git") is None:
        return None
    try:
        result = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "tag", "--list", "--sort=-v:refname"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

    for line in result.stdout.splitlines():
        tag = line.strip().lstrip("v")
        if _VERSION_RE.fullmatch(tag):
            return tag
    return None


class TestVersion:
    def test_pyproject_and_cli_versions_match(self):
        pyproject_version = _read_pyproject_version()
        cli_version = _read_gribcheck_cli_version()
        assert pyproject_version == cli_version, (
            f"version in pyproject.toml ({pyproject_version!r}) does not match "
            f"the version hard-coded in GribCheck.py ({cli_version!r}). "
            "Bump both when releasing."
        )

    def test_version_bumped_since_last_release(self):
        latest_tag = _latest_release_tag()
        if latest_tag is None:
            pytest.skip(
                "no git tags available (not a git checkout, git missing, or "
                "tags not fetched); skipping release-monotonicity check"
            )

        current_version = _read_pyproject_version()
        current = _version_tuple(current_version)
        latest = _version_tuple(latest_tag)

        assert current > latest, (
            f"version in pyproject.toml ({current_version!r}) is not greater "
            f"than the latest release tag ({latest_tag!r}). Bump the version "
            "in pyproject.toml (and GribCheck.py) before merging."
        )
