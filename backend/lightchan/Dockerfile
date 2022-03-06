
FROM python:3.8-alpine

RUN apk update && apk add --no-cache \
    gcc python3-dev \
    postgresql-libs postgresql-dev musl-dev

RUN mkdir /code
COPY requirements.txt /code
WORKDIR /code
RUN apk add --no-cache --upgrade bash
RUN apk add python3 py3-pip 
RUN apk add libffi-dev
RUN pip3 install -r ./requirements.txt --verbose
COPY . /code/