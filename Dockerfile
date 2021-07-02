FROM docker.io/library/python:slim

WORKDIR /app
COPY . .

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y netcat \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --ansi --no-dev

EXPOSE 5000/tcp

CMD bash start_server.sh
