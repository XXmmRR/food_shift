FROM python:3.12.0b3-alpine

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

EXPOSE 27017

COPY . .