# Assignment3
원티드 프리 온보딩 2주차 기업형 과제(원티드랩)

## 설명

본 프로젝트는 원티드x위코드 백엔드 프리온보딩  [원티드랩]에서 출제한 과제를 기반으로 제작 되었습니다.

[과제 소개](https://www.notion.so/wecode/0517378f554a489db507524a91d64dc8)

## 요구사항 분석
**REST API 기능**

- 회사명 자동완성
- 회사 이름으로 회사 검색
- 새로운 회사 추가
- 데이터 셋 [wanted_temp_data.csv](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/81f13ae2-fabc-4fad-a754-9b2d684f41a8/wanted_temp_data.csv)
- 제공되는 test case를 통과할 수 있도록 개발해야 합니다. [test_app.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d2517b3-b80b-4a1b-82c4-9bc6f2a0d5ae/test_app.py)
## 사용 스택
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white" />&nbsp; <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white" />&nbsp; <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white" /> &nbsp; <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=Redis&logoColor=white" /> &nbsp; <img src="https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=Postman&logoColor=white" />  &nbsp; <img src="https://img.shields.io/badge/AWS%20EC2-232F3E?style=flat-square&logo=Amazon%20AWS&logoColor=white" />

## DB 스키마
![원티드 랩 Assignment3 (2)](https://user-images.githubusercontent.com/67785334/140938418-f31e37d2-cd69-4f58-81ff-cd05ecb8a7cc.png)


## 문제정의 및 시퀀스 다이어그램


| 문제 정의 | 
| ------ | 
| [회사 이름으로 회사 검색 & 회사명 자동완성](https://github.com/Wanted-Free-Pre-Onboarding-Course-10/Assignment3/wiki/%EB%AC%B8%EC%A0%9C-%EC%A0%95%EC%9D%98(%ED%9A%8C%EC%82%AC%EB%AA%85-%EC%9E%90%EB%8F%99%EC%99%84%EC%84%B1,-%ED%9A%8C%EC%82%AC-%EA%B2%80%EC%83%89)) |
| [새로운 회사 추가](https://github.com/Wanted-Free-Pre-Onboarding-Course-10/Assignment3/wiki/%EB%AC%B8%EC%A0%9C%EC%A0%95%EC%9D%98(%EC%83%88%EB%A1%9C%EC%9A%B4-%ED%9A%8C%EC%82%AC-%EC%B6%94%EA%B0%80)) |  


## 과제 구현사항


| 구현사항  | 구현 여부                                          |
| ------ | ----------------------------------------------- |
| 회사명 자동완성 |  OK| 
| 회사 이름으로 회사 검색 | OK | 
| 새로운 회사 추가 | OK | 


## API
[API문서](https://documenter.getpostman.com/view/13568025/UVC5F87D)

## API 테스트
1. 우측 링크를 클릭해서 postman으로 들어갑니다.[링크](https://www.postman.com/martian-satellite-348039/workspace/10/overview) 
2. 정의된 flask가 올바른지 확인 합니다.(3.36.88.48:5000)

<img width="732" alt="스크린샷 2021-11-10 오전 5 35 01" src="https://user-images.githubusercontent.com/81801012/141000570-91c5ecda-b24c-46c4-8073-1fe9feae4535.png">


3. 이후, API 테스트를 시도해 주세요.

## 설치 및 실행 방법

### 프로젝트 설치

```bash
git clone https://github.com/Wanted-Free-Pre-Onboarding-Course-10/Assignment3.git
```

 ### 환경 구축
 
 ```bash
 #도커 환경 구축#
 docker-compose up
 ```

```bash
#윈도우#
python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt
```

```bash
#맥#
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

```shell
flask db init
flask db migrate
flask db upgrade
```

```shell
flask run
```


## 팀원

| 이름   | github                                          | 담당 역할                  | 회고록             |
| ------ | ----------------------------------------------- | -------------------------- |------------------|
| 박지율 | [earthkingman](https://github.com/earthkingman) | 자동 완성 API, 도커, 캐싱 전략 |      [회고록](https://velog.io/@earthkingman/%EC%9B%90%ED%8B%B0%EB%93%9C-%ED%94%84%EB%A6%AC%EC%98%A8%EB%B3%B4%EB%94%A9-2%EC%A3%BC%EC%B0%A8-%EC%9B%90%ED%8B%B0%EB%93%9C-%ED%9A%8C%EA%B3%A0%EB%A1%9D)          |
| 염재선 | [Yeom Jae Seon](https://github.com/YeomJaeSeon) | 자동 완성 API, 개발 환경 설정, DB 설계, 서버 배포 |   [회고록](https://yjs3819.tistory.com/68)                  |
| 김태희 | [김태희](https://github.com/godtaehee)            | 회사 추가 API, 테스팅, DB 설계     |        [회고록](https://medium.com/@godtaehee/week-2-wanted-%EA%B3%BC%EC%A0%9C%EB%A5%BC-%EB%A7%88%EC%B9%98%EA%B3%A0-41fa8998a4db)            |
| 박상엽 | [큰형](  https://github.com/lotus0204)            | 검색 API, 테스팅, 캐싱 전략           |     [회고록](https://velog.io/@lotus/Pre-Onboarding-%ED%9A%8C%EA%B3%A0Assignment-3)                   |

## 개발 일정

![](https://images.velog.io/images/earthkingman/post/82de5bb2-bddc-49f9-a5a5-675b8b172a2b/image.png)

## 사전 학습

새로운 기술을 사용하기 전에 서로 다른 주제를 가지고 동료 학습을 진행했습니다.


## 협업 방식

[잡초 협업하기](https://github.com/Wanted-Free-Pre-Onboarding-Course-10/Assignment2/wiki/%ED%98%91%EC%97%85-%EB%B0%A9%EC%8B%9D)

## 개발 과정

**1.회사명 자동완성 API**
[바로가기](https://github.com/Wanted-Free-Pre-Onboarding-Course-10/Assignment3/wiki/%ED%9A%8C%EC%82%AC%EC%9D%B4%EB%A6%84-%EC%9E%90%EB%8F%99%EC%99%84%EC%84%B1-%EA%B8%B0%EB%8A%A5)


**2. 회사 이름으로 회사 검색 API**
[바로가기](https://github.com/Wanted-Free-Pre-Onboarding-Course-10/Assignment3/wiki/%ED%9A%8C%EC%82%AC-%EC%9D%B4%EB%A6%84%EC%9C%BC%EB%A1%9C-%ED%9A%8C%EC%82%AC-%EA%B2%80%EC%83%89-%EA%B8%B0%EB%8A%A5)


**3. 새로운 회사 추가 API**
[바로가기](https://github.com/Wanted-Free-Pre-Onboarding-Course-10/Assignment3/wiki/%EC%83%88%EB%A1%9C%EC%9A%B4-%ED%9A%8C%EC%82%AC-%EC%B6%94%EA%B0%80-%EA%B8%B0%EB%8A%A5)

**4. 캐싱 전략**
[바로가기](https://github.com/Wanted-Free-Pre-Onboarding-Course-10/Assignment3/wiki/%EC%BA%90%EC%8B%B1%EC%A0%84%EB%9E%B5)

## 테스트 

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/44861205/140997102-281d4194-ded8-47aa-ad13-abcaea2d1d43.gif)

gif파일이 너무 커서 풀버전의 gif를 올리지 못하고 있습니다. 해당 gif풀버전은 [김태희](https://github.com/godtaehee)가 가지고 있습니다.

## 개발도중 고민들
- 테이블간의 관계, 다대다 vs 다대일의 고민(<a href="https://github.com/Wanted-Free-Pre-Onboarding-Course-10/Assignment3/wiki/%EB%8B%A4%EB%8C%80%EB%8B%A4-vs-%EC%9D%BC%EB%8C%80%EB%8B%A4">위키 링크</a>)
- 도커의 도입 (<a href="https://github.com/Wanted-Free-Pre-Onboarding-Course-10/Assignment3/wiki/%EB%8F%84%EC%BB%A4%EC%9D%98-%EB%8F%84%EC%9E%85">위키 링크</a>)
- 레디스의 도입 (<a href="https://github.com/Wanted-Free-Pre-Onboarding-Course-10/Assignment3/wiki/%EB%A0%88%EB%94%94%EC%8A%A4%EC%9D%98-%EB%8F%84%EC%9E%85">위키 링크</a>)

