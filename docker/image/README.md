# Image

## basic manipulation
- list: `docker image ls` 
- search: `docker search ubuntu:xenial`
- inspect: `docker image inspect ubuntu:xenial`
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
```bash
docker container run -it --rm ubuntu:xenial /bin/bash
```
- in container, run:
```bash
apt update
apt install net-tools
```
- from another terminal launch: `docker container ps`, where you can find container_ID
- `docker container commit -m "xenial with net-tools" -a "wukong" Container_ID wukongsun/xenial:net`
- `docker login`
- `docker image push wukongsun/xenial:net`
