# How to

## Prometheus
```sh
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

kubectl create namespace monitoring

helm install prometheus prometheus-community/prometheus \
  --namespace monitoring \
  -f monitoring/prometheus-values.yaml \
  --wait

helm uninstall prometheus -n monitoring
```

---
## Redis Exporter
```sh
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm upgrade --install redis-exporter prometheus-community/prometheus-redis-exporter \
  --set redisAddress="redis://redis-service.redis-namespace.svc:6379" \
  --namespace monitoring \
  --wait

helm uninstall redis-exporter -n monitoring
```

kubectl get configmap prometheus-prometheus-kube-prometheus-prometheus-rulefiles-0 -n monitoring -o yaml

---
## Grafana
```sh
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

# helm install grafana grafana/grafana \
#     --namespace grafana-namespace \
#     -f monitoring/grafana-values.yaml \
#     --wait

helm upgrade --install grafana grafana/grafana \
    --namespace monitoring \
    -f monitoring/grafana-values.yaml \
    --wait

helm uninstall grafana -n monitoring
```

### Grafana datasource
TODO: values로...

#### Prometheus
* http://prometheus-server.monitoring.svc

#### Redis-datasource
* redis://redis-service.redis-namespace.svc:6379

```
curl redis-exporter-prometheus-redis-exporter.monitoring.svc:9121/metrics
curl prometheus-prometheus-pushgateway.monitoring.svc:9091/metrics
curl prometheus-server.monitoring.svc:9090
```