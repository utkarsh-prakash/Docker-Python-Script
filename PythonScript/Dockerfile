# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

COPY . /usr/src/myapp

WORKDIR /usr/src/myapp
RUN mkdir -p /usr/src/myapp/data

RUN pip3 install -r requirements.txt


CMD [ "python", "script.py"]