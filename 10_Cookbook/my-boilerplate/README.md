
## 일반적인 Kubernetes 프로젝트 구조
```
project-root/
├── charts/                 # Helm Chart 관련 디렉토리
│   └── my-app/             # 특정 애플리케이션을 위한 Helm Chart
├── manifests/              # 순수 Kubernetes YAML 매니페스트 파일 디렉토리
│   ├── base/               # Kustomize 기반의 기본 매니페스트 (공통 설정)
│   ├── overlays/           # Kustomize 오버레이 설정
│   │   ├── dev/            # 개발 환경용 설정
│   │   ├── staging/        # 스테이징 환경용 설정
│   │   └── prod/           # 프로덕션 환경용 설정
├── deployments/            # 배포 관련 YAML 파일들 (별도 관리 시)
│   ├── app/                # FastAPI 애플리케이션 등
│   ├── redis/              # Redis StatefulSet 및 Service
│   ├── monitoring/         # Grafana, Prometheus 등 모니터링 관련 리소스
│   └── ingress/            # Ingress 관련 리소스
├── crds/                   # Custom Resource Definitions (CRD) 정의
├── scripts/                # 스크립트 파일 (배포, 테스트, 초기화용)
├── configs/                # 애플리케이션 설정 파일
├── templates/              # YAML 템플릿 또는 Helm 템플릿
└── values/                 # Helm values.yaml (환경별 값 정의)
```

### charts
- 각 애플리케이션에 대해 별도의 Helm Chart를 만들고, 환경별 values.yaml을 통해 커스터마이징.

```
charts/
└── my-app/
    ├── Chart.yaml
    ├── values.yaml
    ├── templates/
    │   ├── deployment.yaml
    │   ├── service.yaml
    │   ├── ingress.yaml
    │   └── configmap.yaml
    └── README.md
```

### manifests
- base/에는 모든 환경에서 공통적으로 사용되는 리소스 정의를 배치하고, 환경별 설정(dev, staging, prod)은 overlays/에 관리.

```
manifests/
├── base/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── namespace.yaml
├── overlays/
│   ├── dev/
│   │   └── kustomization.yaml
│   ├── staging/
│   │   └── kustomization.yaml
│   └── prod/
│       └── kustomization.yaml
```

### deployments
- YAML을 사용해 배포 파일들을 관리하는 경우 사용합니다.

```
deployments/
├── app/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
├── redis/
│   ├── statefulset.yaml
│   └── service.yaml
├── ingress/
│   ├── ingress.yaml
│   ├── cert-manager.yaml
```

### configs
- 애플리케이션에 필요한 설정 파일(ConfigMap, Secret 등)을 관리합니다.

```
configs/
├── app-config.yaml
├── redis-config.yaml
└── secrets.yaml
```