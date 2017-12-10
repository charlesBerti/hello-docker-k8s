# Python Web Application

## Web
### Build & Run
- edit *Dockerfile*
- `docker build -t friendlyhello .`
- `docker run -p 8888:80 friendlyhello`
- `docker run -d --rm -p 8888:80 friendlyhello`: run the app in the background and remove after stopping
- `docker container kill docker_id`

### Tag & Image
- `docker tag firendlyhello xxx/yyy:zzz`
- `docker image ls`
- `docker login`
- `docker push xxx/yyy:zzz`

### Service
- edit *docker-compose.yml*
- `docker swarm init`
- `docker stack deploy -c docker-compose.yml getstartedlab`
- `docker service ls`
- `docker service ps getstartedlab_web`
- `docker contaienr ls -q`
- `curl -4 http://localhost:8880`
- `docker stack rm getstartedlab`
- `docker swarm leave --force`