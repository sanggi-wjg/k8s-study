# ArgoCD
* https://argo-cd.readthedocs.io/en/stable/getting_started/

## Install ArgoCD
```sh
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

```

## Login
```sh
# port forwarding argocd-server(pod) 
argocd admin initial-password -n argocd
# 7PQwDSZ3M0tTjQEZ
```


## Install ArgoCD Image updater
```sh
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj-labs/argocd-image-updater/stable/manifests/install.yaml
```

## Create App
```sh
argocd app create springboot-app \
  --repo https://github.com/sanggi-wjg/k8s-study.git \
  --path 10_Cookbook/my-boilerplate/deployments/springboot-app \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default \
  --sync-policy automated \
  --auto-prune

argocd app create fastapi-app \
  --repo https://github.com/sanggi-wjg/k8s-study.git \
  --path 10_Cookbook/my-boilerplate/deployments/fastapi-app \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default \
  --sync-policy automated \
  --auto-prune
```
