from enum import StrEnum
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvironmentStages(StrEnum):
    """
    This class contains all possible application environment stages.
    """

    DEVELOPMENT = 'development'
    STAGING = 'staging'
    PRODUCTION = 'production'


class FastAPIConfig(BaseSettings):
    """
    This class contains all possible FastAPI configurations.
    - title: Application title
    - description: Application description
    - version: Application version
    - debug: Application debug mode
    - docs_url: Application docs URL
    - redoc_url: Application redoc URL
    - openapi_url: Application openapi URL
    """

    title: Optional[str] = 'Open Gym Backend API'
    description: Optional[str] = 'Open Gym Backend API Documentation.'
    version: Optional[str] = '0.0.0'
    debug: Optional[bool] = False
    docs_url: Optional[str] = '/docs'
    redoc_url: Optional[str] = '/redoc'
    openapi_url: Optional[str] = '/openapi.json'
    servers: Optional[list[dict[str, str]]] = [
        {'url': 'http://localhost:8000', 'description': 'Local server'},
        {'url': 'https://dev.backend.open-gym.com', 'description': 'Development server'},
        {'url': 'https://backend.open-gym.com', 'description': 'Production server'},
    ]


class AppBaseSettings(BaseSettings):
    """
    This is a base settings class for all application settings.
    - environment: Application environment
    - database_url: Database URL
    - secret_key: Secret key for JWT token
    - version: Application version
    """

    api_config: FastAPIConfig = FastAPIConfig()
    environment: EnvironmentStages = Field(description='Application environment')
    database_url: str = Field(description='Database URL', examples=['sqlite:///./db.sqlite3'])
    secret_key: str = Field(description='Secret key for JWT token', examples=['secret'])
    version: str = Field(description='Application version', examples=['1.0.0'])

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )


"""
Define all application settings classes.
- DevelopmentSettings: Development settings class configure with .env.dev file.
- StagingSettings: Staging settings class configure with .env.staging file.
- ProductionSettings: Production settings class configure with aws secrets manager.
"""


class DevelopmentSettings(AppBaseSettings):
    """
    This is a development settings class.
    """

    environment: EnvironmentStages = EnvironmentStages.DEVELOPMENT
    api_config: FastAPIConfig = FastAPIConfig(debug=True)


class StagingSettings(AppBaseSettings):
    """
    This is a staging settings class.
    """

    environment: EnvironmentStages = EnvironmentStages.STAGING
    api_config: FastAPIConfig = FastAPIConfig(debug=True)


class ProductionSettings(AppBaseSettings):
    """
    This is a production settings class.
    This class are going to configure the application to run in production with aws secrets manager.
    """

    environment: EnvironmentStages = EnvironmentStages.PRODUCTION
    api_config: FastAPIConfig = FastAPIConfig(debug=False)
    database_url: str = Field(description='Database URL', examples=['sqlite:///./db.sqlite3'])
    secret_key: str = Field(description='Secret key for JWT token', examples=['secret'])
    version: str = Field(description='Application version', examples=['1.0.0'])
    model_config = SettingsConfigDict()
