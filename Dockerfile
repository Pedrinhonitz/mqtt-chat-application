FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y mosquitto mosquitto-clients python3 python3-pip

RUN pip3 install paho-mqtt

COPY chat_client.py /app/chat_client.py
COPY chat_server.py /app/chat_server.py

WORKDIR /app

EXPOSE 1883

CMD mosquitto -d && tail -f /var/log/mosquitto/mosquitto.log
