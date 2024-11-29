# WISE (Wound Identification System) API

## Setup Project

1. Create virtual environtment

```bash
python -m venv virtualenv
# or
python3 -m venv virtualenv
```

2. Activate the virtual environtment

```bash
# linux and mac
source virtualenv/bin/activate

# windows cmd
.\venv\Scripts\activate.bat
```

3. Create and fill the `.env` file

```bash
# linux and mac
cp .env.example .env

# or you can just copy and paste it.
```

Then fill the file with your environtment variables.

4. Install dependencies

```bash
# first you need poetry
pip install poetry

# then install all dependency with poetry
poetry install
```

5. Run the project

```bash
flask run

# or use --reload to autoreload
flask run --reload
```

6. Doing migrations

```bash
flask db upgrade
```

7. How to run the test

```bash
pytest
```
