FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install --no-cache-dir poetry

RUN poetry install --no-dev --no-interaction --no-ansi --no-root

COPY . /app/

ENV FLASK_ENV=production

EXPOSE 5000

CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:5000", "app.app:app"]

