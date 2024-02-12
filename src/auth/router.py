from typing import Annotated

from fastapi import APIRouter, Body, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession

from auth.schemas import JWTPasswordCredentialsSchema, JWTTokenSchema
from auth.services.repository import AuthRepository
from auth.services.services import AuthJWTService
from core.schemas.responses import ResponseSchema
from core.tags import OpenAPITags
from database.session import get_session

router = APIRouter(prefix='/auth', tags=[OpenAPITags.AUTH])


@router.post('/token')
async def get_token(
    credentials: Annotated[JWTPasswordCredentialsSchema, Body(...)],
    db_session: AsyncSession = Depends(get_session),
) -> ResponseSchema[JWTTokenSchema]:
    """
    Retrieves a JWT token based on the provided credentials.

    Args:
        credentials (JWTPasswordCredentialsSchema): The user's credentials.
        db_session (AsyncSession, optional): The database session. Defaults to Depends(get_session).

    Returns:
        ResponseSchema[JWTTokenSchema]: The response containing the JWT token.

    """
    _service = AuthJWTService(AuthRepository(async_session=db_session))

    jwt_token = await _service.create_access_token(credentials=credentials)

    response = ResponseSchema(
        code=0,
        data=JWTTokenSchema(
            access_token=jwt_token,
            token_type='bearer',
        ),
        status_code=status.HTTP_200_OK,
    )
    return response
