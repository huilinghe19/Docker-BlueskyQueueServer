#!/bin/bash

. /opt/conda/etc/profile.d/conda.sh
conda activate daiquiri

set -e

TMP_PATH=$(pwd)

cd /daiquiri-bluesky
echo "installing daiquri_bluesky"
pip install -e .
cd $TMP_PATH

supervisord
