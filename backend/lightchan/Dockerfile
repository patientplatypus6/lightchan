FROM python:3.8

WORKDIR /

SHELL ["/bin/bash", "-c"]

#COPY package*.json ./
COPY requirements.txt ./
RUN apt-get update
RUN apt-get install python3-pip -y
COPY ./ ./
RUN source env/bin/activate
RUN pip3 install -r ./requirements.txt

#SHELL ["/bin/bash", "-c"]
#RUN npm install
#RUN source env/bin/activate
#RUN apt-get update
#RUN apt-get install python3-pip -y
#Not working for some reason -- look into this later (change DNS maybe?)
#RUN pip3 install -r /tmp/requirements.txt 
#RUN pip3 install django django-cors-headers daphne
#RUN pip3 install django
#RUN pip3 install daphne
#RUN pip3 install django-cors-headers
#RUN daphne -b 0.0.0.0 -p 8001 lightchan.asgi:application

#socket.io port
EXPOSE 8001

CMD "./run.sh"

#CMD "daphne -b 0.0.0.0 -p 8001 lightchan.asgi:application"
