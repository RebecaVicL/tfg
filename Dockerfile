#Estamos usando de base la 3.8.10 descargada de docker-hub. esta generando el entorno virtual
#Primero copia el requirements.txt porque en esta imagen necesitamos instalar las librerias a usar
#Despues ejecuta el tutorial.py 

FROM python:3.8.10-slim-buster

COPY ./requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

CMD python3 tutorial.py
