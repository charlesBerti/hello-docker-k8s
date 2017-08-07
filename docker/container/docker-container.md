# Container
## ps
- `docker container ps`
- `docker container ps -a`

## run
- `docker container run -name test ubuntu:xenial`
- interactive mode: `docker container run -ti ubuntu:xenial`
- detached mode: `docker container run -ti -d ubuntu:xenial`

## exec
run a new process inside a running container: `docker container exec –ti Container_ID /bin/bash`

## stop/kill/start
- stop: `docker container stop Container_ID`
- kill: `docker container kill Container_ID`
- start: `docker container start Container_ID`

## rm
- `docker container rm Container_ID`
- --rm: `docker run --rm --ti ubuntu:xenial`

## TP
- `docker run hello-world`
- `docker ps`
- we cann't see the container hello-world: `docker ps -a`
- normally, we can see the container now, why?: `docker run -it --rm ubuntu:xenial /bin/bash`
- from another terminal, launch: `docker ps`
- What's the difference between the previous case? Why?

### in the container
- launch: `ps faux`
- quit the container: `exit`
- check the status: `docker ps -a`
