FROM python:3.11-slim

WORKDIR /app

# Устанавливаем зависимости системы (по минимуму)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Копируем requirements.txt из корня проекта
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем только папку app/ внутрь контейнера
COPY ./app .

# Рабочая директория — внутри app/
WORKDIR /app


CMD ["python", "main.py"]
