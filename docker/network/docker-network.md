# Network
## list
- `docker network list`

## create
- `docker network create Network_Name`

## Attachment
- attach a container to a network: `docker container run --name test1 -ti --net=Network_Name ubuntu:xenial /bin/bash`

## port exposition
- NAT a containter port to the host: `docker run --rm -it demo -p 8080::80`