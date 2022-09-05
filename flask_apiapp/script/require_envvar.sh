#!/bin/bash
SH=$(cd `dirname $BASH_SOURCE` && pwd)
AH=$(cd "$SH/.." && pwd)

[ -f "$AH/.env" ] && source "$AH/.env"  # load .env if exist

[ -z $DB_USER ] && (echo 'Envvar is required DB_USER'; kill $$)
[ -z $DB_PASS ] && (echo 'Envvar is required DB_PASS'; kill $$)
[ -z $DB_HOST ] && (echo 'Envvar is required DB_HOST'; kill $$)
[ -z $DB_NAME ] && (echo 'Envvar is required DB_NAME'; kill $$)

exit 0
