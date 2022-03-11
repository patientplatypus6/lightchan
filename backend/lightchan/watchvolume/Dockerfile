FROM ubuntu:latest

ENV DOCKER_VERSION='20.10.7'
RUN apt-get update 
RUN apt-get install curl -y
# RUN apt-get install systemd -y

RUN set -ex \
    && DOCKER_FILENAME=https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz \
    && curl -L ${DOCKER_FILENAME} | tar -C /usr/bin/ -xzf - --strip-components 1 docker/docker

# just to keep docker container from exiting on finishing process
ENTRYPOINT ["tail", "-f", "/dev/null"]


# RUN docker ps

# RUN system start docker
# RUN systemctl start docker
# RUN service docker start
# RUN docker ps
# RUN docker ps


# RUN apt-get update && \
#     apt-get -qy full-upgrade && \
#     apt-get install -qy curl && \
#     apt-get install -qy curl && \
#     curl -sSL https://get.docker.com/ | sh

# RUN docker ps

# RUN apt-get update
# RUN apt-get install ca-certificates curl gnupg lsb-release -y
# RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
# RUN echo \
#   "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
#   $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
# RUN apt-get update
# RUN apt-get install docker-ce docker-ce-cli containerd.io -y -1
# RUN docker ps 