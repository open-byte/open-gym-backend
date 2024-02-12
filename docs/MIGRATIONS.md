## Database and Migrations
We use PostgreSQL 16 as our database, at the moment this database is into a docker container, so you need to have docker
installed in your machine to run the database. (Just for development)

Also, we use the `alembic` library to manage the database migrations, this library is already installed in the
project(with poetry), so you don't need to install it and **we use the `SQLModel` library as the ORM to manage the
database (SQLModel is a library that is built on top of SQLAlchemy).**
### Step to run migrations:
Before running the migrations, you need to have the `.env` file with the configuration of the database.
We use this configuration for development.
```dotenv
DATABASE_URL=postgresql+psycopg://postgres:postgres@database:5432/open_gym_backend
SECRET_KEY=secret
VERSION=0.0.0
```

You can create a `.env` file into the `src` directory with the above configuration.

#### Steps to run the migrations:
1. Build the docker container with the database:
```bash
docker-compose up --build
```

2. Run the migrations:
```bash
docker-compose run backend alembic upgrade head ## This will run all the migrations
```
### Step to create a new migration:
1. Create a model or modify an existing model in the `{module}/models/{your_model}.py` directory.
1.1 PLEASE USE BaseSQLModel to create your models, this will help to manage the database and the migrations.
2. Add your model to database in the `{module}/models/__init__.py` file.
3. Ensure that your models are import in the `database/models.py` file.
    ```python
    from module.your_models import *
    ```

4. Run the command to generate the migration:
    Please replace `{Your message here}` with a message that describes the changes you made.
    You can use the conventional-commit message format to describe your changes.
    ```bash
    docker-compose run backend alembic revision --autogenerate -m "{feature|fix|refactor|style|test|docs|chore}: {Your message here}"
    ```
5. Run the migrations:
    ```bash
    docker-compose run backend alembic upgrade head
    ```
