#!/bin/bash
#
# Build and install ecCodes together with its dependencies and Python tools,
# all from source (GitHub):
#
#   ecbuild         CMake macros used by eckit and ecCodes
#   eckit           optional (--enable-eckit), used by ecCodes (eckit geo)
#   eccodes         the ecCodes library and tools
#   eccodes-python  installed into a Python venv
#   grib-check      installed into the same venv
#
# Usage: eccodes_install.sh --rootdir <dir> [options]
#
# --rootdir is the only required option; run with --help for the others.
# Every package can be set to a branch or tag; without one, its latest
# release tag is used. The build of ecCodes is derived from the options
# (--compiler, --enable-eckit).
#
# Directory layout (ROOTDIR: given with --rootdir):
#
#   $ROOTDIR/git/<package>          sources
#   $ROOTDIR/build/<package>        build directories (eckit, eccodes)
#   $ROOTDIR/install/<package>      installations (eckit, eccodes)
#   $ROOTDIR/venv                   Python venv with eccodes-python, grib-check
#   $ROOTDIR/load_env               loads the environment
#   $ROOTDIR/unload_env             unloads it again
#   $ROOTDIR/eccodes_install.state  progress (restart point)
#
# The installation runs as a list of steps. The progress is saved after every
# successful step, so a failed installation can be resumed by re-running the
# same command. If the configuration of eckit or ecCodes changes (ref,
# compiler, eckit), its build and install directories are cleaned first.
#
# Possible preparation (missing tools and a missing AEC library are also
# loaded automatically as modules, see TOOL_MODULES and AEC_MODULES below):
#   module load gcc/15.2.0 aec/1.1.4 netcdf4/4.9.3 cdo
#   eval `ssh-agent -s`      # only for --git-protocol ssh

# Stop on the first error. -E: the ERR trap is inherited by functions and
# subshells.
set -eE -o pipefail


###############################################################################
# Configuration
###############################################################################

# Packages that can be selected with --branch/--tag (= repository names)
PACKAGES=(ecbuild eckit eccodes eccodes-python grib-check)

# Tags that count as releases when looking for the latest tag of a package:
# plain version numbers like 2.48.3. This excludes pre-releases (2.0.0-rc1,
# 1.13.0a1), named tags (magics) and the old date-based tags of ecbuild and
# eckit (2021.08.0), which would otherwise sort above the current releases.
RELEASE_TAG_REGEX='^[0-9]{1,3}(\.[0-9]+)*$'

CMAKE_BUILD_TYPE="RelWithDebInfo"

# Settings that can be changed on the command line (see usage). ROOTDIR has
# no default and must be given with --rootdir.
ROOTDIR=""               # --rootdir: sources, builds and installations
COMPILER="gcc"           # --compiler: gcc or clang (C/C++; Fortran: gfortran)
ENABLE_ECKIT=0           # --enable-eckit: install eckit, build ecCodes with it
GIT_PROTOCOL="https"     # --git-protocol: https or ssh
JOBS=$(nproc 2>/dev/null || echo 4)   # --jobs: parallel build jobs (available cores)
PYTHON="python3"         # --python: Python used to create the venv

# Minimum Python version (grib-check: requires-python >= 3.8; the findlibs
# package used by eccodes-python does not run on older versions)
PYTHON_MIN_VERSION="3.8"

# Modules tried with 'module load' (in this order) if a required tool is not
# found. Tools without an entry are tried as a module of the same name.
declare -A TOOL_MODULES=(
    [git]="git"
    [cmake]="cmake"
    [make]="make"
    [gcc]="gcc"
    [g++]="gcc"
    [gfortran]="gcc"
    [clang]="clang llvm"
    [clang++]="clang llvm"
    [python3]="python3 python"
)

# Modules tried with 'module load' (in this order) if ecCodes cannot find the
# AEC library (libaec) it requires, e.g. because only an older system version
# is installed. Their default versions are used.
AEC_MODULES=(aec libaec)

# Scripts that define the 'module' command (Environment Modules, Lmod), used
# if it is not already defined ($MODULESHOME/init/bash is tried first)
MODULE_INIT_SCRIPTS=(
    /etc/profile.d/modules.sh
    /etc/profile.d/lmod.sh
    /usr/share/lmod/lmod/init/bash
    /usr/share/Modules/init/bash
)


###############################################################################
# Global state (filled in by the functions below)
###############################################################################

# Command line arguments, for the resume message
ORIG_ARGS=""
if [ $# -gt 0 ]; then ORIG_ARGS=$(printf '%q ' "$@"); fi

# Selected ref of every package: PKG_KIND[<package>]=branch|tag and
# PKG_REF[<package>]=<name>
declare -A PKG_KIND=() PKG_REF=()

# Installation steps: name (shown in messages) and command
STEP_NAMES=()
STEP_CMDS=()

# Progress
RESTART=0
COMPLETED=0
AEC_CHECKED=0            # 1: check_aec succeeded (see check_aec_once)
CURRENT_STEP=""
FAILED_CMD=""
FAILED_LINE=""
FAILED_MSG=""


###############################################################################
# General helpers
###############################################################################

# die <message>: print an error and exit (the message is repeated on failure)
function die() {
    FAILED_MSG=$1
    echo "$1" >&2
    exit 1
}

# banner <text>: status message
function banner() {
    echo
    echo "########## $* ##########"
    echo
}

# source_quietly <file>: source a file without tracing its contents (set -x);
# returns the exit status of the sourced file
function source_quietly() {
    local xtrace=0 rc=0
    if [[ $- == *x* ]]; then xtrace=1; fi
    { set +x; } 2>/dev/null
    source "$1" || rc=$?
    if [ ${xtrace} = 1 ]; then set -x; fi
    return ${rc}
}

# libdir_of <prefix>: <prefix>/lib64 if it exists, otherwise <prefix>/lib
function libdir_of() {
    if [ -d "$1/lib64" ]; then echo "$1/lib64"; else echo "$1/lib"; fi
}


###############################################################################
# Directory layout
###############################################################################

function src_dir()        { echo "${ROOTDIR}/git/$1"; }       # <package>
function build_dir()      { echo "${ROOTDIR}/build/$1"; }     # <package>
function prefix_dir()     { echo "${ROOTDIR}/install/$1"; }   # <package>
function venv_dir()       { echo "${ROOTDIR}/venv"; }
function load_env_file()  { echo "${ROOTDIR}/load_env"; }
function unload_env_file(){ echo "${ROOTDIR}/unload_env"; }
function state_file()     { echo "${ROOTDIR}/eccodes_install.state"; }


###############################################################################
# Command line
###############################################################################

function usage() {
    cat <<END_OF_USAGE
Usage: $(basename "$0") --rootdir <dir> [options]

Required:
  --rootdir <dir>              Directory for sources, builds and installations

Options:
  --branch <package>/<branch>  Use a branch of <package>.
                               A GitHub pull request can be selected with
                               pr-<number>, e.g. --branch eccodes/pr-123
  --tag <package>/<tag>        Use a tag of <package>, e.g. --tag eccodes/2.48.3
  --compiler gcc|clang         C/C++ compiler for eckit and ecCodes
                               (default: ${COMPILER}; Fortran: gfortran)
  --enable-eckit               Install eckit and build ecCodes with it
                               (default: eckit is not installed)
  --git-protocol https|ssh     Protocol for cloning from GitHub (default: ${GIT_PROTOCOL})
  --jobs <n>                   Number of parallel build jobs (default: ${JOBS},
                               the number of available cores)
  --python <python>            Python used to create the venv (default: ${PYTHON})
  --restart                    Ignore the saved progress and install everything
                               from the beginning
  -h, --help                   Show this help

Options with a value can also be written as --option=value.

Packages: ${PACKAGES[*]}

Every package accepts at most one --branch or --tag. A package without one
uses its latest release tag (the highest version number, e.g. 2.48.3;
pre-releases like 2.0.0-rc1 are ignored). A --branch/--tag for eckit requires
--enable-eckit.

ecCodes is installed in <rootdir>/install/eccodes. If the ref, the compiler or
--enable-eckit differ from the previous installation, the build and install
directories are cleaned and ecCodes is rebuilt from scratch.

The progress is saved after every successfully installed step. If a step
fails, fix the problem and re-run the same command: the installation resumes
at the failed step.

Examples:
  $(basename "$0") --rootdir /tmp/\$USER
  $(basename "$0") --rootdir \$LOCALSSD/\$USER --tag eccodes/2.48.3 --enable-eckit --tag eckit/2.3.0
  $(basename "$0") --rootdir ~/ecmwf --branch eccodes/develop --compiler clang
END_OF_USAGE
}

# is_package <name>: true if <name> is one of PACKAGES
function is_package() {
    local p
    for p in "${PACKAGES[@]}"; do
        if [ "${p}" = "$1" ]; then return 0; fi
    done
    return 1
}

# is_enabled <package>: true if <package> is installed (eckit is optional)
function is_enabled() {
    if [ "$1" = "eckit" ]; then
        [ "${ENABLE_ECKIT}" = 1 ]
    else
        is_package "$1"
    fi
}

# add_ref <branch|tag> <package>/<ref>: store one --branch/--tag option
function add_ref() {
    local kind=$1 spec=$2
    local pkg=${spec%%/*}
    local ref=${spec#*/}

    if [[ "${spec}" != */* ]] || [ -z "${pkg}" ] || [ -z "${ref}" ]; then
        die "Invalid --${kind} '${spec}': expected <package>/<${kind}>"
    fi
    if ! is_package "${pkg}"; then
        die "Unknown package '${pkg}' in --${kind} ${spec}. Allowed packages: ${PACKAGES[*]}"
    fi
    if [ -n "${PKG_REF[${pkg}]:-}" ]; then
        die "Only one --branch/--tag allowed for ${pkg} (already set: --${PKG_KIND[${pkg}]} ${pkg}/${PKG_REF[${pkg}]})"
    fi
    PKG_KIND[${pkg}]=${kind}
    PKG_REF[${pkg}]=${ref}
}

# check_choice <option> <value> <allowed values...>: check the value of an option
function check_choice() {
    local opt=$1 value=$2 allowed
    shift 2
    for allowed in "$@"; do
        if [ "${value}" = "${allowed}" ]; then return 0; fi
    done
    die "Invalid ${opt} '${value}': use $(printf '%s\n' "$@" | paste -sd '|')"
}

function parse_args() {
    local opt value inline_value

    while [ $# -gt 0 ]; do
        opt=$1
        shift

        # --option=value is handled like --option value
        inline_value=0
        if [[ "${opt}" == --*=* ]]; then
            set -- "${opt#*=}" "$@"
            opt=${opt%%=*}
            inline_value=1
        fi

        # Options with a value
        case "${opt}" in
            --rootdir|--branch|--tag|--compiler|--git-protocol|--jobs|--python)
                if [ $# -eq 0 ]; then die "${opt} requires a value (see --help)"; fi
                value=$1
                shift
                ;;
            --restart|--enable-eckit|-h|--help)
                if [ ${inline_value} = 1 ]; then die "${opt} does not take a value"; fi
                ;;
        esac

        case "${opt}" in
            --rootdir)       ROOTDIR=${value} ;;
            --branch|--tag)  add_ref "${opt#--}" "${value}" ;;
            --compiler)      check_choice "${opt}" "${value}" gcc clang; COMPILER=${value} ;;
            --enable-eckit)  ENABLE_ECKIT=1 ;;
            --git-protocol)  check_choice "${opt}" "${value}" https ssh; GIT_PROTOCOL=${value} ;;
            --jobs)
                if [[ ! "${value}" =~ ^[1-9][0-9]*$ ]]; then
                    die "Invalid --jobs '${value}': expected a positive number"
                fi
                JOBS=${value}
                ;;
            --python)        PYTHON=${value} ;;
            --restart)       RESTART=1 ;;
            -h|--help)       usage; exit 0 ;;
            *)               usage >&2; die "Unknown argument: ${opt}" ;;
        esac
    done

    if [ -z "${ROOTDIR}" ]; then
        usage >&2
        die "Missing required option: --rootdir <dir>"
    fi
    if [ "${ENABLE_ECKIT}" = 0 ] && [ -n "${PKG_REF[eckit]:-}" ]; then
        die "--${PKG_KIND[eckit]} eckit/${PKG_REF[eckit]} requires --enable-eckit"
    fi
}


###############################################################################
# Required tools
###############################################################################

# check_not_loaded: refuse to install from a shell with a loaded environment,
# which could otherwise leak into the builds (PATH, LD_LIBRARY_PATH, venv)
function check_not_loaded() {
    if [ -n "${ECCODES_INSTALL_ROOT:-}" ]; then
        die "The ecCodes environment of ${ECCODES_INSTALL_ROOT} is loaded in this shell. Unload it first: source ${ECCODES_INSTALL_ROOT}/unload_env"
    fi
}

# compilers: the C and C++ compiler of COMPILER, e.g. "gcc g++"
function compilers() {
    case "${COMPILER}" in
        gcc)   echo "gcc g++" ;;
        clang) echo "clang clang++" ;;
    esac
}

# required_tools: programs needed by the installation (one per line)
function required_tools() {
    printf '%s\n' git cmake make $(compilers)
    echo gfortran             # ecCodes is built with Fortran support
    echo "${PYTHON}"
}

# python_version <python>: major.minor version of a Python, e.g. "3.12"
function python_version() {
    "$1" -c 'import sys; print("%d.%d" % sys.version_info[:2])' 2>/dev/null
}

# python_problem <python>: why a Python cannot be used (too old, no venv or
# ensurepip module); empty if it is suitable
function python_problem() {
    local version
    if ! version=$(python_version "$1") || [ -z "${version}" ]; then
        echo "does not run"
    elif [ "$(printf '%s\n' "${PYTHON_MIN_VERSION}" "${version}" | sort -V | head -n 1)" != "${PYTHON_MIN_VERSION}" ]; then
        echo "version ${version} is too old, ${PYTHON_MIN_VERSION} or newer is required"
    elif ! "$1" -c "import venv, ensurepip" > /dev/null 2>&1; then
        echo "version ${version}, without the Python modules venv/ensurepip"
    fi
}

# tool_available <tool>: true if the program exists (for Python: in a
# suitable version, see python_problem)
function tool_available() {
    if ! command -v "$1" > /dev/null 2>&1; then
        return 1
    fi
    if [ "$1" = "${PYTHON}" ]; then
        [ -z "$(python_problem "$1")" ]
    fi
}

# tool_problem <tool>: why an existing tool is not used ("version 3.6 is too
# old, ..."); "not found" if it does not exist
function tool_problem() {
    if ! command -v "$1" > /dev/null 2>&1; then
        echo "not found"
    elif [ "$1" = "${PYTHON}" ]; then
        python_problem "$1"
    fi
}

# init_modules: make the 'module' command available; false if there is none
function init_modules() {
    local init
    if type module > /dev/null 2>&1; then return 0; fi

    for init in ${MODULESHOME:+"${MODULESHOME}/init/bash"} "${MODULE_INIT_SCRIPTS[@]}"; do
        if [ -f "${init}" ]; then
            source_quietly "${init}" > /dev/null 2>&1 || true
            if type module > /dev/null 2>&1; then return 0; fi
        fi
    done
    return 1
}

# check_tools: make sure all required tools exist. Missing tools are loaded
# with 'module load' (see TOOL_MODULES); fails with a list of all tools that
# are still missing.
function check_tools() {
    local tool module entry tool_tried
    local missing=()
    local have_modules=0

    for tool in $(required_tools | awk '!seen[$0]++'); do
        if tool_available "${tool}"; then continue; fi

        tool_tried=()
        if [ ${have_modules} = 0 ] && init_modules; then have_modules=1; fi
        if [ ${have_modules} = 1 ]; then
            for module in ${TOOL_MODULES[${tool}]:-${tool}}; do
                echo "Required tool '${tool}' $(tool_problem "${tool}"): trying 'module load ${module}'"
                module load "${module}" > /dev/null 2>&1 || true
                if tool_available "${tool}"; then
                    echo "Loaded module '${module}' for '${tool}'"
                    break
                fi
                tool_tried+=("${module}")
            done
        fi

        if ! tool_available "${tool}"; then
            entry=${tool}
            if command -v "${tool}" > /dev/null 2>&1; then
                entry="${tool} ($(command -v "${tool}"): $(tool_problem "${tool}"))"
            fi
            if [ ${#tool_tried[@]} -gt 0 ]; then
                entry="${entry}  [tried: module load ${tool_tried[*]}]"
            fi
            missing+=("${entry}")
        fi
    done

    if [ ${#missing[@]} -gt 0 ]; then
        {
            echo "The following required tools are missing:"
            printf '    %s\n' "${missing[@]}"
            if [ ${have_modules} = 0 ]; then
                echo "No 'module' command is available to load them."
            fi
            echo "Install them or load them (e.g. 'module load ...') before running $(basename "$0")."
        } >&2
        die "Missing required tools: $(printf '%s\n' "${missing[@]}" | sed 's/ *[[(].*//' | paste -sd ' ')"
    fi
}


###############################################################################
# AEC library (libaec)
#
# ecCodes requires libaec (CCSDS compression) and stops in its configuration
# if the library is not found, or if it is too old (ecCodes >= 2.49 requires
# libaec >= 1.1.4). The requirement depends on the ecCodes version, so the
# check runs the same find_package() call as the ecCodes sources in a small
# CMake project. If it fails, the modules in AEC_MODULES are loaded one after
# the other until the library is found.
###############################################################################

# aec_find_package: the find_package() call for libaec in the ecCodes sources,
# e.g. "libaec 1.1.4" or "AEC"; empty if there is none
function aec_find_package() {
    local cmakelists="$(src_dir eccodes)/CMakeLists.txt"
    if [ -f "${cmakelists}" ]; then
        sed -nE 's/^[[:space:]]*find_package[[:space:]]*\([[:space:]]*((lib)?aec\b[^)]*)\).*/\1/Ip' "${cmakelists}" \
            | head -n 1 | sed 's/[[:space:]]*$//'
    fi
}

# aec_probe <find_package arguments>: true if CMake finds libaec the same
# way the ecCodes build does (same compiler, ecCodes' Find modules)
function aec_probe() {
    local args=$1
    local name=${args%% *}
    local dir="$(build_dir aec-check)" cc cxx rc=0
    read -r cc cxx <<< "$(compilers)"

    rm -rf "${dir}"
    mkdir -p "${dir}"
    cat > "${dir}/CMakeLists.txt" <<END_OF_PROBE
cmake_minimum_required(VERSION 3.12)
project(aec_check C)
list(APPEND CMAKE_MODULE_PATH "$(src_dir eccodes)/cmake")
set(libaec_USE_STATIC_LIBS OFF)
find_package(${args})
if(NOT ${name}_FOUND)
  message(FATAL_ERROR "find_package(${args}) failed")
endif()
message(STATUS "AEC library found: \${${name}_DIR}\${AEC_LIBRARIES}")
END_OF_PROBE

    cmake -S "${dir}" -B "${dir}/build" -DCMAKE_C_COMPILER="${cc}" \
        > "${dir}/cmake.log" 2>&1 || rc=$?
    if [ ${rc} = 0 ]; then
        sed -n 's/^-- AEC library found: /    /p' "${dir}/cmake.log"
        rm -rf "${dir}"
    fi
    return ${rc}
}

# check_aec: make sure ecCodes will find libaec; tries 'module load' for the
# modules in AEC_MODULES. Fails with an error message if the library cannot
# be found. Needs the ecCodes sources (to know the requirement); without them
# the check is skipped.
function check_aec() {
    local args module tried=() have_modules=0

    args=$(aec_find_package)
    if [ -z "${args}" ]; then
        if [ -f "$(src_dir eccodes)/CMakeLists.txt" ]; then
            echo "ecCodes ($(ref_of eccodes)) does not look for libaec: AEC check skipped"
        fi
        return 0
    fi

    echo "Checking the AEC library required by ecCodes: find_package(${args})"
    if aec_probe "${args}"; then return 0; fi

    if init_modules; then have_modules=1; fi
    if [ ${have_modules} = 1 ]; then
        for module in "${AEC_MODULES[@]}"; do
            echo "AEC library not found: trying 'module load ${module}'"
            if ! module load "${module}" > /dev/null 2>&1; then
                tried+=("${module} (not available)")
                continue
            fi
            if aec_probe "${args}"; then
                echo "Loaded module '${module}' for the AEC library"
                return 0
            fi
            # Loaded, but not suitable (e.g. too old): do not keep it
            module unload "${module}" > /dev/null 2>&1 || true
            tried+=("${module} (not suitable)")
        done
    fi

    {
        echo "The AEC library (libaec) required by ecCodes ($(ref_of eccodes)) was not found:"
        echo "    find_package(${args}) failed"
        if [ ${have_modules} = 1 ]; then
            echo "    tried: module load ${tried[*]}"
        else
            echo "    No 'module' command is available to load it."
        fi
        echo "Load a suitable version (e.g. 'module load aec/<version>', see 'module avail aec')"
        echo "or install it and add its prefix to CMAKE_PREFIX_PATH, then re-run $(basename "$0")."
        echo "CMake output of the last check:"
        sed 's/^/    /' "$(build_dir aec-check)/cmake.log" | grep -v '^    --' || true
    } >&2
    rm -rf "$(build_dir aec-check)"
    die "AEC library not found: find_package(${args}) failed"
}

# check_aec_once: check_aec, unless it already succeeded in this run
function check_aec_once() {
    if [ ${AEC_CHECKED} = 0 ]; then
        check_aec
        AEC_CHECKED=1
    fi
}


###############################################################################
# Environment
###############################################################################

function setup_environment() {
    # Absolute path, because it is written into the load_env file
    mkdir -p "${ROOTDIR}"
    ROOTDIR=$(cd "${ROOTDIR}" && pwd)

    case "${GIT_PROTOCOL}" in
        https) GITHUB_BASE="https://github.com/ecmwf" ;;
        ssh)   GITHUB_BASE="git@github.com:ecmwf" ;;
    esac
}


###############################################################################
# Git
###############################################################################

function repo_url() { echo "${GITHUB_BASE}/$1.git"; }   # <package>

# remote_ref_of <kind> <ref>: full name of the ref on the remote
function remote_ref_of() {
    local kind=$1 ref=$2
    if [ "${kind}" = "tag" ]; then
        echo "refs/tags/${ref}"
    elif [[ "${ref}" =~ ^pr-([0-9]+)$ ]]; then
        echo "refs/pull/${BASH_REMATCH[1]}/head"
    else
        echo "refs/heads/${ref}"
    fi
}

# latest_tag <package>: the latest release tag on GitHub (see RELEASE_TAG_REGEX),
# empty if there is none
function latest_tag() {
    git ls-remote --tags --refs "$(repo_url "$1")" \
        | sed 's|.*refs/tags/||' \
        | { grep -E "${RELEASE_TAG_REGEX}" || true; } \
        | sort -V \
        | tail -n 1
}

# select_default_refs: packages without --branch/--tag use their latest tag
function select_default_refs() {
    local pkg tag
    for pkg in "${PACKAGES[@]}"; do
        if ! is_enabled "${pkg}" || [ -n "${PKG_REF[${pkg}]:-}" ]; then continue; fi

        if ! tag=$(latest_tag "${pkg}"); then
            die "Could not read the tags of ${pkg} ($(repo_url "${pkg}"))"
        fi
        if [ -z "${tag}" ]; then
            die "No release tag found in ${pkg} ($(repo_url "${pkg}")): use --branch or --tag"
        fi
        echo "No --branch/--tag given for ${pkg}: using the latest tag ${tag}"
        PKG_KIND[${pkg}]=tag
        PKG_REF[${pkg}]=${tag}
    done
}

# validate_refs: check all selected refs before installing anything
function validate_refs() {
    local pkg
    for pkg in "${PACKAGES[@]}"; do
        if ! is_enabled "${pkg}"; then continue; fi
        if ! git ls-remote --exit-code "$(repo_url "${pkg}")" \
                "$(remote_ref_of "${PKG_KIND[${pkg}]}" "${PKG_REF[${pkg}]}")" > /dev/null; then
            die "${PKG_KIND[${pkg}]} '${PKG_REF[${pkg}]}' not found in ${pkg} ($(repo_url "${pkg}"))"
        fi
    done
}

# checkout <package>: clone the package if needed, then check out its ref: a
# tag (detached), a pull request (pr-<number>) or a branch (fast-forwarded)
function checkout() {
    local pkg=$1
    local dir=$(src_dir "${pkg}")
    local kind=${PKG_KIND[${pkg}]} ref=${PKG_REF[${pkg}]}

    if [ ! -d "${dir}/.git" ]; then
        mkdir -p "$(dirname "${dir}")"
        git clone "$(repo_url "${pkg}")" "${dir}"
    fi

    git -C "${dir}" fetch --tags --force origin

    if [ "${kind}" = "tag" ]; then
        git -C "${dir}" checkout --detach "refs/tags/${ref}"
    elif [[ "${ref}" =~ ^pr-[0-9]+$ ]]; then
        git -C "${dir}" fetch origin "$(remote_ref_of "${kind}" "${ref}")"
        git -C "${dir}" checkout -B "${ref}" FETCH_HEAD
    elif git -C "${dir}" show-ref --verify --quiet "refs/heads/${ref}"; then
        git -C "${dir}" checkout "${ref}"
        git -C "${dir}" merge --ff-only "origin/${ref}"
    else
        git -C "${dir}" checkout -b "${ref}" --track "origin/${ref}"
    fi
}

# ref_of <package>: the selected ref, e.g. "tag 2.49.0"
function ref_of() {
    echo "${PKG_KIND[$1]} ${PKG_REF[$1]}"
}

# describe_package <package>: e.g. "tag 2.49.0 (2.49.0)" or
# "branch develop (2.48.0-12-gabc1234)"
function describe_package() {
    local commit
    commit=$(git -C "$(src_dir "$1")" describe --tags --always --dirty 2>/dev/null || echo "not checked out")
    echo "$(ref_of "$1") (${commit})"
}

# package_summary <line prefix>: one line per installed package
function package_summary() {
    local prefix=$1 pkg
    for pkg in "${PACKAGES[@]}"; do
        if is_enabled "${pkg}"; then
            printf '%s%-16s%s\n' "${prefix}" "${pkg}:" "$(describe_package "${pkg}")"
        fi
    done
}


###############################################################################
# Build helpers
###############################################################################

# eckit_setting: the eckit setting of the ecCodes build, e.g. "with eckit"
function eckit_setting() {
    if is_enabled eckit; then echo "with eckit"; else echo "without eckit"; fi
}

# build_config <package>: the configuration a package is built with. If it
# changes, the package is rebuilt from scratch (see prepare_build).
function build_config() {
    case "$1" in
        eckit)   echo "$(ref_of eckit), ${COMPILER}, ${CMAKE_BUILD_TYPE}" ;;
        eccodes)
            if is_enabled eckit; then
                echo "$(ref_of eccodes), ${COMPILER}, ${CMAKE_BUILD_TYPE}, with eckit ($(ref_of eckit))"
            else
                echo "$(ref_of eccodes), ${COMPILER}, ${CMAKE_BUILD_TYPE}, without eckit"
            fi
            ;;
    esac
}

# prepare_build <package>: clean the build and install directories if they
# were made with another configuration, then record the current one
function prepare_build() {
    local pkg=$1
    local build=$(build_dir "${pkg}") prefix=$(prefix_dir "${pkg}")
    local stamp="${build}/eccodes_install.config"
    local config=$(build_config "${pkg}") old

    if [ -e "${build}" ] || [ -e "${prefix}" ]; then
        old=$(cat "${stamp}" 2>/dev/null || echo "unknown")
        if [ "${old}" != "${config}" ]; then
            echo "Configuration of ${pkg} changed ('${old}' -> '${config}'): cleaning ${build} and ${prefix}"
            rm -rf "${build}" "${prefix}"
        fi
    fi
    mkdir -p "${build}" "${prefix}"
    echo "${config}" > "${stamp}"
}

# cmake_install <package> <compiler flags> [cmake options...]: configure,
# build and install a CMake project with the selected compiler and ecbuild
function cmake_install() {
    local pkg=$1 flags=$2
    local cc cxx
    shift 2
    read -r cc cxx <<< "$(compilers)"

    prepare_build "${pkg}"
    cmake \
        -S "$(src_dir "${pkg}")" \
        -B "$(build_dir "${pkg}")" \
        -DCMAKE_INSTALL_PREFIX="$(prefix_dir "${pkg}")" \
        -DCMAKE_BUILD_TYPE="${CMAKE_BUILD_TYPE}" \
        -DCMAKE_EXPORT_COMPILE_COMMANDS=1 \
        -DCMAKE_C_COMPILER="${cc}" \
        -DCMAKE_CXX_COMPILER="${cxx}" \
        -DCMAKE_C_FLAGS="${flags}" \
        -DCMAKE_CXX_FLAGS="${flags}" \
        -Decbuild_DIR="$(src_dir ecbuild)/cmake" \
        "$@"
    cmake --build "$(build_dir "${pkg}")" -j"${JOBS}"
    cmake --install "$(build_dir "${pkg}")"
}

# compiler_runtime_libdirs: colon separated directories of the runtime
# libraries (libstdc++, libgcc_s, libgfortran) of the selected compilers, if
# they are not in a system directory. libeccodes finds them via its RPATH, but
# that is not enough in Python: numpy (or another module) may load the older
# system libstdc++ first, and as a library of the same name is loaded only
# once, libeccodes then fails with "GLIBCXX_3.4.xx not found". These
# directories are therefore put into LD_LIBRARY_PATH (venv, load_env).
function compiler_runtime_libdirs() {
    local cc cxx compiler lib file dir
    local dirs=""
    read -r cc cxx <<< "$(compilers)"

    for compiler in "${cxx}" gfortran; do
        for lib in libstdc++ libgcc_s libgfortran; do
            file=$(cd / && "${compiler}" -print-file-name="${lib}.so" 2>/dev/null) || continue
            # Not found: the compiler prints the bare name
            if [[ "${file}" != /* ]]; then continue; fi
            dir=$(cd "$(dirname "${file}")" 2>/dev/null && pwd -P) || continue
            case "${dir}" in
                /lib|/lib64|/usr/lib|/usr/lib64) continue ;;
            esac
            # Only directories with the shared library itself (not just a
            # linker script pointing to the system library)
            if ! compgen -G "${dir}/${lib}.so.[0-9]*" > /dev/null; then continue; fi
            case ":${dirs}:" in
                *":${dir}:"*) ;;
                *) dirs="${dirs:+${dirs}:}${dir}" ;;
            esac
        done
    done
    echo "${dirs}"
}

# with_runtime_libs <command...>: run a command with the compiler runtime
# libraries (see compiler_runtime_libdirs) in LD_LIBRARY_PATH
function with_runtime_libs() {
    local rt
    rt=$(compiler_runtime_libdirs)
    if [ -n "${rt}" ]; then
        LD_LIBRARY_PATH="${rt}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}" "$@"
    else
        "$@"
    fi
}

# venv_ok: true if the Python venv exists, works and uses the version of the
# selected Python (a venv of another Python version, e.g. the old system
# Python, is treated as broken and recreated by step_eccodes_python)
function venv_ok() {
    [ -f "$(venv_dir)/bin/activate" ] \
        && [ "$(python_version "$(venv_dir)/bin/python")" = "$(python_version "${PYTHON}")" ]
}

# in_venv <command...>: run a command in the Python venv, with ECCODES_DIR
# pointing to the ecCodes installation
function in_venv() {
    local rc=0

    if ! venv_ok; then
        die "The Python venv $(venv_dir) is missing or broken"
    fi

    (
        source_quietly "$(venv_dir)/bin/activate" || exit 99
        export ECCODES_DIR="$(prefix_dir eccodes)"
        with_runtime_libs "$@"
    ) || rc=$?

    if [ ${rc} = 99 ]; then
        die "Could not activate the Python venv $(venv_dir)"
    elif [ ${rc} != 0 ]; then
        die "Command failed in the Python venv (exit code ${rc}): $*"
    fi
}


###############################################################################
# Installation steps
###############################################################################

function step_ecbuild() {
    checkout ecbuild
}

function step_eckit() {
    checkout eckit
    cmake_install eckit "-Wno-unused-but-set-variable"
}

function step_eccodes_source() {
    checkout eccodes
}

function step_eccodes_build() {
    local options=(-DENABLE_FORTRAN=ON -DENABLE_EXTRA_TESTS=1 -DENABLE_MEMFS=OFF)

    check_aec_once

    if is_enabled eckit; then
        options+=(-DENABLE_ECKIT_GEO=ON -Deckit_ROOT="$(prefix_dir eckit)")
    else
        options+=(-DENABLE_ECKIT_GEO=OFF)
    fi

    cmake_install eccodes "" "${options[@]}"
}

# eccodes-python and grib-check are installed from the git checkouts (not from
# PyPI) and without the binary library 'eccodeslib', so that they use the
# locally built libeccodes (found via ECCODES_DIR).

function step_eccodes_python_source() {
    checkout eccodes-python
}

function step_grib_check_source() {
    checkout grib-check
}

function step_eccodes_python() {
    local venv=$(venv_dir)

    # Create the venv; a broken one (e.g. after an interrupted run or a
    # changed Python) is recreated from scratch
    if [ ! -d "${venv}" ]; then
        "${PYTHON}" -m venv "${venv}"
    elif ! venv_ok; then
        if [ ! -f "${venv}/pyvenv.cfg" ] && [ -n "$(ls -A "${venv}")" ]; then
            die "${venv} exists but is not a Python venv: remove or rename it"
        fi
        echo "The Python venv ${venv} is broken or uses another Python version (not $(python_version "${PYTHON}")): recreating it"
        "${PYTHON}" -m venv --clear "${venv}"
    fi

    in_venv pip install --upgrade pip

    # With DEPEND_ON_ECCODESLIB=1, setup.py would add the 'eccodeslib' dependency
    in_venv env -u DEPEND_ON_ECCODESLIB \
        pip install --upgrade --force-reinstall --no-cache-dir "$(src_dir eccodes-python)"

    # Make sure no bundled binary library shadows the local build
    in_venv pip uninstall -y eccodeslib

    in_venv env ECCODES_PYTHON_TRACE_LIB_SEARCH=1 python -m eccodes selfcheck
}

# step_grib_check: needs the venv of step_eccodes_python
function step_grib_check() {
    # eccodes-python must be installed in the venv, otherwise pip would pull
    # 'eccodes' from PyPI as a dependency of grib-check. If the venv was
    # removed or broken after step_eccodes_python, install it again.
    if ! venv_ok || ! ECCODES_DIR="$(prefix_dir eccodes)" with_runtime_libs \
            "$(venv_dir)/bin/python" -c "import eccodes" > /dev/null 2>&1; then
        echo "eccodes-python is missing in the Python venv: installing it again"
        step_eccodes_python
    fi

    # First install the dependencies of grib-check (the installed eccodes
    # satisfies 'eccodes>=...' and is kept), then rebuild grib-check itself
    # without touching its dependencies
    in_venv pip install "$(src_dir grib-check)"
    in_venv pip install --force-reinstall --no-deps --no-cache-dir "$(src_dir grib-check)"

    # Make sure no bundled binary library shadows the local build
    in_venv pip uninstall -y eccodeslib

    in_venv python -c "import grib_check"
    in_venv grib-check --help > /dev/null
}

# step_env_files: write and test load_env and unload_env
function step_env_files() {
    write_load_env > "$(load_env_file)"
    write_unload_env > "$(unload_env_file)"

    # Test the environment: load it, use it, try to load it a second time
    # (must be refused), unload it and compare with the original environment
    (
        env_vars() { echo "${PATH}|${LD_LIBRARY_PATH:-}|${PKG_CONFIG_PATH:-}|${CMAKE_PREFIX_PATH:-}|${ECCODES_DIR:-}|${VIRTUAL_ENV:-}"; }
        original=$(env_vars)

        source_quietly "$(load_env_file)"
        codes_info
        python -c "import eccodes, grib_check; print('eccodes-python', eccodes.__version__, '-> ecCodes', eccodes.codes_get_api_version())"
        grib-check --help > /dev/null

        if source_quietly "$(load_env_file)"; then
            die "load_env did not refuse to load the environment twice"
        fi

        source_quietly "$(unload_env_file)"
        if [ "$(env_vars)" != "${original}" ]; then
            die "unload_env did not restore the environment"
        fi
        if [ -n "${ECCODES_INSTALL_ROOT:-}" ]; then
            die "unload_env did not unset ECCODES_INSTALL_ROOT"
        fi
    )
}


###############################################################################
# Environment files
#
# load_env sets ECCODES_INSTALL_ROOT and remembers everything it changes in
# ECCODES_INSTALL_* variables. It refuses to load while ECCODES_INSTALL_ROOT
# is set. unload_env undoes exactly these changes: it removes only the entries
# load_env added to PATH & co., so later changes of the user are kept.
###############################################################################

# write_load_env: print the load_env file
function write_load_env() {
    local prefix=$(prefix_dir eccodes)
    local libdirs=$(libdir_of "${prefix}") rt=$(compiler_runtime_libdirs)

    if is_enabled eckit; then
        libdirs="${libdirs}:$(libdir_of "$(prefix_dir eckit)")"
    fi
    # Runtime libraries of the compiler (see compiler_runtime_libdirs)
    if [ -n "${rt}" ]; then
        libdirs="${libdirs}:${rt}"
    fi

    echo "# Generated by $(basename "$0")"
    echo "# Usage: source $(load_env_file)"
    echo "# Undo:  source $(unload_env_file)"
    echo "#"
    echo "# ecCodes: $(build_config eccodes)"
    package_summary "#   "
    echo
    echo "# Settings of this installation"
    echo "_ecc_root=$(printf '%q' "${ROOTDIR}")"
    echo "_ecc_desc=$(printf '%q' "eccodes $(ref_of eccodes), ${COMPILER}, $(eckit_setting)")"
    echo "_ecc_prefix=$(printf '%q' "${prefix}")"
    echo "_ecc_libdirs=$(printf '%q' "${libdirs}")"
    echo "_ecc_pkgconfig=$(printf '%q' "$(libdir_of "${prefix}")/pkgconfig")"
    echo "_ecc_venv=$(printf '%q' "$(venv_dir)")"
    echo "# Modules that were loaded during the installation (e.g. the compiler)"
    echo "_ecc_modules=$(printf '%q' "${LOADEDMODULES//:/ }")"
    echo "_ecc_module_inits=$(printf '%q' "${MODULE_INIT_SCRIPTS[*]}")"
    cat <<'END_OF_LOAD_ENV'

if ! (return 0 2>/dev/null); then
    echo "This file must be sourced: source ${BASH_SOURCE[0]}" >&2
    exit 1
fi

_ecc_load() {
    local init m before missing

    if [ -n "${ECCODES_INSTALL_ROOT:-}" ]; then
        echo "The ecCodes environment of ${ECCODES_INSTALL_ROOT} is already loaded." >&2
        echo "Unload it first with: source ${ECCODES_INSTALL_ROOT}/unload_env" >&2
        return 1
    fi

    # Modules; only the modules loaded here are unloaded by unload_env
    export ECCODES_INSTALL_MODULES=""
    if [ -n "${_ecc_modules}" ]; then
        if ! type module > /dev/null 2>&1; then
            for init in ${MODULESHOME:+"${MODULESHOME}/init/bash"} ${_ecc_module_inits}; do
                if [ -f "${init}" ]; then source "${init}"; break; fi
            done
        fi
        before=":${LOADEDMODULES:-}:"
        # Load only the modules that are not loaded yet: loading an already
        # loaded module again makes Lmod reload it, which reorders PATH & co.
        missing=""
        for m in ${_ecc_modules}; do
            case "${before}" in
                *":${m}:"*) ;;
                *) missing="${missing:+${missing} }${m}" ;;
            esac
        done
        if [ -n "${missing}" ] && ! module load ${missing}; then
            echo "Warning: could not load the modules: ${missing}" >&2
        fi
        for m in ${LOADEDMODULES//:/ }; do
            case "${before}" in
                *":${m}:"*) ;;
                *) ECCODES_INSTALL_MODULES="${ECCODES_INSTALL_MODULES:+${ECCODES_INSTALL_MODULES} }${m}" ;;
            esac
        done
    fi

    # Remember the changes for unload_env
    export ECCODES_INSTALL_ROOT="${_ecc_root}"
    export ECCODES_INSTALL_DESC="${_ecc_desc}"
    export ECCODES_INSTALL_VENV="${_ecc_venv}"
    export ECCODES_INSTALL_PATHS="PATH=${_ecc_prefix}/bin|LD_LIBRARY_PATH=${_ecc_libdirs}|PKG_CONFIG_PATH=${_ecc_pkgconfig}|CMAKE_PREFIX_PATH=${_ecc_prefix}"
    if [ -n "${ECCODES_DIR+x}" ]; then
        export ECCODES_INSTALL_OLD_ECCODES_DIR="${ECCODES_DIR}"
    fi

    export ECCODES_DIR="${_ecc_prefix}"
    export PATH="${_ecc_prefix}/bin${PATH:+:${PATH}}"
    export LD_LIBRARY_PATH="${_ecc_libdirs}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"
    export PKG_CONFIG_PATH="${_ecc_pkgconfig}${PKG_CONFIG_PATH:+:${PKG_CONFIG_PATH}}"
    export CMAKE_PREFIX_PATH="${_ecc_prefix}${CMAKE_PREFIX_PATH:+:${CMAKE_PREFIX_PATH}}"

    # Python venv with eccodes-python and grib-check
    source "${_ecc_venv}/bin/activate"

    echo "Loaded ecCodes environment: ${_ecc_desc} (unload with: source ${_ecc_root}/unload_env)"
}

_ecc_load
_ecc_rc=$?
unset -f _ecc_load
unset _ecc_root _ecc_desc _ecc_prefix _ecc_libdirs _ecc_pkgconfig _ecc_venv _ecc_modules _ecc_module_inits
if [ ${_ecc_rc} = 0 ]; then unset _ecc_rc; return 0; else unset _ecc_rc; return 1; fi
END_OF_LOAD_ENV
}

# write_unload_env: print the unload_env file
function write_unload_env() {
    echo "# Generated by $(basename "$0")"
    echo "# Unloads the ecCodes environment loaded with load_env"
    echo "# Usage: source $(unload_env_file)"
    cat <<'END_OF_UNLOAD_ENV'

if ! (return 0 2>/dev/null); then
    echo "This file must be sourced: source ${BASH_SOURCE[0]}" >&2
    exit 1
fi

# _ecc_remove_path <variable> <dir>: remove <dir> from a colon separated list
_ecc_remove_path() {
    local var=$1 dir=$2
    local value=":${!var:-}:"
    while [[ "${value}" == *":${dir}:"* ]]; do
        value=${value//":${dir}:"/:}
    done
    value=${value#:}
    value=${value%:}
    if [ -n "${value}" ]; then export "${var}=${value}"; else unset "${var}"; fi
}

_ecc_unload() {
    local desc entry var dir path
    local -a entries dirs

    if [ -z "${ECCODES_INSTALL_ROOT:-}" ]; then
        echo "No ecCodes environment is loaded." >&2
        return 1
    fi
    desc=${ECCODES_INSTALL_DESC}

    # Python venv. 'deactivate' would reset PATH to its value before loading
    # (losing later changes of the user), so PATH is kept and only the venv
    # entry is removed below. 'deactivate' is not defined in subshells.
    if [ -n "${VIRTUAL_ENV:-}" ] && type deactivate > /dev/null 2>&1; then
        path=${PATH}
        deactivate
        export PATH=${path}
    fi
    if [ -n "${VIRTUAL_ENV:-}" ] && [ "${VIRTUAL_ENV}" -ef "${ECCODES_INSTALL_VENV}" ]; then
        unset VIRTUAL_ENV VIRTUAL_ENV_PROMPT
    fi

    # Entries added to PATH & co.
    IFS='|' read -ra entries <<< "${ECCODES_INSTALL_PATHS}|PATH=${ECCODES_INSTALL_VENV}/bin"
    for entry in "${entries[@]}"; do
        var=${entry%%=*}
        IFS=':' read -ra dirs <<< "${entry#*=}"
        for dir in "${dirs[@]}"; do
            _ecc_remove_path "${var}" "${dir}"
        done
    done

    if [ -n "${ECCODES_INSTALL_OLD_ECCODES_DIR+x}" ]; then
        export ECCODES_DIR="${ECCODES_INSTALL_OLD_ECCODES_DIR}"
    else
        unset ECCODES_DIR
    fi

    # Modules loaded by load_env
    if [ -n "${ECCODES_INSTALL_MODULES:-}" ]; then
        if type module > /dev/null 2>&1; then
            module unload ${ECCODES_INSTALL_MODULES}
        else
            echo "Warning: no 'module' command to unload: ${ECCODES_INSTALL_MODULES}" >&2
        fi
    fi

    unset ECCODES_INSTALL_ROOT ECCODES_INSTALL_DESC ECCODES_INSTALL_VENV \
          ECCODES_INSTALL_PATHS ECCODES_INSTALL_OLD_ECCODES_DIR ECCODES_INSTALL_MODULES
    hash -r
    echo "Unloaded ecCodes environment: ${desc}"
}

_ecc_unload
_ecc_rc=$?
unset -f _ecc_unload _ecc_remove_path
if [ ${_ecc_rc} = 0 ]; then unset _ecc_rc; return 0; else unset _ecc_rc; return 1; fi
END_OF_UNLOAD_ENV
}


###############################################################################
# Step list
###############################################################################

# add_step <name> <command>
function add_step() {
    STEP_NAMES+=("$1")
    STEP_CMDS+=("$2")
}

# step_index <command>: number of the step (1-based) that runs <command>
function step_index() {
    local i
    for ((i = 0; i < ${#STEP_CMDS[@]}; i++)); do
        if [ "${STEP_CMDS[i]}" = "$1" ]; then echo $((i + 1)); return 0; fi
    done
    die "Unknown step: $1"
}

# define_steps: the installation steps in the order they are run
function define_steps() {
    add_step "ecbuild ($(ref_of ecbuild))" step_ecbuild
    if is_enabled eckit; then
        add_step "eckit ($(ref_of eckit), ${COMPILER})" step_eckit
    fi
    add_step "eccodes source ($(ref_of eccodes))"                   step_eccodes_source
    add_step "eccodes build (${COMPILER}, $(eckit_setting))"        step_eccodes_build
    add_step "eccodes-python source ($(ref_of eccodes-python))"     step_eccodes_python_source
    add_step "eccodes-python"                                       step_eccodes_python
    add_step "grib-check source ($(ref_of grib-check))"             step_grib_check_source
    add_step "grib-check"                                           step_grib_check
    add_step "load_env and unload_env"                              step_env_files
}


###############################################################################
# Progress (restart point)
#
# The state file stores a hash of the configuration (step names, git
# protocol, Python) and the number of completed steps. A re-run with the same
# configuration skips the completed steps. The file is removed once the
# installation is complete.
###############################################################################

function config_hash() {
    printf '%s\n' "${STEP_NAMES[@]}" "${GIT_PROTOCOL}" "${PYTHON}" | md5sum | cut -d' ' -f1
}

function save_progress() {
    local file=$(state_file) i
    {
        echo "config=$(config_hash)"
        echo "completed=${COMPLETED}"
        echo "# command: $0 ${ORIG_ARGS}"
        for ((i = 0; i < COMPLETED; i++)); do
            echo "# done $((i + 1))/${#STEP_NAMES[@]}: ${STEP_NAMES[i]}"
        done
    } > "${file}.tmp"
    mv "${file}.tmp" "${file}"
}

function load_progress() {
    local file=$(state_file) saved_hash saved_completed

    if [ "${RESTART}" = 1 ]; then
        rm -f "${file}"
        banner "--restart given: installing everything from the beginning"
        return
    fi
    if [ ! -f "${file}" ]; then
        return
    fi

    saved_hash=$(sed -n 's/^config=//p' "${file}")
    saved_completed=$(sed -n 's/^completed=//p' "${file}")

    if [ "${saved_hash}" != "$(config_hash)" ]; then
        banner "Saved progress in ${file} belongs to a different configuration: installing everything from the beginning"
    elif [[ "${saved_completed}" =~ ^[0-9]+$ ]] && [ "${saved_completed}" -le ${#STEP_NAMES[@]} ]; then
        COMPLETED=${saved_completed}
        banner "Resuming installation: ${COMPLETED}/${#STEP_NAMES[@]} steps already done (${file})"
    else
        banner "Invalid state file ${file}: installing everything from the beginning"
    fi
}

# on_exit: on failure, report the failed step and how to resume
function on_exit() {
    local rc=$?
    { set +x; } 2>/dev/null

    if [ ${rc} -ne 0 ]; then
        echo
        echo "########## FAILED ##########"
        if [ -n "${CURRENT_STEP}" ]; then
            echo "Installation of ${CURRENT_STEP} failed (exit code ${rc})."
        else
            echo "Installation failed (exit code ${rc})."
        fi
        if [ -n "${FAILED_MSG}" ]; then
            echo "Error: ${FAILED_MSG}"
        elif [ -n "${FAILED_CMD}" ]; then
            echo "Failed command (line ${FAILED_LINE}): ${FAILED_CMD}"
        fi
        if [ -f "$(state_file)" ]; then
            echo "Progress: ${COMPLETED}/${#STEP_NAMES[@]} steps done, saved in $(state_file)"
        else
            echo "Progress: ${COMPLETED}/${#STEP_NAMES[@]} steps done"
        fi
        echo "Fix the problem and re-run the same command to resume:"
        echo "    $0 ${ORIG_ARGS}"
        echo "############################"
    fi
    exit ${rc}
}

# run_steps: run all steps that are not completed yet. The commands of a step
# are traced (set -x).
function run_steps() {
    local nsteps=${#STEP_NAMES[@]} i n

    for ((i = 0; i < nsteps; i++)); do
        n=$((i + 1))
        if [ ${n} -le ${COMPLETED} ]; then
            banner "[${n}/${nsteps}] SKIPPED (already installed): ${STEP_NAMES[i]}"
            continue
        fi

        CURRENT_STEP="[${n}/${nsteps}] ${STEP_NAMES[i]}"
        banner "[${n}/${nsteps}] STARTED: ${STEP_NAMES[i]}"

        set -x
        ${STEP_CMDS[i]}
        { set +x; } 2>/dev/null

        COMPLETED=${n}
        save_progress
        banner "[${n}/${nsteps}] SUCCESS: ${STEP_NAMES[i]} successfully installed"
        CURRENT_STEP=""
    done

    # Complete: the next run starts from the beginning again
    rm -f "$(state_file)"
}


###############################################################################
# Summary
###############################################################################

function print_summary() {
    echo
    echo "============================================================"
    echo " ecCodes installation finished (${#STEP_NAMES[@]}/${#STEP_NAMES[@]} steps)"
    echo "============================================================"
    echo
    echo "Packages:"
    package_summary "    "
    echo
    echo "ecCodes: $(build_config eccodes)"
    echo "    install: $(prefix_dir eccodes)"
    echo "    venv:    $(venv_dir)"
    echo
    echo "Load the environment (ecCodes tools, eccodes-python, grib-check):"
    echo
    echo "    source $(load_env_file)"
    echo
    echo "Unload it again:"
    echo
    echo "    source $(unload_env_file)"
    echo
    echo "After loading, the following is available:"
    echo "    ecCodes tools:  codes_info, grib_ls, grib_dump, bufr_dump, ..."
    echo "    Python:         python -c 'import eccodes, grib_check'"
    echo "    grib-check:     grib-check --help"
    echo "    Scripts:        use '#!/usr/bin/env python3' as shebang"
}


###############################################################################
# Main
###############################################################################

function main() {
    parse_args "$@"
    check_not_loaded
    check_tools
    setup_environment
    select_default_refs
    define_steps
    load_progress

    trap 'FAILED_CMD=${BASH_COMMAND}; FAILED_LINE=${LINENO}' ERR
    trap on_exit EXIT

    validate_refs
    # When resuming with the ecCodes sources already checked out, check the
    # AEC library right away: this fails early and (re)loads its module for
    # the remaining steps. Otherwise it is checked before building ecCodes.
    if [ ${COMPLETED} -ge $(step_index step_eccodes_source) ]; then
        check_aec_once
    fi
    run_steps
    print_summary
}

main "$@"
