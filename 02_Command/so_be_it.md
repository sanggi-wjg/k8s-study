
# so be it

* https://kubernetes.io/ko/docs/reference/kubectl/cheatsheet/

## k3d
* https://k3d.io/stable/usage/commands/k3d/

### Cluster
```sh
k3d cluster create demo --agents 2 \
                        --agents-memory 4G \
                        --api-port 6443 \
                        --port 80:80@loadbalancer \
                        --port 443:443@loadbalancer \
                        --servers 2

k3d cluster edit demo --port-add 30001:3001@loadbalancer

k3d cluster start demo
k3d cluster stop demo
k3d cluster delete demo
``` 

---
## k8s

### 
```sh
kubectl apply -f manifest.yaml
kubectl delete -f manifest.yaml
```

### Namespace
```sh
kubectl get namespace

# If namespace is removed, resources that using namespace are also removed.
kubectl delete ns [namespace name] 
```

###
```sh
kubectl create namespace grafana
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm install grafana grafana/grafana \
    --namespace grafana \
    -f values.yaml \
    --wait
```