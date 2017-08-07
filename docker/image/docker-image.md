# Image
## ls
- `docker image ls`

## search/ pull
- search: `docker search ubuntu:xenial`
- pull: `docker image pull ubuntu:xenial`

## rm
- `docker image rm Image_ID`

## create/commit
- create an image from an existing container: `docker container commit -m "comment" -a "author" Container_ID Image_Name:TAG`

## tag
- change tag: `docker image tag image[:tag] image:new_tag`

## push
push to a remote registry
- login: `docker login hub.docker.com –u xxx –p yyy`
- push (when creating an image, we should specify its login): `docker image push wukongsun/xenial:net`

## TP
### Pull Image
Pull a mysql image
- `docker image list`
- `docker search mysql`
- `docker pull mysql`
- `docker image list`
- `docker ps -a`

What's the difference between a container and an image? 

### Create Image
Create a Xenial image with ifconfig install
- `sudo apt-get update`
- `sudo apt-get install net-tools`
- `docker container commit -m "ubuntu:xenial with net-tools package" -a "WuKong" Container_ID Xenial:net`
