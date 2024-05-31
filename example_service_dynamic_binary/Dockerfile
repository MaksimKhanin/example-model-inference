# Указываем базовый образ
FROM python:3.11.9-alpine3.19

# Копируем requirements.txt в контейнер
COPY ./requirements.txt /app/requirements.txt

RUN apk add --update --no-cache g++


# Устанавливаем зависимости
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./main.py /app/main.py

# Указываем рабочую директорию
WORKDIR /app

# Запускаем FastAPI сервис
CMD [ "python", "./main.py"]