from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt  # type: ignore

from auth.constants import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    AUTH_MODEL,
    JWT_ALGORITHM,
)
from auth.exceptions import (
    JWTInvalidCredentials,
    JWTNoAuthorizationAccess,
    JWTUnknownError,
    JWTUserInactive,
)
from auth.schemas import (
    JWTPasswordCredentialsSchema,
    JWTTokenDataSchema,
    JWTUserSchema,
)
from auth.services.repository import AuthRepository
from auth.utils import verify_password
from config.settings import get_settings

_settings = get_settings()


class AuthJWTService:
    _JWT_ALGORITHM: str = JWT_ALGORITHM
    _ACCESS_TOKEN_EXPIRE_MINUTES: int = ACCESS_TOKEN_EXPIRE_MINUTES
    _SECRET_KEY: str
    _repository: AuthRepository

    def __init__(self, repository: AuthRepository) -> None:
        self._SECRET_KEY = _settings.secret_key
        self._repository = repository

    def __create_access_token(self, data: JWTTokenDataSchema) -> str:
        """
        Creates an access token with the provided data.

        Args:
            data (JWTTokenDataSchema): The data to be encoded in the access token.

        Returns:
            str: The generated access token.
        """
        expire = datetime.now(timezone.utc) + timedelta(minutes=self._ACCESS_TOKEN_EXPIRE_MINUTES)
        data.exp = expire
        jwt_token: str = jwt.encode(
            data.model_dump(), key=self._SECRET_KEY, algorithm=self._JWT_ALGORITHM
        )

        return jwt_token

    async def create_access_token(self, credentials: JWTPasswordCredentialsSchema) -> str:
        """
        Creates an access token for the provided user.

        Args:
            user (JWTTokenDataSchema): The user to create the access token for.

        Returns:
            str: The generated access token.
        """
        user = await self._repository.get_user_by_username(credentials.username)

        if user is None:
            raise JWTInvalidCredentials

        if user.hashed_password is None:
            raise JWTInvalidCredentials

        salt = user.created_at.isoformat()  # type: ignore

        if not verify_password(credentials.password, salt, user.hashed_password):
            raise JWTInvalidCredentials

        user_data = JWTUserSchema(
            id=user.id,
            username=user.username,
            email=user.email,
            full_name=user.full_name,
        )

        token_data = JWTTokenDataSchema(
            sub=user.username,
            user=user_data,
        )

        return self.__create_access_token(token_data)

    async def get_current_user(self, token: str) -> AUTH_MODEL:
        """
        Decodes the provided token and returns the user associated with it.

        Args:
            token (str): The token to decode.

        Returns:
            JWTTokenDataSchema: The user associated with the token.
        """
        try:
            payload = jwt.decode(token, self._SECRET_KEY, algorithms=[self._JWT_ALGORITHM])

        except JWTError:
            raise JWTNoAuthorizationAccess

        username: str = payload.get('sub')

        user = await self._repository.get_user_by_username(username)

        if user is None:
            raise JWTUnknownError

        if not user.is_active:
            raise JWTUserInactive

        return user
