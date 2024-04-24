FROM python:3.12-slim

WORKDIR /app

COPY src/ /app
COPY Makefile /app
COPY requirements.txt /app

RUN apt-get update && apt-get install make && pip3 install -r requirements.txt