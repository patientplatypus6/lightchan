#FROM ubuntu:latest

#WORKDIR .
#COPY . .
#RUN echo "line 1"
#RUN apt-get update -y
#RUN echo "line 2"
#RUN apt-get install nodejs npm
#RUN echo "line 3"
#RUN npm install
#RUN echo "line 4"
#RUN npm run start
#RUN echo "line 5"

# pull official base image

FROM node:13.12.0-alpine

# set working directory
# RUN mkdir /app
WORKDIR .

# add `/app/node_modules/.bin` to $PATH

ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies

COPY package.json ./
COPY package-lock.json ./
RUN npm install

#RUN npm install react-scripts@3.4.1 -g --silent
# add app

COPY . ./

# start app

CMD ["npm", "start"]





