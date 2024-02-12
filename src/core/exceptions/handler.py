from fastapi import Request, status
from fastapi.exceptions import ValidationException
from pydantic_core import ValidationError

from config.settings import get_settings
from core.exceptions.exceptions import APIHTTPException
from core.responses import CJSONResponse
from core.schemas.responses import ErrorResponse, ResponseSchema

_setting = get_settings()


def http_exception_handler(request: Request, exc: Exception) -> CJSONResponse:
    if isinstance(exc, APIHTTPException):
        response = ResponseSchema(
            code=-1,
            data=ErrorResponse(
                code=exc.detail.get('code', 'unknown_error'),  # type: ignore [attr-defined]
                description=exc.detail.get('description', 'Unknown error'),  # type: ignore [attr-defined]
            ),
            status_code=exc.status_code,
        )

    elif isinstance(exc, ValidationException) or isinstance(exc, ValidationError):
        error = exc.errors()[0]
        loc: tuple[str, ...] = error.get('loc')  # type: ignore

        msg = f'{error.get('msg', 'Validation error')} at '
        msg += '> '.join(loc) if loc else 'unknown location'

        response = ResponseSchema(
            code=-1,
            data=ErrorResponse(
                code=f'validation_error_{error.get("type", "unknown")}',
                description=msg,
            ),
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    elif isinstance(exc, Exception) and _setting.api_config.debug:
        response = ResponseSchema(
            code=-1,
            data=ErrorResponse(
                code='internal_server_error',
                description=str(exc),
            ),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    else:
        response = ResponseSchema(
            code=-1,
            data=ErrorResponse(
                code='internal_server_error',
                description='Internal server error',
            ),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return CJSONResponse(content=response.model_dump())
