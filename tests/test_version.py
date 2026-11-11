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

Both checks only run on release and hotfix branches (``release/*`` and
``hotfix/*``), where the version is expected to be bumped. On all other
branches they are skipped, so they never fail there.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Tuple

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
PYPROJECT = REPO_ROOT / "pyproject.toml"
GRIBCHECK_PY = REPO_ROOT / "src" / "grib_check" / "GribCheck.py"
RELEASE_BRANCH_PREFIXES = ("release/", "hotfix/")


def _is_release_branch(branch: str | None) -> bool:
    """Branches on which the version must have been bumped: ``release/*`` and ``hotfix/*``."""
    return branch is not None and branch.startswith(RELEASE_BRANCH_PREFIXES)


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


def _current_branch() -> str | None:
    """Return the name of the branch being tested, or ``None`` if unknown.

    On GitHub Actions the checkout is often a detached HEAD, so the branch is
    taken from the CI environment: ``GITHUB_HEAD_REF`` is the source branch of
    a pull request, ``GITHUB_REF_NAME`` the branch of a push. Otherwise the
    current branch of the local git checkout is used.
    """
    for var in ("GITHUB_HEAD_REF", "GITHUB_REF_NAME"):
        branch = os.environ.get(var, "").strip()
        if branch:
            return branch

    if shutil.which("git") is None:
        return None
    try:
        result = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

    branch = result.stdout.strip()
    return None if branch in ("", "HEAD") else branch


_BRANCH = _current_branch()

# Version checks are only enforced on release and hotfix branches; skip them everywhere else.
pytestmark = pytest.mark.skipif(
    not _is_release_branch(_BRANCH),
    reason=(
        f"not on a release or hotfix branch ({_BRANCH!r}); version checks only run on "
        f"{' and '.join(p + '*' for p in RELEASE_BRANCH_PREFIXES)}"
    ),
)


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
        else:
            current_version = _read_pyproject_version()
            current = _version_tuple(current_version)
            latest = _version_tuple(latest_tag)

            assert current > latest, (
                f"version in pyproject.toml ({current_version!r}) is not greater "
                f"than the latest release tag ({latest_tag!r}). Bump the version "
                "in pyproject.toml (and GribCheck.py) before merging."
            )
