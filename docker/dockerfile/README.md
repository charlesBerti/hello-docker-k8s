# Dockerfile
Dockerfile specifies all the configurations to build an image.

## Terminology
- `FROM`: use which base image
- `LABEL`: replace the previous MAINTAINER
- `RUN`: effectuate the fellow functions: 
  - installation of packages
  - modification ofconfiguration
  - creation of links and directories
  - creation of users and groups
- `ENV`: define environment variables
- `COPY/ADD`: copy files from the host to the container
  - `COPY ./index.html /var/www/html/index.html`
- `ENTRYPOINT/CMD`: 
  - `Entrypoint`: launch the commands during the creation of the container
  - `CMD`: launch the only command during the execution of the container
- `WORKDIR`: switch path
- `USER`: execute the commands with which user
- `VOLUME`: mount a volume to the container
- `EXPOSE`: NAT container's port to the host's port
- `ONBUILD`:
- `HEALTHCHECK`: 
- `SHELL`: use which shell to execute commands

## Build Image
- `docker image build -t apache2-demo .`

## TP: Apache2 Web Server
- write a Dockerfile to create an image with packages php, apache (apache2, libapache2-mod-php)
- add a index.php file with: <?php phpinfo() ?>

See the [Dockerfile](Dockerfile) as the answer
- `docker image build -t apache2-demo .`
- `docker container run -d -p 8885:80 apache2-demo`
- `http://172.17.0.2/index.php`: direct access through browser
- `http://localhost:8885/index.php`: NAT access through browser
