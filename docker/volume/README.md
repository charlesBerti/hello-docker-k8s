# Volume

## Basic Manipulation
- list: `docker volume list`
- create: `docker volume create Volume_Name`
- inspect: `docker volume inspect Volume_Name`
- attach a volume to a container: `docker container run -it -v Volume_Name:path ubuntu:xenial`
- setup a permission for the volume: `docker container run ... -v Volume_Name:path:rw ...`
- setup a permission for the volume: `docker container run ... -v Volume_Name:path:ro ...`

## TP
- `docker container run -it --rm ubuntu:xenial /bin/bash`
- in container: `ls`
- `docker volume create my_volume`
- `docker container run -it --rm -v my_volume:/my_data_path ubuntu:xenial /bin/bash`
- in container: `ls`
