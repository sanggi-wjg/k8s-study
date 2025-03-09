# Requirement

애플리케이션 배포, 관리 등을 성공적으로 수행하기 위한 자원 요구사항이나 런타임 의존성 등에 대해서 식별 및 정리 해야한다. 프로그래밍 언어, 프레임워크마다 요구사항이 다를 수 있으며 애플리케이션의 수행하는 역할을 고려 해야한다.

어떤 서비스는 고정 CPU와 고정 메모리를 가지는 서비스도 있고 데이터를 저장하기 위한 Stroage가 필요한 경우도 있을 수 있고 포트 번호 변경이 어려운 서비스가 있을 수도 있다.

> [!NOTE]
> 요구사항 템플릿 정의를 통해서 어느정도 해결할 수 있지 않을까?  
> 언어, 프레임워크, 포트번호, 스토리지 사용여부, 서비스 특징, CPU bound? I/O bound?

### **Resoure**
  - **CPU, Memory**
    - 고정 메모리: 고성능 처리가 필요한 서비스 경우 일정 수준 CPU, RAM을 보장 받아야 한다. (LLM, AI, BigData 등)
    - 동적 메모리: 트래픽에 따라 필요 리소스가 다른 경우 수평적 확장을 위한 동적 리소스 할당이 가능하도록 되어야 한다. (커머스 이벤트, 스트리밍 축구 국대 경기 등)
  - **Storage**
    - 클러스터 내 Redis를 aof 활성화하여 사용한다면 적절한 스토리지 설정이 필요
  - **Network, Permission**
    - 레거시 프로젝트내 socket 통신 혹은 쉘 통신이 있고 특정 포트를 사용한다면 네트워크 설정 변경이 어려울 수 있기에 미리 제약사항들을 파악하고 있어야 한다.
- **Framework, Language**
  - JVM 은 실행 옵션으로 힙 메모리 설정을 제공. (OOM 안전 보장 ❌)
  - PHP, GO 는 메모리 제한을 설정 가능. (OOM 에서 안전 보장 ❌)
  - Python은 메모리 제한 없지 않나?

### **Service**
  - 서비스 주요 기능들이 CPU bounded? I/O bounded? 에 따라 자원 설정을 다르게 가져가야 한다.
  - 예를 들어 Celery 배치 서비스 설정시
    - **CPU bounded**
      - 효율적인 계산을 위해 계산 로직들은 multi-processing 을 이용하여 구현 되어 있다면 CPU를 많이 주어야 한다.
      - 계산을 많이 하지만 로직들은 multi-processing 으로 구현되어 있지 않다면 CPU를 많이 줄 필요가 없다.
      - 또한 언어와 마찬가지로 Celery 적절한 옵션이 필요
    - **I/O bounded**
      - 파일 생성, 네트워크 통신 등이 많고 coroutine, multi-threading 동시 실행이 많은 경우 CPU 보다는 메모리 설정이 중요하다.
      - Celery를 사용한다면 multi-threading 구현 하지 않아도 concurrency 옵션으로 gevent, eventlet을 지원하니 구현단과 상관없이 설정이 가능하다.  
      (멀티 쓰레딩의 경우 DB Connection에 대한 부분도 계획이 필요하다.)
  
> [!TIP]
> 자원에 대한 요구사항을 미리 파악해야하는 이유는 2가지 중요한 이유가 있다.
> 1. k8s는 효율적인 하드웨어 사용을 위해 적절한 컨테이너의 실행 위치를 결정.
> 2. 서비스의 요구사항을 포함하여 전체 인프라의 효율적인 자원, 용량 계획을 세우고 경제적 비용 효율을 높일수 있다.

---
## Runtime dependency

### Storage dependency
가장 일반적인 런타임 의존성은 `Storage` 이다. 컨테이너 파일 시스템은 컨테이너 종료시 삭제된다. k8s는 pod 레벨에서 컨테이너 재시작시에도 삭제되지 않고 유지되는 storage 기능을 제공한다.

기본 값으로 볼륨 타입은 `emptyDir` 이며 pod이 살아있는 동안 존재하고 pod 삭제시 같이 삭제된다.
볼륨을 유지하기 위해서는 명시적으로 설정을 해주어야 한다.
* docs 참고: https://kubernetes.io/ko/docs/concepts/storage/volumes/#local

스케줄러는 팟이 요청한 볼륨 종류를 판단하며 제공하지 않는 볼륨이라면 결코 스케줄링 되지 않는다.

### Configuration dependency
두번째 의존성으로 설정 의존성이 있다. 서비스를 위한 애플리케이션들은 대부분 설정 정보들이 필요로 하며 k8s에서 제공하는 권장 방법은 `ConfigMap` 이며 설정 방법으로는 2가지가 있다.
1. 환경변수 설정
2. 파일 시스템 설정

2가지 모두 `ConfigMap`에 의존성을 가지며 볼륨과 마찬가지로 `ConfigMap`이 설정이 되어 있지 않다면 Pod은 시작되지 않는다. 일반적으로 민감하지 않은 정보에 대해서 사용 한다.

> [!NOTE]
> 비슷한 개념으로 `Secret`이 있으며 좀 더 안전한 방법을 제공한다. 사용 방법은 `ConfigMap`과 동일하다.
> 민감 정보를 다루어야할 경우 사용하며 기본적으로 평문으로 저장되어 암호화 설정과 접근 권한을 설정 해애햔다.
> 보안을 위해서 시크릿 전문 서비스를 사용하는 것도 고려할 수 있다.


---
## Resource profile
컨테이너 자원 요구사항에 대해서는 역시 많은 고민과 실험이 필요로 한다. Resource 설정시 고려할 점은 크게 2개 이다.
1. Compressible resource: CPU, Network connection, bandwidth 처럼 제어 가능한
   1. CPU 초과 설정시 race condition 발생
2. Incompressible resource: Memory 처럼 제어 불가능한
   1. Memory 초과 설정시 OOM 발생

* container resource limit 혹은 stream log file, linux network 관련 설정 비슷

requests, limits 를 어떻게 설정하냐 예 따라 
* **Best-Effort Pod**: requests와 limits 미설정시 가장 낮은 우선순위로 고려되며 Incompressible reource 고갈시 pod을 종료 시킨다.
* **Busrtable Pod**: requests와 limits 모두 설정되어 있지만 값이 다른 경우 Incompressible resource 압박시 종료될 수도 있다.
* **Guarated Pod**: requests와 limits 모두 동일하게 설정되어 있다면 가장 높은 우선순위로 고려되며 가장 나중에 죽는다.

> [!TIP]
> 운영환경에서 최적으로 자원을 활용하기 위해 `Best-Effort`, `Burstable`을 주로 사용할텐데 동적인 환경에서 많은 컨테이너가 동시에 시작되고 종료될 수 있다. 이런 현상이 발생해도 그다지 치명적이지 않을 것이다.
> 좀더 안정적으로 운용하고 싶다면 `Guaranted`를 이용하면 된다. (만약 컨테이너가 죽는다면 자원 부족일 확률이 높다.)

> [!WARNING]
> 서비스 중 자원 부족한 경우를 고려하여 자원 할당을 설정해야한다.

### Pod Priority
다음과 같이 하나 이상의 PriorityClass를 설정하여 Pod의 우선순위를 설정할 수 있다.
* https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/
* linux nice 비슷

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000000 # 값이 높을수록 
globalDefault: false
description: "This priority class should be used for XYZ service pods only."

---
apiVersion: v1
...
priorityClassName: high-priority
```