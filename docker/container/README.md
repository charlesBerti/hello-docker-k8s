# Container
## ps
- `docker container ps`
- `docker container ps -a`

## run
- `docker container run --name test ubuntu:xenial`: name of the container
- `docker container run -ti ubuntu:xenial`: interactive mode (executing in bg and attached):
- `docker container run -ti -d ubuntu:xenial`: detached mode (executing in bg but not attached)

## exec
- `docker container exec –ti Container_ID /bin/bash`: run a cmd in a container

## stop/kill/start
- `docker container start Container_ID`: start/ relaunch
- `docker container stop Container_ID`: stop (send SIGTERM + SIGKILL)
- `docker container kill Container_ID`: kill (send SIGKILL)

## rm
- `docker container rm Container_ID`: remove a *stopped* docker
- `docker container run --rm -ti ubuntu:xenial`: remove after the execution

## TP
- `docker container run hello-world`
- `docker container ps`: we can't see the container `hello-world`
- `docker container ps -a`: - normally, we can see the container now, why?
- `docker container run -it --rm ubuntu:xenial /bin/bash` 
- from another terminal launch: `docker container ps`, what's the difference between the previous case? Why?
- in the container
  - launch: `ps faux`
  - quit the container: `exit`
  - check the status: `docker container ps -a`
