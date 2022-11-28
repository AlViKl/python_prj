# python_prj

To start a project need to execute:
Build image/images
```
docker-compose -f docker-compose-dev.yml build
```
Run docker-compose to start containers
```
docker-compose -f docker-compose-dev.yml up -d
```
To stop and remove containers
```
docker-compose -f docker-compose-dev.yml down
```


Temporary solution befor packing app to docker image, to provide database connection string using ENV:
```
export URI='postgresql://<username>:<psw>@localhost:<port>/<database>'
```
