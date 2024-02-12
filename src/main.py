from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError, ValidationException

from auth.router import router as auth_router
from config.settings import get_settings
from core.exceptions.handler import http_exception_handler
from core.responses import CJSONResponse
from core.schemas.responses import (
    InformationalResponse,
    ResponseSchema,
)
from core.tags import OpenAPITags
from user.routers.general import router as user_router

settings = get_settings()

app = FastAPI(
    **settings.api_config.model_dump(),
    default_response_class=CJSONResponse,
)

app.add_exception_handler(Exception, http_exception_handler)
app.add_exception_handler(ValueError, http_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(ValidationException, http_exception_handler)
app.add_exception_handler(RequestValidationError, http_exception_handler)

app.include_router(auth_router)
app.include_router(user_router)


@app.post(
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
    information = InformationalResponse(
        status='success',
        environment=settings.environment,
        version=settings.version,
    )

    response = ResponseSchema(
        code=0,
        data=information,
        status_code=status.HTTP_200_OK,
    )

    return response
