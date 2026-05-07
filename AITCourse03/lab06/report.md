# Отчет по лабораторной работе "Docker-Compose First Look"

## Выбор языка и архитектура проекта
Для создания "Ping Pong" веб-приложения я выбрал язык программирования Python (FastAPI).

Я создал папку на сервере `app`, у которой была следующая архитектура:

app/
- app.py
- Dockerfile
- docker-compose.yaml
- requirements.txt

## Содержимое моих файлов следующее:

app.py
```python
from fastapi import FastAPI
import os

app = FastAPI()

MESSAGE = os.getenv('PONG_MESSAGE', 'pong')

@app.get('/ping')
def ping():
    return MESSAGE
```

Dockerfile
```dockerfile
FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
```

docker-compose.yaml
```docker-compose
version: '3.8'

services:
  fastapi-pong-1:
    build: .
    ports:
      - "5001:5000"
    environment:
      - PONG_MESSAGE=pong from instance 1
    restart: unless-stopped

  fastapi-pong-2:
    build: .
    ports:
      - "5002:5000"
    environment:
      - PONG_MESSAGE=pong from instance 2
    restart: unless-stopped
```

requirements.txt
```
fastapi==0.104.1
uvicorn==0.23.2
```

## Запуск приложения

После применив команду `docker compose up --build` собраз и запустил контейнер.

## Проверка работы приложения

Далее в новом терминале сделал два запроса:
```
curl http://ip_address_server:5001/ping
curl http://ip_address_server:5002/ping
```

И получил два ответа: 
```
pong from instance 1

pong from instance 2
```

## Вывод

Что подтверждает работу приложения и выполнения задания по требованиям.
