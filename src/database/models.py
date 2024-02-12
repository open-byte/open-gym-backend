"""
Import all the models here to ensure they are all included in the migration process
Alembic will use the metadata from the models to generate the migration files.

Steps to create a migration:

- Write the model into the {modulel}/models.py file
- import the model into the database/models.py file
- run the command `alembic revision --autogenerate -m "{migration message}"`
- apply the migration with `alembic upgrade head`
- commit the changes to the repository
"""
## User module
from user.models import User  # noqa F403
