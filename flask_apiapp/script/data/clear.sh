#!/bin/bash
SH=$(cd `dirname ${BASH_SOURCE:-$0}` && pwd)
AH=$(cd "$SH/../.." && pwd)

cd $AH
    PYTHONPATH=$AH \
    python3 -m pipenv run \
        python3 "$SH/clear.py"
