# 학부생 연구프로그램(URP)

한국과학창의재단에서 실시한 학부생 연구프로그램(URP)에 선정되어 진행한 프로젝트.

코로나 바이러스와 같은 위급한 상황에서 바이러스의 확산과 N차 감염을 최소화 하기 위하여 바이러스 검사를 빠르게 진행하고 다수의 인원과의 접촉을 피하기위한 분산 시스템 및 경로 안내 시스템 구축

병원과의 거리, 대기 시간 등의 여러 상황을 고려하여 최적화된 경로를 알려줄 수 있도록 제작

[dbpia](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11037810)

# 팀 구성 및 역활
* 팀 구성: 3명
* 역할: 개발 및 팀장
* 본인이 맡은 역할: 병원 데이터 전처리, TMAP API 사용, 이동 경로 수식 최적화 및 개발
* 연구 성과: 2022년도 한국컴퓨터정보학회 동계학술대회 우수 논문상 수상.

# 개발환경
Pycharm, visual studio code

# 개발언어
Python, JavaScript

# 사용API
카카오 맵 API, 티맵 API

# 그래프 구축
![image](https://user-images.githubusercontent.com/40080826/230781447-0d78cf91-9066-418e-bf83-1179ec80f9c2.png)

실제 병원 위치를 빠르게 찾기 위하여 K-d 트리를 활용해 그래프 구축

# 이동 경로 cost 설정
![image](https://user-images.githubusercontent.com/40080826/230781673-f0c205fa-f015-4363-a15c-92f2749b29e1.png)
* m: 분배인원
* P: 병원의 환자 수
* t_treat: 환자 한 명당 검사 시간
* t_trav: 현재 위치에서 병원까지 걸리는 시간
결과적으로 대기환자가 적고 거리가 가깝고 병원 수용 가능 인원이 많을 수록 cost를 낮게 설정함.

# Cost 계산 및 분배
![image](https://github.com/ShinYoungChan/urp/assets/40080826/1a4accab-4f90-44a6-8c48-8dbf97a907d6)
* Cost가 낮은 병원부터 환자를 보내면서 Cost 갱신

# 그래프 애니메이션
![미디어01](https://github.com/ShinYoungChan/urp/assets/40080826/2c8a2568-9bdc-47e8-b8c7-d5eb51e2f9bd)


# 이동경로 확인 및 분배 인원 확인
![image](https://github.com/ShinYoungChan/urp/assets/40080826/c42e2860-1952-47c7-b9f7-757f8815ffd4)
* 보라색 위치에서 검사할 수 있는 병원 확인 가능
* 검사 가능 병원의 cost 및 이동인원 파악
* Scale: 병원 규모(검사를 한번에 할 수 있는 수), Agents: 병원으로 이동한 환자 수, Cost: 분배 후 계산된 Cost, start: 시작 시간, end: 끝나는 시간

# 경로 최적화
![image](https://user-images.githubusercontent.com/40080826/230781863-1c3e1a17-79a5-47ae-bfe6-d9ee84630ab2.png)

여러 위치에서 경로를 탐색할 경우 각 경로에 대한 cost에 영향이 가지 않도록 최적화함.
겹치는 경로를 최적화하여 단위 시간당 더 많은 환자를 검사할 수 있도록함.

# 실행 방법
* 출발지역에 맞게 주석 수정
> main.py에서 시작 위치 수정 (줄 13~)  
> main.py에서 환자 생성 수정 (줄 101~)  
> DomainSystem.py에서 cost파일 위치 수정 (줄8~) _OffTime은 퇴근 시간에 측정했던 cost값 저장한 파일입니다.

* 파이썬 실행 후 http://127.0.0.1:8080/ 접속
* 화면을 클릭하여 시뮬레이션을 시작하고 다시 클릭하게 되면 다음과 같이 장면이 바뀜
   - 한 위치에서 발생한 환자들의 이동 현황
   - 발생한 모든 환자들의 이동 현황
