# WordPress Deployment
In order to deploy a *wordpress* application, we should:
- create 1 network
- create 2 volumes
  - 1 for wordpress
  - 1 for mysql
- create 2 containers
  - 1 for wordpress
  - 1 for mysql

## Network Creation
- `docker network create web`
- `docker network list`

## Volume Creation
- `docker volume create wordpress`
- `docker volume create mysql`
- `docker volume list`

## WordPress Image
- `docker image pull wordpress`
- `docker image inspect wordpress:latest`: this shows the parameters to fill while launching a container

To get more info about these images, take a look at *dockerhub.com*

## MySql Image
- `docker image pull mysql`
- `docker image inspect mysql:latest`, this shows the parameters to fill while launching a container

## Launch Containers
- `docker container run --name mysql -ti -d --rm --net web -v mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw  mysql:latest`
- `docker container run --name wordpress -ti -d --rm --net web -p 8090:80 -v wordpress:/var/www/html -e WORDPRESS_DB_PASSWORD=my-secret-pw wordpress:latest`
