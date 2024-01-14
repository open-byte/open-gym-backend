from config.settings import get_settings
from core.schemas.responses import (
    CJSONResponse,
    InformationalResponse,
    ResponseSchema,
)
from core.tags import OpenAPITags
from fastapi import FastAPI, status

settings = get_settings()
app = FastAPI(
    **settings.api_config.model_dump(),
    default_response_class=CJSONResponse,
)


@app.get(
    '/info',
    tags=[OpenAPITags.INFORMATIONAL],
    description='Information about application',
    status_code=status.HTTP_200_OK,
)
async def info() -> ResponseSchema[InformationalResponse]:
    """
    Information about application

    Returns:
        ResponseSchema[InformationalResponse]: Information about application
    """
    healthcheck = InformationalResponse(
        status='success',
        environment='dev',
        version='1.0.0',
    )

    response = ResponseSchema(
        code=0,
        data=healthcheck,
        status_code=status.HTTP_200_OK,
    )

    return response
