#!/bin/bash
SH=$(cd `dirname $BASH_SOURCE` && pwd)
AH=$(cd "$SH/../.." && pwd)

cd $AH
    PYTHONPATH=$AH \
    python3 -m pipenv run \
        python3 "$SH/add.py"
