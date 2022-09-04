#!/bin/bash
SH=$(cd `dirname $BASH_SOURCE` && pwd)
source "$SH/clear.sh"

# add() twice on purpose
source "$SH/add.sh"
source "$SH/add.sh"
