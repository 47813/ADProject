

# Webserver Fullstack Project

이 프로젝트는 Django를 백엔드로, React를 프론트엔드로 구성한 전체 웹 애플리케이션입니다. 책 정보, 사용자 요청, 로그인 기능 등을 포함하고 있습니다.

---

## 🔧 설치 및 실행 방법

### 1. 백엔드 (Django)

#### ✅ 가상환경 생성 및 패키지 설치

```bash
cd Webserver
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```


#### ✅ PostgreSQL 설정

macOS

```bash
brew install postgresql
brew services start postgresql
createdb postgresql
```

Windows
```
	1.	PostgreSQL 공식 사이트에서 설치
	2.	pgAdmin 또는 CLI에서 postgresql 이름의 데이터베이스 생성
```


#### ✅ 마이그레이션 및 더미 데이터 삽입

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata dummy_data.json
```


#### ✅ 개발 서버 실행

```bash
python manage.py runserver
```

> 기본 포트: `http://localhost:8000/`

---

### 2. 프론트엔드 (React)

#### ✅ 패키지 설치 및 실행

```bash
cd frontend
npm install
npm start
```

> 기본 포트: `http://localhost:3000/`

---

## 📦 주요 기능

- 📚 도서 목록 및 검색 (저자, 키워드, 정렬)
- 🔐 로그인 및 인증 (Django superuser 기반)
- 📝 사용자 요청 정보 출력 (Request info viewer)
- 📁 파일 업로드 기능
- 💬 Hello API 테스트 및 메시지 POST 전송

---

## 🔗 주요 경로 (프론트엔드)

- `/books` - 전체 도서 목록
- `/books/author` - 저자 검색
- `/books/keyword` - 키워드 검색
- `/login` - 로그인 페이지
- `/request_info` - 사용자 요청 정보

---

## ✅ 기타

- `.gitignore` 파일을 통해 venv, node_modules, DB 파일 등은 버전관리에서 제외됨
- 백엔드와 프론트엔드는 각각 독립적으로 실행되며, CORS 설정이 적용되어 연결됨

---