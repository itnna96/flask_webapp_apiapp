#!/bin/bash
SH=$(cd `dirname ${BASH_SOURCE:-$0}` && pwd)
source "$SH/clear.sh"

# add() twice on purpose
source "$SH/add.sh"
source "$SH/add.sh"
