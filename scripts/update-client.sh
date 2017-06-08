#!/bin/bash

set -ex

SED=sed
if which gsed > /dev/null 2>&1; then
  SED=gsed
fi

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
CLIENT_ROOT="${SCRIPT_ROOT}/../claircontroller"
CLIENT_VERSION=$(python "${SCRIPT_ROOT}/constants.py" CLIENT_VERSION)
PACKAGE_NAME=$(python "${SCRIPT_ROOT}/constants.py" PACKAGE_NAME)

pushd "${SCRIPT_ROOT}" > /dev/null
SCRIPT_ROOT="${PWD}"
popd > /dev/null

pushd "${CLIENT_ROOT}" > /dev/null
CLIENT_ROOT="${PWD}"
popd > /dev/null

rm -rf "${CLIENT_ROOT}/client"
mkdir -p "${CLIENT_ROOT}/client"

mvn -f "${SCRIPT_ROOT}/pom.xml" clean generate-sources \
    -Dgenerator.spec.path="${SCRIPT_ROOT}/swagger.json" \
    -Dgenerator.output.path="${CLIENT_ROOT}" \
    -Dgenerator.package.name=client \
    -Dgenerator.client.version=${CLIENT_VERSION}
