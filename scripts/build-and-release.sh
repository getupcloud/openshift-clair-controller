#!/bin/bash

ROOT_DIR=$(cd $(dirname $0)/.. && echo $PWD)
ENV_DIR="$ROOT_DIR/.env"

cd $ROOT_DIR

if ! [ -d "$ENV_DIR" ]; then
   virtualenv .env
fi

source .env/bin/activate
set -exu

PACKAGE_NAME=`python $ROOT_DIR/scripts/constants.py PACKAGE_NAME`
PACKAGE_VERSION=`python $ROOT_DIR/scripts/constants.py PACKAGE_VERSION`

cat > $ROOT_DIR/$PACKAGE_NAME/version.py <<EOF
CLAIR_CONTROLLER_VERSION = '${PACKAGE_VERSION}'
EOF

rm -rf build/ dist/
python setup.py bdist_wheel --universal
twine upload dist/${PACKAGE_NAME}-${PACKAGE_VERSION}-py2.py3-none-any.whl
