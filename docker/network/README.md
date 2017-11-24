# Network

## Basic Manipulation
- list: `docker network list`
- create: `docker network create Network_ID`
- attach a container to a network: `docker container run --name vm1 -ti --net=Network_ID ubuntu:xenial`

## port exposition
- NAT port of container to a random port of host: `docker container run -d -P training/webapp python app.py`
- NAT port of container to port of host: `docker container run -d -p 8888:5000 training/webapp python app.py`

## TP
### Inter-VM Communication
- `docker network create test_net`
- `docker container run --name vm1 -ti -d --net=test_net ubuntu:xenial`
- `docker container run --name vm2 -ti --net=test_net ubuntu:xenial`
- in the container `vm2`: 
    - `apt update`
    - `apt install iputils-ping`
    - `ping vm2`

### Web Server
- `docker container run -ti --rm -p 8888:80 ubuntu:xenial`
- install and launch apache2 in the container
    - `apt update`
    - `apt install apache2 vim`
    - `vim /var/www/html/index.html`
    - `apache2ctl -D FOREGROUND`

