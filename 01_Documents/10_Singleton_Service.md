# Singleton Service
"클러스터 내에서 단 하나의 인스턴스만 동작하도록 보장되는 서비스"를 지칭할 때 사용하며 `StatefulSet`와 `replicas: 1` 설정으로 단일 pod만 실행되도록 구성할 수 있다.

사용 예시:
1. polling 서비스
2. 단일 Consumerm (or application)

> [!NOTE]
> `replicas: 1`로 설정 되었다고 하나의 인스턴스 실행만을 보장하지는 않는다. (아마 Deployments?)
> k8s는 일반적으로 일관성 보다는 가용성을 선호한다. 검증이 실패하는 경우 등에서 pod의 수는 설정된 값 보다 많을 수 있다.


## StatefulSet
`StatefulSet`은 가용성보다는 일관성을 선호하고 엄격한 싱글톤을 보장하고 그에 따라 복잡성 존재한다.

StatefulSet로 관리되는 싱글톤 pod은 단일 pod만 소유하고 지속적인 네트워크 식별이 가능하다.  
이런 경우 `headless service`로 설정 하는게 좋다. (clusterIp: None, 서비스에 가상 IP가 없고 종단점 DNS record만 생성하여 사용)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: redis-service
  namespace: redis-namespace
spec:
  clusterIP: None # Headless Service를 생성
  selector:
    app: redis-storage
  ports:
  - name: redis
    port: 6379
    targetPort: 6379
```

## PDB, PodDistruptionBudget
사용자가 관리하는 애플리케이션의 가용성을 보장하기 위해 사용하는 섫정으로
클러스터에서 노드 장애, 유지보수 작업(예: 롤링 업데이트, 수동 노드 삭제 등) 또는 기타 스케줄링 이벤트로 인해 애플리케이션이 과도하게 중단되지 않도록 보호한다. 애플리케이션이 특정 비율이나 수 아래로 절대 떨어지지 않아야 하는 경우 유용한 설정이다.

- **MinAvailable**: 최소 가용 pod 수
- **MaxUnavailable**: 최대 비가용 pod 수
  - MinAvailable, MaxUnavailable 동시 설정은 불가능하다.
- **Distruption**: pod이 종료되는 모든 경우(중단)
- **Pod Selector**: 특정 그룹에만 적용 가능


### minAvailable
```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: web-app-pdb
  namespace: web-namespace
spec:
  minAvailable: 2 # 최소 2개의 Pod는 항상 가용해야 함
  selector:
    matchLabels:
      app: web-app # 이 라벨을 가진 Pod에만 적용
```

### maxUnavailable
```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: example-pdb
spec:
  maxUnavailable: 1 # 최대 1개의 Pod만 중단 가능
  selector:
    matchLabels:
      app: example-app
```