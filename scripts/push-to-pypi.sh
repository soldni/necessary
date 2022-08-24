#!/usr/bin/env bash

# get script directory
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  SCRIPT_DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  # if $SOURCE was a relative symlink, we need to resolve it
  # relative to the path where the symlink file was located
  [[ $SOURCE != /* ]] && SOURCE="$SCRIPT_DIR/$SOURCE"
done
SCRIPT_DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"

# this is the directory i'm in rn
CURRENT_DIR=$(pwd)

# fail if any command fails
set -ex

# upgrade twine as needed
python3 -m pip install --upgrade build twine

# moves up to root dir
cd "${SCRIPT_DIR}/.."

# build and upload to PyPi
python3 -m build
python3 -m twine upload dist/*

# no need to keep all previous builds
rm -rf dist/* build/*

# go back to original dir
cd ${CURRENT_DIR}
