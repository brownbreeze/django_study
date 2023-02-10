# 장고 공부
> 인프런 강좌에서 시작
## 도커 환경
```
# dokcerfile 가져가기 
docker build -t centos:1.0 .
docker run -itd -p 0.0.0.0:{로컬사용포트}:8000/tcp -v {로컬PATH}:/home/ --name {container이름} centos:1.0 /bin/bash
```

## 설치
```
./install.sh
vi ~/.bashrc
    # 파일 끝에 아래내용 추가 작성
    alias python='/usr/local/bin/python3.7
    export LC_ALL='ko_KR.UTF-8'
    export LANG='ko_KR.UTF-8'
    #
source ~/.bashrc
```
```
cd /home
# git clone 해온 후 기동하기 
```
