FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update \
    && apt-get install -y wget \
    && apt-get install -y gnupg \
    && wget -P /etc/apt/sources.list.d/ http://downloads.perfsonar.net/debian/perfsonar-jessie-release.list \
    && wget -qO - http://downloads.perfsonar.net/debian/perfsonar-debian-official.gpg.key | apt-key add - \
    && apt-get update \
    && apt install -y perfsonar-tools

RUN mkdir /gerenciaRedes

COPY clientOWAMP.sh /gerenciaRedes/clientOWAMP.sh

COPY serverOWAMP.sh /gerenciaRedes/serverOWAMP.sh


