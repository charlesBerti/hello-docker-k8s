# Container
## ps
- `docker container ps`
- `docker container ps -a`

## run
- name: `docker container run --name test ubuntu:xenial`
- interactive mode (executing in bg and attached): `docker container run -ti ubuntu:xenial`
- detached mode (executing in bg but not attached): `docker container run -ti -d ubuntu:xenial`

## exec
run a new process inside a running container: 
- `docker container exec –ti Container_ID /bin/bash`

## stop/kill/start
- stop (send SIGTERM + SIGKILL): `docker container stop Container_ID`
- start (relaunch): `docker container start Container_ID`
- kill (send SIGKILL): `docker container kill Container_ID`

## rm
- remove a stopped docker: `docker container rm Container_ID`
- --rm remove after execution: `docker container run --rm -ti ubuntu:xenial`

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
