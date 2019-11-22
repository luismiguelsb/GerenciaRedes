# GerenciaRedes

TRABALHO 2: DOCKER + OWAMP

  
* Como inicializar os containers:

  Primeiro precisa inserir as VMs no Swarm:
  `docker swarm init` -> na VM que será o Gerente do Swarm (a que você clonou o Git)
  
  `docker swarm join --token...blablabla` -> na VM que será o Worker do Swarm (copiar e colar o comando de saída do init)
  
  Para confirmar que as duas VMs estão no Swarm:
  `docker node ls`
  
  Agora já pode executar o script (no diretório T2) para inicializar os containers:
  `bash initDocker.sh`
  
  No fim do script vai acessar o terminal do container client OWAMP, os logs estão em /gerenciaRedes/logs
  
  

* Configurar OWAMP em um Host Linux (normalmente):

  `sudo wget -P /etc/apt/sources.list.d/ http://downloads.perfsonar.net/debian/perfsonar-jessie-release.list`

  `sudo wget -qO - http://downloads.perfsonar.net/debian/perfsonar-debian-official.gpg.key | sudo apt-key add -`

  `sudo apt update`

  `sudo apt install perfsonar-tools`

  `owampd` -> inicializa o servidor

  `owping <IP_servidor>` -> executa o one-way ping (default: sessão de 10 segundos nas duas direções)


* Referências:

  https://github.com/sonata-nfv/tng-probes/wiki/owamp?fbclid=IwAR3WqMJmsTIdlyDg4q5DevLunQe6fOfG4bsAqVhhMX5J2Nq6hhitR-7wKs8

  https://software.internet2.edu/owamp/
  

