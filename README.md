# railcar_trend 🚂🛤️🛤️
## 철도 관련 입력 키워드에 대한 트랜드 분석 모델 구현

### 1. 최근 뉴스 데이터
네이버 뉴스 API를 활용하여 뉴스를 불러온 다음 대표적인 LLM 모델(Llama 3.1)을 활용하여 Keyword를 추출한다.

### 2. 데이터베이스 연동
Mongo DB를 활용하여 추출한 Keyword를 해당 날짜와 함께 저장을한다
- 만약 이미 해당날짜에 존재하는 keyword가 있다면, 횟수(num) +1 을 해준다
- 데이터베이스와 연동을 하는 이유는 추가적으로 다시 LLM 모델과 API를 사용하여 데이터를 불러오면 안전하지도 않고 많은 시간 비용이 들기 때문에
- 
### 3. Top 10 & Wordcloud
언급된 keyword 중 가장많이 언급된 keyword와 쉽게 user가 비교해 볼 수 있게 준비
- i. Top - k 개를 그래프를 활용하여 시각적 자료 준비
- ii. WordCloud를 사용하여 많이 언급된 keyword는 크게, 적게 언급된 keyword는 작게 표현

### 4. Co-occurrence Network (기간 설정 가능)
- i. 한 기사 내에서 같이 언급된 키워드를 2개씩 묶어준 database 생성 (중복되면 num += 1)
- ii. num (같이 언급된 횟수) 를 가중치를 사용 => 선이 굵어진다.
- iii. 언급이 많이 될 수록 노드의 사이즈도 커진다.

### 5. 키워드 언급 추이 변화 (여러개씩 가능)
- i. 사용자가 원하는 개수의 keyword 입력
- ii. 해당 키워드의 날짜별 언급추이를 그래프를 통해서 확인 가능
- iii. 여러 개를 한번에 확인할 수 있어 비교도 가능

### 6. Llamma fine tuning
- i. 기존에 pre train 되어 있는 LLM 모델을 가져와서 input-response 형식의 데이터 fine tuning
- ii. prompt를 통해 사용자의 질문을 받으면 fine tuning 되어있는 모델을 사용하여 답변하는 형식
