# Data

소소한 데이터 프로젝트를 모아 정리하였다.
혹시 파일 오류 (Something went wrong. Reload?) 가 발생할 경우, 새로고침 하거나 직접 다운 받으면 열린다.

### telegraph -> influxDB -> Grafana (24.07)
타 프로젝트 진행과정에서 MQTT 를 이용하여 시계열 로그데이터를 수집하는 프로젝트가 있었다. 
이에 착안하여 내가 남길 수 있는 CPU 등 노트북의 로그를 telegraph 라이브러리를 사용하여 TSDB인 influxdb에 적재,
influxdb에서 grafana로 간단한 시각화를 진행하였다.


- - -

### Movie_Data_Analysis.ipynb / collect_tmdb_api.ipynb
영화추천 프로젝트용으로 수집 및 mongodb에 적재한 데이터를 이용하여 통계 시각화 및 손익 분석 수행.

- - -

### kbo_player
kbo 데이터의 연봉정보 및 기록을 수집하여 연봉과 성적의 상관관계를 비교 분석.

- - -

### starbucks
스타벅스 매장 추이 분석 및 시각화.

- - -

### convenience_store
전국 편의점 데이터를 바탕으로 점유율 분석.


### crawling 연습
웹상의 데이터 extract 연습


### study
데이터 분석의 기본이 되는 공부관련 자료입니다
- Python, Pandas, Numpy, Statsmodels를 사용해 시계열 데이터를 예측하고 분석 (udemy)
- 컬럼베이스인 duckdb의 장단점 및 왜 사용하는지에 대해 test
- pygwalker를 사용한 시각화
- streamlit을 이용한 web, pygwalker를 사용한 시각화 => 대시보드 web 구축
