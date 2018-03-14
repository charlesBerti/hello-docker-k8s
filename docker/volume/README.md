# Volume

## Manipulation
- `docker volume list`: list
- `docker volume inspect VOL_ID`: inspect
- `docker volume create VOL_ID`: create
- `docker container run -it --rm -v VOL_ID:path ubuntu:xenial`: attach a volume to a container
  - `docker container run ... -v Volume_Name:path:rw ...`: setup *rw* permission for the volume
  - `docker container run ... -v Volume_Name:path:ro ...`: setup *ro* permission for the volume

## TP
- `docker container run -it --rm ubuntu:xenial /bin/bash`
- `ls /`: check the path in the container
- `docker volume create test_volume1`
- `docker container run -it --rm -v test_volume1:/data ubuntu:xenial /bin/bash`
- `ls /`: check the path in the container
