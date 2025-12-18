# 1. Базовый образ
FROM python:3.11-slim

# 2. Рабочая директория
WORKDIR /app

# 3. Установка зависимостей системы (curl для HEALTHCHECK)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 4. Копируем зависимости и устанавливаем
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем исходники
COPY . .

# 6. Открываем порт
EXPOSE 8000

# 7. Команда запуска (uvicorn)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# 8. Healthcheck (проверка эндпоинта)
HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:8000/healthcheck || exit 1
curl http://localhost:8000/healthcheck
