import os

from config.environments import (
    AppBaseSettings,
    DevelopmentSettings,
    EnvironmentStages,
    ProductionSettings,
    StagingSettings,
)


def get_settings() -> AppBaseSettings:
    """
    This function is going to return the settings class based on the environment variable.
    """
    environment = os.getenv('ENVIRONMENT', EnvironmentStages.DEVELOPMENT)
    match environment:
        case EnvironmentStages.DEVELOPMENT:
            return DevelopmentSettings()
        case EnvironmentStages.STAGING:
            return StagingSettings()
        case EnvironmentStages.PRODUCTION:
            return ProductionSettings()
        case _:
            return DevelopmentSettings()
