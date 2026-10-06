# 1. 경량화된 파이썬 3.9 이미지 사용
FROM python:3.9-slim

# 2. 컨테이너 내부 작업 디렉터리 설정
WORKDIR /app

# 3. 라이브러리 목록 복사 및 설치 (레이어 캐싱 최적화)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 앱 소스 코드 복사
COPY app.py .

# 5. 컨테이너 가동 시 실행할 메인 명령
CMD ["python", "app.py"]
