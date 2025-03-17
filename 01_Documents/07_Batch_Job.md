# Batch job
Batch Job은 일정 시간 동안 실행된 후 종료되는 작업을 의미합니다. 
Kubernetes에서 **일반적인 서비스(Pod)**는 계속 실행되는 형태지만, Batch Job은 특정 작업을 수행하고 종료되는 특징이 있습니다.

예를 들어 아래 같은 경우에 유용할 수 있음:
- 데이터 ETL
- 이메일 발송 
- 정기적 백업 작업



## 표현식
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: simple-job
spec:
  completions: 5   # 총 5개의 작업을 수행
  parallelism: 2   # 동시에 2개씩 실행
  template:
    spec:
      restartPolicy: Never  # 필수값
      containers:
      - name: hello
        image: busybox
        command: ["echo", "Hello Kubernetes!"]
      
```