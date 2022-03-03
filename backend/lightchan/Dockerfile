
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
#CMD ["python3", "manage.py", "runserver"]  


#FROM python:3

#RUN mkdir /code
#COPY requirements.txt /code
#WORKDIR /code

#RUN pip install --no-cache-dir -r requirements.txt

#COPY . .

#CMD [ "python3", "manage.py runserver" ]


#RUN apk update && apk add --no-cache \
#    # Required for installing/upgrading postgres, Pillow, etc:
#    gcc python3-dev \
#    # Required for installing/upgrading postgres:
#    postgresql-libs postgresql-dev musl-dev

# Set work directory
#RUN mkdir /code
#COPY requirements.txt /code
#WORKDIR /code

#RUN apk add --no-cache --upgrade bash

#Install dependencies into a virtualenv
#RUN pip install --upgrade pipenv
#COPY ./Pipfile .
#COPY ./Pipfile.lock .
#RUN pipenv install --dev --deploy

#RUN apk add python3 py3-pip 
#RUN apk add libffi-dev
#apk add py3-pip
#RUN apt-get update
#RUN apt-get install python3-pip -y
#RUN pip3 install -r ./requirements.txt --verbose

#RUN pip3 install django django-cors-headers daphne

# Copy project code
#COPY . /code/
