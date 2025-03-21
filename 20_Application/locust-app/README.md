# Locust application

## Docker

```shell
docker build -t girr311/locust-app .
# docker run -d -p 8000:8000 girr311/locust-app

docker login
docker push girr311/locust-app:latest 
```

## Local

```shell
# Web
locust -f main.py --host=http://127.0.0.1:8000

# Command line
locust -f main.py \
    --host http://127.0.0.1:8000 \
    --headless \
    --users 100 \
    --spawn-rate 0.5 \
    --run-time 2m \
    --stop-timeout 1s \
    --only-summary
```
