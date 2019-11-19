# GerenciaRedes

TRABALHO 2: DOCKER + OWAMP

* Referências:

  https://github.com/sonata-nfv/tng-probes/wiki/owamp?fbclid=IwAR3WqMJmsTIdlyDg4q5DevLunQe6fOfG4bsAqVhhMX5J2Nq6hhitR-7wKs8

  https://software.internet2.edu/owamp/

  

* Configurar OWAMP em um Host Linux (normalmente):

  `sudo wget -P /etc/apt/sources.list.d/ http://downloads.perfsonar.net/debian/perfsonar-jessie-release.list`

  `sudo wget -qO - http://downloads.perfsonar.net/debian/perfsonar-debian-official.gpg.key | sudo apt-key add -`

  `sudo apt update`

  `sudo apt install perfsonar-tools`

  `owampd` -> inicializa o servidor

  `owping <IP_servidor>` -> executa o one-way ping (default: sessão de 10 segundos nas duas direções)


* Configurar OWAMP no Ubuntu-Docker:

  `apt update`
  
  `apt-get install -y wget`

  `apt-get install -y gnupg`

  `wget -P /etc/apt/sources.list.d/ http://downloads.perfsonar.net/debian/perfsonar-jessie-release.list`

  `wget -qO - http://downloads.perfsonar.net/debian/perfsonar-debian-official.gpg.key | apt-key add -`

  `apt update`  ->  denovo...

  `apt install -y perfsonar-tools`  ->  aqui tem que colocar uns números, tem que ver como fazer isso no Dockerfile

  `owampd -f` -> inicializa o servidor

  `owping <IP_servidor>` -> executa o one-way ping (não sei como fazer funcionar...)

  

