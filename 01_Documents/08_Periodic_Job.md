# Periodic Job
Periodic Job은 k8s에서 주기적으로 실행되는 Job을 의미하며
일반적으로 CronJob을 사용하여 구현.

## 표현식
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: periodic-job
spec:
  schedule: "*/5 * * * *"  # 5분마다 실행
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: periodic-task
            image: busybox
            command: ["echo", "Hello! This is a periodic job."]
          restartPolicy: Never
```


## 운영시
1. 불필요한 Job이 쌓이지 않게 자동 삭제 설정
   1. `ttlSecondsAfterFinished: 600`: 600초(10분) 후 Job 자동 삭제
2. 중복 실행 방지 
   1. `concurrencyPolicy: Forbid`: 이전 Job이 끝나야 새로운 Job 실행
3. 특정 시간 내에 실행되지 않으면 강제 종료
   1. `activeDeadlineSeconds: 300`: 5분(300초) 안에 실행되지 않으면 강제 종료
