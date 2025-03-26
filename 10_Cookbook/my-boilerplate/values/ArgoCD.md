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
```


## Install ArgoCD Image updater
```sh
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj-labs/argocd-image-updater/stable/manifests/install.yaml
```