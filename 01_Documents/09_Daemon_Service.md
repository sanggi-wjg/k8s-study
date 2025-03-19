# Daemon Service
k8s의 `DaemonSet` 기능으로 특정 노드마다 반드시 하나의 Pod가 실행되도록 보장하는 방식의 서비스로 일반적인 Deployment와 달리 클러스터의 모든 노드에 자동으로 배포되며 노드가 추가되면 해당 노드에도 자동으로 Pod가 생성 된다.

주로 아래 경우에서 사용:
- **로그 수집**: 모든 노드에서 로그를 수집하는 에이전트 실행 (Fluentd, Filebeat)
- **모니터링: 노드** 단위 메트릭을 수집하는 모니터링 에이전트 (Prometheus Node Exporter)
- **네트워크 관리**: CNI(Container Network Interface) 플러그인 실행 (Calico, Flannel)
- **보안**: 노드 단위의 보안 에이전트 실행 (Falco, OSSEC)
