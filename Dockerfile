FROM python:3.7-slim

COPY requirements.txt /

RUN pip install -r /requirements.txt
RUN apt-get update -y &&\
    apt-get install curl -y &&\
    curl -sL https://deb.nodesource.com/setup_10.x | bash &&\
    apt-get install nodejs -y &&\
    node -v &&\
    npm -v &&\
    npm install -g serverless@1.52.2
