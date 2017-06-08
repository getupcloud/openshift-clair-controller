#!/bin/bash

set -x
IMAGENAME=${1:-getupcloud/claircontroller}
TAG=${2:-devel}

docker build --no-cache . -t ${IMAGENAME}:${TAG}
#docker push ${IMAGENAME}:${TAG}
