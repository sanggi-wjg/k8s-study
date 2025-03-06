# k3d Cheat Sheet

* https://k3d.io/stable/usage/commands/k3d/

```sh
k3d cluster create demo --agents 2 \
                        --agents-memory 4G \
                        --api-port 6443 \
                        --port 80:80@loadbalancer \
                        --port 443:443@loadbalancer \
                        --servers 2
```

```sh
k3d cluster start demo
k3d cluster stop demo
k3d cluster delete demo
``` 

```sh
kubectl apply -f manifest.yaml
kubectl delete -f manifest.yaml
```

```sh
kubectl create namespace grafana
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm install grafana grafana/grafana \
    --namespace grafana \
    -f values.yaml \
    --wait
```