from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security.http import HTTPBearer
from sqlmodel.ext.asyncio.session import AsyncSession

from auth.constants import AUTH_MODEL
from auth.exceptions import JWTInvalidCredentials
from auth.services.repository import AuthRepository
from auth.services.services import AuthJWTService
from database.session import get_session

authorization_scheme = HTTPBearer(auto_error=False)


async def authentication(
    db_session: Annotated[AsyncSession, Depends(get_session)],
    token: HTTPAuthorizationCredentials | None = Depends(authorization_scheme),
) -> AUTH_MODEL:
    """
    Get the current user from the provided database session.

    Args:
        db_session (AsyncSession, optional): The database session. Defaults to Depends(get_session).

    Returns:
        User: The current user.
    """
    if token is None:
        raise JWTInvalidCredentials

    _service = AuthJWTService(AuthRepository(async_session=db_session))

    return await _service.get_current_user(token.credentials)
