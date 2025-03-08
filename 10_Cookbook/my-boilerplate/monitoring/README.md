
## Grafana
```sh
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

kubectl create namespace grafana-namespace

# helm install grafana grafana/grafana \
#     --namespace grafana-namespace \
#     -f monitoring/grafana-values.yaml \
#     --wait

helm upgrade --install grafana grafana/grafana \
    --namespace grafana-namespace \
    -f monitoring/grafana-values.yaml \
    --wait
```

## Redis Exporter
```sh
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

kubectl create namespace prometheus-namespace

helm upgrade --install redis-exporter prometheus-community/prometheus-redis-exporter \
  --set redisAddress="redis://redis-service.redis-namespace.svc:6379" \
  --namespace prometheus-namespace \
  -f monitoring/prometheus-values.yaml
```

curl  prometheus-namespace.prometheus-redis-exporter.svc:9121

curl redis-exporter-prometheus-redis-exporter.prometheus-namespace.svc:9121