FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir ".[dev]"

COPY . .

EXPOSE 5000

CMD ["flask", "--app", "app:create_app", "run", "--host=0.0.0.0", "--port=5000"]
