FROM python:3.13-slim AS builder

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir "poetry>=2.0" \
    && poetry self add poetry-plugin-export \
    && poetry export -f requirements.txt --output requirements.txt \
    --without-hashes --without-urls


FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    python3-dev \
 && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 app

WORKDIR /app

COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ../alembic.ini .
COPY ../src ./src

ENV PYTHONPATH=/app/src

RUN chown -R app:app /app

USER app

CMD ["sh", "-c", "alembic upgrade head && uvicorn src.main:app --host 0.0.0.0 --port 8000"]