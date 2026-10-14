FROM python:3.11-slim
WORKDIR /usr/srv/app
RUN pip install --no-cache-dir fastapi uvicorn
COPY pinpong.py .
CMD ["sh", "-c", "uvicorn pinpong:app --host 0.0.0.0 --port $PORT"]
