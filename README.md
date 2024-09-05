# FastAPI Backend API
---
FastAPI Backend API Sample code

---
## 샘플 코드 특징
- db crud 처리 및 transaction 처리 샘플 코드
- [read / write] db 를 구분하여 crud 처리
- 비동기 session 을 생성하여 비동기 db 처리
- dependency injection 을 활용하여 공통 (전처리, 후처리) 작업 실행
    - 전처리 : api_token 체크
    - 후처리 : 사용자 사용 로그 저장 (백그라운드작업처리)
- pycryptodome 모듈을 사용하여 패스워드 암복호화 처리

---
## Install
1. install python 3.10.X higher
2. install python library
---
```bash
pip install -r app/config/requirements.txt
```

---
## Run
```bash
uvicorn app.main:app --reload
```