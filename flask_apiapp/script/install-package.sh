#!/bin/bash
#TODO rename this file to install_package.sh

# install pipenv fr latest pip
python3 -m pip install --upgrade pip
python3 -m pip install pipenv


# install app's package
SH=$(cd `dirname $BASH_SOURCE` && pwd)
AH=$(cd "$SH/.." && pwd)
cd $AH
    python3 -m pipenv sync
        echo ; python3 -m pipenv --venv
               python3 -m pipenv run   python3 -V
