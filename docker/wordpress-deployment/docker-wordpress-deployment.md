# Wordpress Deployment
In order to deploy a wordpress application, we should: 
- create a network
- create 2 volumes
  - one for wordpress
  - one for mysql
- create 2 containters
  - one for wordpress
  - one for mysql

## Network Creation
- `docker network create web`
- `docker network list`

## Volume Creation
- `docker volume create wordpress`
- `docker volume create mysql`
- `docker volume list`

## Image Download
### wordpress image
- `docker pull wordpress`
- mysql image: `docker inspect --type image mysql:latest`, this shows which are the parameters to fill while launching a container

### mysql image
- `docker pull mysql`
- `docker inspect --type image wordpress:latest`, this shows which are the parameters to fill while launching a containter
To get more info about these images, take a look at dockerhub.com

## Launch Containers
- `docker run -it --rm --net web -v mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw --name mysql -d mysql:latest`
- `docker run -it --net web --rm -v wordpress:/var/www/html -e WORDPRESS_DB_PASSWORD=my-secret-pw -p 8090:80 --name wordpress -d wordpress:latest`