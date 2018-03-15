# TP: Frontend and Backend Web

- `docker image build -t backend ./backend`
- `docker image build -t frontend ./frontend`

- `docker network create internal`

- `docker container run --name backend -ti -d --net=internal backend`
- `docker container run --name frontend -ti -d --net=internal -p 8888:8888 frontend`