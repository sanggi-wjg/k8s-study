# Managed Lifecycle

프로세스 상태확인만으로는 애플리케이션의 정상상태를 검사에 충분치 않다. 그렇기 때문에 상태 모니터링을 위해서는 다른 API가 추가로 필요하다.
- 실행을 준비하는데 도움이 필요한 애플리케이션도 있고 
- 깔끔한 종료 절차가 필요로하는 애플리케이션도 있다.

* `SIGTERM`: k8s가 컨테이너를 중지하기로 결정시 컨테이너로 `SIGTERM` 신호를 보낸다.
* `SIGKILL`: `SIGTERM` 수신 후에도 종료하지 않는다면 `SIGKILL` 신호로 강제 종료시킨다. 
  * `.spec.terminationGracePeriodSeconds` 필드로 팟별로 개별 정의할 수 있지만 재정의가 될 수 있어 보장되지는 않는다.


## Start, Stop Hook
수명주기 관리를 `SIGNAL`만 사용하는건 다소 제한이 있기 때문에 k8s는 `postStart`, `preStop` 설정을 제공하고 있다.

* `postStart`: 컨테이너가 생성된 후 컨테이너 프로세스와 비동기적으로 실행.
* 

```yaml
apiVersion: v1
kind: Pod
...
spec:
  containers:
  ...
    lifecycle:
      postStart:
        exec:
          command: ["sh", "-c", "sleep 30 echo \"hello world\" > /tmp/lifecycle"]
```
