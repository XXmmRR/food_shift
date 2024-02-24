FROM python:3.12.0b3-alpine

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 
EXPOSE 27017

COPY . .