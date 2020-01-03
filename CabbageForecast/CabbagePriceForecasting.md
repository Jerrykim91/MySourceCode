# 배추 가격 예측

  [주소]https://github.com/ndb796/Vegita



### 1. 데이터 수집

- 크롤링의 과정이 필요할수도 있음 

- 기상청 => 기상자료 개발 포탈 => 다중지점 통계 

  -   https://data.kma.go.kr/climate/StatisticsDivision/selectStatisticsDivision.do?pgmNo=158

- 농산물 유통정보 사이트 => 배추 가격정보 받아오기

  -   https://www.kamis.or.kr/customer/price/retail/period.do?action=daily

  

### 2. 데이터 전처리 및 정제

- 수집한 데이터는 AiSw가 인식하기 쉬운형태로 정제  => 주말에는 배추가격 x 몇몇 일자 NG데이터 

- 데이터를 전처리 => 정제를 해야한다.

- 날짜에 따라 평균기온, 최저기온, 최대기온, 강수량 , 평균가격 

- 주의 ) 모형에 변수가 많을수록 데이터를 과적합 (overfitting)시킬위험은 더욱 커지게 된다.  => 적당한 변수가 좋다

  - 데이터마이닝의 경우에는 요구사항이 비교적 상세하지 않으므로 경험에 의한 법칙(rulesof thumb)에 의존해 데이터마이닝 작업을 수행 한다.

  

### 3. 모델 구현

- 사용하는 패키지 (텐서, 넘파이, 판다스)

- 모델을 초기화 

- 데이터 로드 

- 변수 => 행렬형태로 

-  **다변인 선형회귀 

  - 모델에 영향을 미치는 변인이 여러개일때 사용하는 모델 

  - 평균온도 , 최저,최대온도,강수량등 ... => 변인이 가격에 영향을 미친다고 감안 -> 가중치를 고려했을때 

  -   H(x1, x2, x3, x4) = x1w1 + x2w2 + x3w3 + x4w4

    => **H(X) = XW**

  안정적인 학습을 위해서는 학습의 보폭을 잘 선택해야한다.

-----

<나동빈>

네이버 주소 - 머신러닝 과정 설명 (https://blog.naver.com/ndb796/221277713538)

티스토리 - ai 배추 코드 설명  (https://ndb796.tistory.com/124?category=1013932)

<무료 플라스크 템플릿 소스 >

(  https://mdbootstrap.com/freebies/ )