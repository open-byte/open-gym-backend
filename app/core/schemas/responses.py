from typing import Any, Generic, TypeVar

from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field

M = TypeVar('M', bound=BaseModel)


def schema_extra(schema: dict[str, Any], _: Any) -> None:
    props = {k: v for k, v in schema['properties'].items() if not v.get('hidden')}
    schema['properties'] = props


class ResponseSchema(BaseModel, Generic[M]):
    """
    This is a generic response schema for all API endpoints.
    For status code we add `json_schema_extra` to hide it from documentation.
    because we use `status_code` to set HTTP status code in CJSONResponse class.

    Args:
        BaseModel (_type_): Base model from pydantic
        Generic (_type_): Generic class M for documentation purposes and `data` field
    """

    code: int = Field(
        description='Response code, 0 for success, -1 for soft error, -2 for hard error'
    )
    data: M = Field(description='Response data model [BaseModel]')
    status_code: int = Field(
        description='HTTP status code',
        examples=[200, 400, 500],
        json_schema_extra={'hidden': True},
    )

    model_config = ConfigDict(json_schema_extra=schema_extra)


class ErrorResponse(BaseModel):
    """
    This is a generic error response schema for all API endpoints.
    This schema is for raising errors in API endpoints.
    """

    code: str = Field(
        description='Error code',
        examples=['invalid_request', 'invalid_token', 'invalid_grant', 'invalid_client'],
    )
    description: str = Field(description='Error description', examples=['Invalid request'])


class InformationalResponse(BaseModel):
    """
    This is a healthcheck response schema for healthcheck API endpoint.
    """

    status: str = Field(description='Healthcheck status', examples=['success', 'fail'])
    environment: str = Field(description='Application environment', examples=['dev', 'prod'])
    version: str = Field(description='Application version', examples=['1.0.0'])


class CJSONResponse(JSONResponse):
    """
    This is a custom JSON response class for all API endpoints.
    """

    def __init__(self, content: Any = None, status_code: int = 200, **kwargs: Any) -> None:
        """
        This is a custom JSON response class for all API endpoints.

        Args:
            content (dict, optional): Response content. Defaults to None.
            status_code (int, optional): HTTP status code. Defaults to 200.
        """
        status_code = content.pop('status_code', status_code)

        super().__init__(content=content, status_code=status_code, **kwargs)
