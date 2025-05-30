# SQDBI - Solo Queue Database Ingest

**This repository is currently archived as the owner works on [ATG (All the games)](github.com/Allan-Cao/ATG) as an maintained replacement!**

Models and scripts to store riot summary files for a database of players.

## Virtualenv

Please use a virtual environment to manage dependencies.

```bash
python -m virtualenv .venv
source .venv/bin/activate
```

To setup the project

```bash
python -m pip install -r requirements.txt
```


## Alembic Commands

```bash
alembic revision --autogenerate -m "changes"
alembic upgrade head
alembic downgrade base
```

## FastAPI

Run the FastAPI server with the following commands

```bash
cd api
fastapi dev main.py
```
