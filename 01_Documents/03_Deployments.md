# Deployment
Deployment는 Kubernetes에서 애플리케이션을 배포하고 관리하는 객체
- Pod를 생성, 업데이트하는 역할 수행
- 애플리케이션을 자동으로 복구하고 롤백할 수 있는 기능 제공
- Rolling Update가 가능하여 무중단 서비스 제공

주요 기능으로
1. **Replica 관리**: 여러개 Pod을 생성하여 트래픽 분산
2. **Self-healing**: Pod이 죽으면 다시 생성
3. **Rolling Update**: 신규 버전의 애플리케이션을 점진적 배포(무중단)
4. **Rollback**: 문제시 이전버전으로 롤백
5. **Scaling**: `kubectl scale` 명령어로 실행중인 Pod 개수 조절


## Rolling update
Deployment의 기본 배포 설정값으로 무중단에 가깝게 보장한다. 일반적으로 알려진 롤링 배포 개념과 동일하고 새로운 컨테이너로 이전 컨테이너를 교체하는 동작을 수행한다. 추가 기능으로는 교체 동작의 비율을 설정할 수 있다는 것이다. (설정값: maxSurge, maxUnavailable)

```yaml
apiVersion: apps/v1
kind: Deployment
...
spec:
  replicas: 2          # RollingUpdate를 사용하기 위해서는 2개 이상의 레플리카 필요
  ...
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1       # 업데이트 동안 실행될 수 있는 최대 팟 개수
      maxUnavailble: 1  # 업데이트 동안 사용 불가능한 최대 팟 개수
```
> [!WARNING]
> 롤링 배포시 무중단을 위해서 `Readiness` 에 대한 설정이 필요하다.

## Recreate
두 버전의 컨테이너가 실행되서는 안되는 특정 경우도 있을 수 있다. 그런 경우 Recreate를 사용할 수 있다.
우선적으로 현재 버전의 컨테이너들을 모두 죽인 다음에 새로운 버전의 컨테이너들을 시작한다.

## Blue-Green deplpoyment
일반적으로 알려진 Blue-Green 배포 개념으로 다운타임을 최소화 하고 위험성을 줄이는 배포 전략이다. 
확장서비스(Service mesh, Knative)를 사용하지 않는다면 기본적으로 수동으로 실행되며 신규 버전 컨테이너가 생성 되어도 요청을 바로 보내지 않고 실제 요청을 처리할 준비가 되었을 때 트래픽을 이전 버전 컨테이너에서 신규 버전 컨테이너로 전환한다.

> [!WARNING]
> Blue-Green deployment 전략은 동시에 여러 버전들이 존재하는 것을 방지함으로 복잡성을 줄여주지만 컨테이너들이 모두 실행되어야 해서 용량을 2배로필요로 한다.

## Canary release
일반적으로 알려진 카나리 배포 개념으로 소수 사용자만 신규 버전으로 요청을 보내고 문제가 없다면 신규 버전 컨테이너들로 교체하는 방식이다.