FROM python:3.12-slim

WORKDIR /app

RUN mkdir src/

COPY src/ /app/src/
COPY Makefile /app
COPY requirements.txt /app

RUN apt-get update && apt-get install make && pip3 install -r requirements.txt