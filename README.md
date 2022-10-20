# Predict_Price_Laptop
참고 링크(notion 포트폴리오) : https://www.notion.so/ollpp/3311e5ddf4154003954d4a28e368768c

</br>
</br>

## 프로젝트 개요
온라인 쇼핑 진행 시 다양한 특성을 고려하여 가격을 예측하는데 많은 시간이 소요된다. 
이에, 네이버 쇼핑에 등록된 물건들의 특성과 가격을 수집하여 원하는 특성의 노트북 가격을 예측해주는 서비스를 구현하고자 프로젝트를 진행해보았다.

</br>
</br>

## 필요한 데이터셋 소개
- `naver_data.csv` : 네이버 쇼핑에서 크롤링한 특성, 가격 데이터

</br>
</br>

## 서비스 설명
1. 디렉토리 구조
  - Predict_price
    - mk_model
      - `modeling_.ipynb` : 크롤링한 데이터를 바탕으로 EDA 및 modeling 진행
    - naver_shop : 서비스 구현을 위한 Flask 모델
    - chromedriver : 크롤링을 위한 필요 파일
    - `crawling.py` : 네이버 쇼핑에서 크롤링을 진행하는 파일
    - Procfile : Heroku 배포를 위한 파일
    - requirements.txt : 필요 설치 파일 목록
    
</br>

2. 서비스 구현 방식
    1. 웹 서비스
        - 원하는 레포지토리에 다운을 받은 후, 다음 코드를 실행시켜 필요한 패키지들을 다운받는다.
          - `pip freeze > requirements.txt`
        - `flask run` 을 통해 웹 서비스를 실행시킨다.
    2. 크롤링 서비스
        - `crawling.py` : 추가 크롤링을 원할 때 사용
    3. 모델링
        - `modeling_.ipynb` : 크롤링한 데이터 특성을 바탕으로 ML 학습 및 예측에 사용하는 모델을 생성하는 파일


</br>

3. 전체적인 서비스 흐름
    1. `crawling.py` 파일을 통해 네이버 쇼핑 데이터를 크롤링하고, PostgreSQL에 관계형 DB로 적재한다.
    2. `modeling_.ipynb` 파일을 통해 크롤링한 데이터를 EDA 및 전처리를 진행하고, 모델학습을 통해 생성된 가격 예측 모델을 pickle 라이브러리를 통해 추출한다.
    3. 추출한 pickle 모델을 Flask app에 import 시키고, 사용자로부터 받은 input feature들을 기반으로 가격을 예측한다.
    4. docker의 metabase container를 사용해 대시보드를 작성해 본다.
    5. Heroku에 해당 서비스를 배포한다.
    
        </br></br>

## 결론
1. 데이터의 양을 충분히 크롤링한다면 모델의 성능을 높일 수 있다.
2. ML 모델의 hyper parameter를 조율하여 모델의 성능을 높여야 할 필요가 있다.
