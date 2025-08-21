FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Daniel-Dief/sql-gen-webhook.git .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python", "-m", "app.main"]