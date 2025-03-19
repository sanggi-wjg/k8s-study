## Container image push

```shell
docker build -t girr311/fastapi-app .
# docker run -d -p 8000:8000 girr311/fastapi-app

docker login
docker push girr311/fastapi-app:latest 
```
