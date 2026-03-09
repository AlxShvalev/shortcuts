# ShortCuts
API для хранения сокращенных ссылок. POST-запрос принимает оригинальную ссылку
и возвращает индекс сокращенной ссылки. GET-запрос по индексу перенаправляет на оригинальную ссылку.
Также есть возможность получить статистику по сокращенной ссылке, включая количество переходов.

## API:
```commandline
/shorten/ - POST - Сокращение ссылки
{
    "original": "https://www.example.com/very/long/url"
}

/{shorten_id}/ - GET - Редирект на оригинальную ссылку

/stats/{shorten_id}/ - GET - Получение статистики по сокращенной ссылке
```

## Запуск проекта:
1. Клонируйте репозиторий:
```commandline
git clone
```
2. Перейдите в директорию проекта:
```commandline
cd shortcuts
```
3. Скопируйте файл `.env.example` в `.env` и заполните необходимые переменные окружения.:
```commandline
cp .env.example .env
```
4. Запустите проект с помощью Docker Compose:
```commandline
docker compose up -d --build
```

## Зупуск тестов:
1. Установка зависимостей
```commandline
poetry install --no-root
```
2. Запуск тестов
```commandline
poetry run pytest
```

## Документация
Документация API доступна по адресу: `http://service_host:service_port/docs`

## Технологии:
- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- Pytest
- Poetry
