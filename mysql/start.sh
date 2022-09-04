#!/bin/bash
SH=$(cd `dirname $BASH_SOURCE` && pwd)

c=cau3_mysql_c ; p=20829 v="$SH/v"
docker rm -f $c ; docker run -d  --name $c -h$c \
    -p "$p:3306" \
    \
    -e MYSQL_ROOT_PASSWORD=root \
    -e MYSQL_DATABASE=db \
    \
    -v "$v:/var/lib/mysql" \
    mysql ; [ $? != 0 ] && exit

    echo ; echo '--- checkport'
        set -x  # exec print ON
            echo ; nmap -p$p localhost    | grep -E "$p.+open" --color=always ; checkport_nmap=$?
            echo ; nc -z     localhost $p ; checkport_nc=$?
        set +x  # exec print OFF

        echo
        echo "checkport_nmap=$checkport_nmap"
        echo "checkport_nc=$checkport_nc"
        echo '--- checkport END'
