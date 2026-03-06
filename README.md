# ShortCuts
API для хранения сокращенных ссылок.

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

## Технологии:
- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- Pytest
