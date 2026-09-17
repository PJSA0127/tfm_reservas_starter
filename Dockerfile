FROM python:3.14-slim@sha256:cad9a2c871761c413caa6fdd6441c783451e740a48aaeba60ae62a8b53525ef6

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.lock ./

RUN pip install --no-cache-dir -r requirements.lock

COPY . .

EXPOSE 5000

CMD ["flask", "--app", "app:create_app", "run", "--host=0.0.0.0", "--port=5000"]
