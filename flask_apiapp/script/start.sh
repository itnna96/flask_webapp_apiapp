#!/bin/bash
SH=$(cd `dirname $BASH_SOURCE` && pwd)

AH=$(cd "$SH/.." && pwd) ; [[ -z $BASH_SOURCE ]] && AH='/app'
#                        ;       $BASH_SOURCE not avail. in sh shell of python:3.8 container, only avail. in bash shell, so we hardcode it as /app here

cd $AH
    PYTHONPATH=$AH \
    python3 -m pipenv run \
        python3 "$AH/app.py"
