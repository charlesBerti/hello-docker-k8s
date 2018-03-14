# Network

## Drivers
- bridge: 
- host: 

## Manipulation
- `docker network list`: list
- `docker network inspect bridge`: inspect
- `docker network create NET_ID`: create
- `docker container run --name vm1 -ti --rm --net=NET_ID ubuntu:xenial`: launch a container in a network
- `docker network connect NET_ID Container_ID`: connect a container to a network, one container can be connected to multiple networks
- `docker network disconnect NET_ID Container_ID`: disconnect

## Port Exposition
- `docker container run -d -P training/webapp python app.py`: NAT port of the container to a random port of the host
- `docker container run -d -p 8888:5000 training/webapp python app.py`: NAT port of the container to port of the host

## TP
### Inter-VM Communication
- `docker network create test_net`
- `docker container run --name vm1 -ti -d --net=test_net ubuntu:xenial`
- `docker container run --name vm2 -ti --net=test_net ubuntu:xenial /bin/bash`
- in the container `vm2`: 
    - `apt update`
    - `apt install iputils-ping`
    - `ping vm1`

### Web Server
- `docker container run -ti --rm -p 8888:80 ubuntu:xenial`
- install and launch apache2 in the container
    - `apt update`
    - `apt install apache2 vim`
    - `vim /var/www/html/index.html`
- `apache2ctl -D FOREGROUND`: find your container IP
- access the web page from host OS at IP:80 

