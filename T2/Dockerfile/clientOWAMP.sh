#!/bin/bash

cd /gerenciaRedes
mkdir logs

while true;
do
    if [ -f /gerenciaRedes/owampServerIP.txt ]; then
        owping $(cat /gerenciaRedes/owampServerIP.txt) > /gerenciaRedes/logs/"$(date +"%FT%T").log";
    fi
    sleep 10;
done
