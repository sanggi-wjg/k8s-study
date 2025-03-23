---
marp: true
# theme: uncover
# theme: gaia
# _class: invert
---

# Singleton Service
"클러스터 내에서 단 하나의 인스턴스만 동작하도록 보장되는 서비스"를 지칭할 때 사용하며 `StatefulSet`와 `replicas: 1` 설정으로 단일 pod만 실행되도록 구성할 수 있다.

사용 예시:
1. polling 서비스
2. 단일 Consumerm (or application)

> [!NOTE]
> `replicas: 1`로 설정 되었다고 하나의 인스턴스 실행만을 보장하지는 않는다. (아마 Deployments?)
> k8s는 일반적으로 일관성 보다는 가용성을 선호한다. 검증이 실패하는 경우 등에서 pod의 수는 설정된 값 보다 많을 수 있다.

---

## StatefulSet
`StatefulSet`은 가용성보다는 일관성을 선호하고 엄격한 싱글톤을 보장하고 그에 따라 복잡성 존재한다.

StatefulSet로 관리되는 싱글톤 pod은 단일 pod만 소유하고 지속적인 네트워크 식별이 가능하다. 이런 경우 `headless service`로 설정 하는게 좋다. (clusterIp: None, 서비스에 가상 IP가 없고 종단점 DNS record만 생성하여 사용)