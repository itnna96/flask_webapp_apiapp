#!/bin/bash
SH=$(cd `dirname $BASH_SOURCE` && pwd)

c='mysql__toda20_cau3_c' ; p=20829 ; v='mysql__toda20_cau3_v' ; n='mysql__toda20_cau3_n'

echo;echo;
docker network create $n

# mysql c
echo;echo;
docker rm -f $c ; docker run -d  --name $c -h$c \
    -p "$p:3306" \
    \
    -e MYSQL_ROOT_PASSWORD=root \
    -e MYSQL_DATABASE=db \
    \
    -v "$v:/var/lib/mysql" \
    -v "$SH/db_seed.sql":/docker-entrypoint-initdb.d/'db_seed.sql'  `# run dbseed script  ref. https://hub.docker.com/_/mysql  > Initializing a fresh instance` \
    \
    --network $n \
    mysql ; [ $? != 0 ] && exit

    #region checkport
    echo ; echo '--- checkport'
        echo ; nmap -p$p localhost    | grep -E "$p.+open" --color=always ; checkport_nmap=$?
        echo ; nc -z     localhost $p ; checkport_nc=$?

        echo "checkport_nmap=$checkport_nmap"
        echo "checkport_nc=$checkport_nc"
        echo '--- checkport END'
    #endregion checkport


# GUI db client @ adminer
echo;echo;
docker rm -f "adminer_$c"; docker run -d    \
    -p8080:8080  \
    --network $n \
    --name "adminer_$c" \
    adminer


echo;echo;
docker ps | grep -E "$c|adminer_$c"
