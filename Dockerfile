FROM python:3.12-slim

WORKDIR /api

COPY pyproject.toml poetry.lock /api/

RUN pip install --no-cache-dir poetry python-dotenv

RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /api/

RUN poetry run flask db upgrade

ENV FLASK_ENV=production

EXPOSE 8080

RUN rm -f .env

CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:8080", "app.app:app"]