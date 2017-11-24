# Volume

## Basic Manipulation
- list: `docker volume list`
- create: `docker volume create Volume_Name`
- inspect: `docker volume inspect Volume_Name`
- attach a volume to a container: `docker container run -ti -v data:/data ubuntu:xenial`
- setup a permission for the volume: `docker container run ... -v data:/data:rw ...`
- setup a permission for the volume: `docker container run ... -v data:/data:ro ...`

## TP
- `docker volume create data`
- `docker container run -ti -v data:/data ubuntu:xenial`