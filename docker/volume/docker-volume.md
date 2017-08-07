# Volume
## list
- `docker volume list`

## create
- `docker volume create Volume_Name`

## Inspect
- `docker volume inspect Volume_Name`

## Attachment
- attach a volume to a container: `docker container run ... -v data:/data -v sql:/var/lib/mysql -v web:/var/www ...`

## rw/ro
- setup a permission for the volume: `docker container run ... -v data:/data:rw ...`
- setup a permission for the volume: `docker container run ... -v data:/data:ro ...`