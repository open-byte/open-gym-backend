# Open Gym Backend
Project to manage the backend of the Open Gym application

## Structure

See [Structure](./docs/STRUCTURE.md)

## Technologies
- Python 3.12+ ✨
- [Uvicorn](https://www.uvicorn.org/) Lightning-fast ASGI server implementation, using uvloop and httptools 🦄
- [FastAPI](https://fastapi.tiangolo.com/) Web Framework for building APIs 🚀
- [SQLModel](https://sqlmodel.tiangolo.com/) SQLModel is a library for interacting with SQL databases from Python code 🗄️
- [Pydantic](https://pydantic-docs.helpmanual.io/) Data validation and settings management using python type annotations ✅
- [Poetry](https://python-poetry.org/) Python dependency management and packaging made easy 📦
- [Alembic](https://alembic.sqlalchemy.org/) A database migrations tool for SQLAlchemy 🐍
- [PostgreSQL](https://www.postgresql.org/) Open Source Relational Database 🐘
- [Docker](https://www.docker.com/) Containerization platform 🐳
- [Docker Compose](https://docs.docker.com/compose/) Tool for defining and running multi-container Docker applications 🛠️


## Format and Linting
- [Ruff](https://docs.astral.sh/ruff/) is a code formatter and linter for Python 🐶
- [Pre-commit](https://pre-commit.com/) A framework for managing and maintaining multi-language pre-commit hooks 🎣
- [mypy](https://mypy.readthedocs.io/en/stable/) Static type checker for Python 🏗️


## Code Style
- Comments: [Google Style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- [Ruff](https://docs.astral.sh/ruff/) is a code formatter and linter for Python 🐶
- All code has to be formatted and linted before committing using pre-commit hooks

For checking static type checking run the following command
```bash
mypy src/**/*.py

```

## Project setup

### Prerequisites
  - Python 3.12+
  - Docker
  - Docker Compose
  - Poetry
  - Pre-commit

- We are using pre-commit to enforce code style and formatting
```bash
## Install pre-commit
pip install pre-commit
## Install the pre-commit hooks
pre-commit install
```
### Local development
- Clone the repository
- Install poetry
```bash
pip install poetry
```

- Create a virtual environment
```bash
poetry env use python3.x # where x is the version of python you want to use (3.12+)
source .venv/bin/activate # activate the virtual environment
```
 or
```bash
python3.x -m venv .venv # where x is the version of python you want to use (3.12+)
source .venv/bin/activate # activate the virtual environment
```
- Install the dependencies
```bash
poetry install
```


- Run the server (before running the server, you need to have the `.env` file with the configuration of the database)
```bash
uvicorn src.main:app --reload --port 8000
```

### Local development with Docker
- Clone the repository
- Use docker-compose to build and run the server
```bash
docker-compose up --build
```
### API Documentation
- The API documentation is available at `http://localhost:8000/docs`


## Apply migrations

See [Migrations](./docs/MIGRATIONS.md)
