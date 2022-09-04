#!/bin/bash
ps aux | grep -E 'flask_apiapp/app.py' --color=always
echo
ps aux | grep -E 'flask_apiapp/app.py' | while read l; do
    processid=`echo $l | cut -d' ' -f2`
    echo -e "\nKilling $processid ..."
    kill -9 $processid
done
