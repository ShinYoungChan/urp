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

# 경로 최적화
![image](https://user-images.githubusercontent.com/40080826/230781863-1c3e1a17-79a5-47ae-bfe6-d9ee84630ab2.png)

여러 위치에서 경로를 탐색할 경우 각 경로에 대한 cost에 영향이 가지 않도록 최적화함.
겹치는 경로를 최적화하여 단위 시간당 더 많은 환자를 검사할 수 있도록함.
