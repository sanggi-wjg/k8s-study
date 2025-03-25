# Springboot application

## Docker

```shell
docker build -t girr311/springboot-app .
# docker run -d -p 3355:8080 girr311/springboot-app -e REDIS_HOST=127.0.0.1

docker login
docker push girr311/springboot-app:latest 
```
