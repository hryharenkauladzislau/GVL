# Лабораторная работа №7 — Docker

## Задания:

1. **Установка Docker**  
   ```bash
   docker --version
   ```

2. **Работа с образами**  
   ```bash
   docker pull nginx
   docker run -d -p 8080:80 nginx
   ```

3. **Создание пользовательского образа**  
   - Создан `Dockerfile` и `app.py` с приложением Flask.

4. **Работа с томами (Volumes)**  
   - Том подключён в docker-compose как `webdata` и `pgdata`.

5. **Сеть в Docker**  
   - Описана в `docker-compose.yml` через `webnet`.

6. **Docker Compose**  
   ```bash
   docker-compose up --build
   ```

7. **Очистка ресурсов**  
   ```bash
   docker-compose down -v
   docker system prune -a
   ```