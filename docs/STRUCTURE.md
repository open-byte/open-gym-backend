# Structure of Project

[See Reference structure](https://github.com/zhanymkanov/fastapi-best-practices)

The project follows the structure of a FastAPI project. The main components are:
- `src`: Contains the source code of the project
- `src/{module}/tests`: Contains the tests of the project
- `src/core`: Contains the core of the project
    - schemas: Contains the schemas of the project with Pydantic
    - `exceptions`: Contains the exceptions of the project
        - Models are defined here and are used to validate the input and output of the API(In General)
    - `constants.py`: Contains the constants of the project
    - `dependencies.py`: Contains the dependencies of the project
    - `utils.py`: Contains the utilities of the project
    - `tags.py`: Contains the tags of the project (OpenAPI)
- `src/config`: Contains the configuration of the project
- `tests`: Contains the tests of the project

A module is a part of the project that is responsible for a specific functionality. For example, the module `users` is
responsible for the users of the project. The module `auth` is responsible for the authentication of the project.


Every module has the following structure:
- `{module}`
    - `__init__.py`: The module is a package
    - `models`: Contains the models of the module
    - `services`: Contains the services of the module
    - `routers`: Contains the routers of the module
    - `constants.py`: Contains the constants of the module
    - `schemas.py`: Contains the schemas of the module
    - `dependencies.py`: Contains the dependencies of the module
