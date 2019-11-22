#!/bin/bash

# executar este script a partir de GerenciaRedes/T2

cd Compose

# inicializar os containers em modo Swarm (esse script não insere os hosts no Swarm, isso deve ser feito anteriormente)
echo "init containers..."
docker stack deploy -c docker-compose.yml stackGerencia

# aguarda que os containers inicializem (acho que 2min é o suficiente)
sleep 120

# salva o IP do servidor OWAMP em um arquivo
echo "save IP from OWAMP server to file..."
docker inspect $(docker node ps $(docker node ls | grep -v "Leader" | grep -v "STATUS" | head -n1 | cut -d " " -f1) | grep "owamp-server" | head -n1 | cut -d " " -f1) | grep -A1 "Addresses" | grep -v "Addresses" | tr -d '" ' | cut -f1 -d "/" > owampServerIP.txt

# transfere o arquivo para o cliente OWAMP
echo "copy file to OWAMP client..."
docker cp owampServerIP.txt $(docker ps | grep "owamp" | head -n1 | cut -d " " -f1):/gerenciaRedes/owampServerIP.txt

# abre a interface do container cliente
docker exec -it $(docker ps | grep "owamp" | head -n1 | cut -d " " -f1) bash

