# Базовый образ с Python
FROM python:3.11-slim

# Установка зависимостей
RUN pip install flask

# Копирование приложения
COPY app /app
WORKDIR /app

# Указание порта и команды запуска
EXPOSE 5000
CMD ["python", "app.py"]