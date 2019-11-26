# GerenciaRedes

TRABALHO 2: DOCKER + OWAMP

  Primeiro é necessário clonar o diretório
  `git clone https://github.com/luismiguelsb/GerenciaRedes/edit/master/` -> Na VM que será o Manager 
  
  
* Como inicializar os containers:

  Em seguida precisa inserir as VMs no Swarm:
  `docker swarm init` -> na VM Manager do Swarm
  
  `docker swarm join <token>` -> na VM que será o Worker do Swarm (onde token é informado pelo Manager e preenchido manualmente pelo Worker)
  
  Para confirmar que as duas VMs estão no Swarm:
  `docker node ls`
  
  Agora já pode executar o script (localizado em gerenciaRedes/T2) para inicializar os containers:
  `bash initDocker.sh`
  
  No fim do script vai acessar o terminal do container client OWAMP, os logs estão em /gerenciaRedes/logs
  

* Referências:

  https://github.com/sonata-nfv/tng-probes/wiki/owamp?fbclid=IwAR3WqMJmsTIdlyDg4q5DevLunQe6fOfG4bsAqVhhMX5J2Nq6hhitR-7wKs8

  https://software.internet2.edu/owamp/
  

