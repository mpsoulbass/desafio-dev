FROM docker.io/library/python:slim

WORKDIR /app
COPY ./pyproject.toml pyproject.toml

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y netcat \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --ansi

EXPOSE 8000/tcp
CMD python manage.py runserver 0.0.0.0:8000

#CMD python manage.py migrate && \
#    gunicorn --bind 0.0.0.0:3333 sales.wsgi:application \
#    --workers 2 --preload --log-file - --log-level=debug --error-logfile -