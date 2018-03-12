# Swarm
## Terminology
- Swarm: a swarm is a group of machines that are running Docker and joined into a cluster.
The machine can be physical or virtual.
After joining a swarm, a machine becomes a node.
- Swarm manager: swarm managers are the only machines in a swarm that can execute your commands, or authorize other machines to join the swarm as workers.
- Workers: workers are just there to provide capacity.
- Swarm mode: after switching into the swarm mode, docker will run the commands you execute on the swarm you're managing, rather than just on the current machine.

## Setup
### Swarm Manager
- `docker swarm init`: enable swarm mode and make your current machine a swarm manager

### Swarm Worker

- `docker swarm join`: on other machines to have them join the swarm as workers

### docker-machine
-  install: ```
curl -L https://github.com/docker/machine/releases/download/v0.13.0/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine &&
chmod +x /tmp/docker-machine &&
sudo cp /tmp/docker-machine /usr/local/bin/docker-machine```
- `docker-machine create --driver virtualbox myvm1`
- `docker-machine create --driver virtualbox myvm2`
- `docker-machine start myvm1`
- `docker-machine ssh myvm1 "docker swarm init --advertise-addr 192.168.99.100"`: make myvm1 as a manager
- `docker swarm join --token SWMTKN-1-1xhjmxgg41iqno69prtm6w67xrvu0yi7rkf0mr197u199rbp8a-4bx2y0vzmy2t7jpj4uber5a3t 192.168.99.100:2377`: make myvm2 as a worker
- `docker-machine ssh myvm1 "docker node ls"`: check nodes of a swarm
- `eval $(docker-machine env myvm1)`: set local shell as the shell of myvm1
- `docker stack deploy -c docker-compose.yml getstartedlab`: launch the service
- `curl -4 http://192.168.99.100:8890`
- `docker stack rm getstartedlab`: cleanup
- `eval $(docker-machine env -u)`: unset ENV

## TP: Python Web Application Deployment
- [Python Web Application Deployment](tp_pythonweb/README.md)