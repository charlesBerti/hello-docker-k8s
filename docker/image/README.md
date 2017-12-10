# Image

## basic manipulation
- list: `docker image ls` 
- search: `docker search ubuntu:xenial`
- inspect: `docker image inspect ubuntu:xenail`
- pull: `docker image pull ubuntu:xenial`
- rm: `docker image rm Image_ID`
- change tag: `docker image tag old_image:old_tag new_image:new_tag`

## create/commit/ push
- create an image from an existing container: `docker container commit -m "comment" -a "author" Container_ID Image_Name:TAG`
- push to a remote registry
  - login: `docker login`
  - push (when creating an image, we should specify its login): `docker image push wukongsun/xenial:net`

## TP
### Download a MySQL image
- `docker image list`
- `docker search mysql`
- `docker pull mysql`
- `docker image list`
- `docker ps -a`

What's the difference between a container and an image? 

### Create a Xenial Image with ifconfig
- `apt update`
- `apt install net-tools`
- `docker container commit -m "xenial with net-tools" -a "wukong" Container_ID xenial:net`
