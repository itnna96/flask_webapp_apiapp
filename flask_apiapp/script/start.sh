#!/bin/bash
SH=$(cd `dirname $BASH_SOURCE` && pwd)
AH=$(cd "$SH/.." && pwd)

cd $AH
    PYTHONPATH=$AH \
    \
    DB_USER=root \
    DB_PASS=root \
    DB_HOST=127.0.0.1:20829  _=`#CAUTION localhost NOT working > DB_HOST=localhost:20829` \
    DB_NAME=db \
    \
    python3 -m pipenv run \
        python3 "$AH/app.py"
