from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from auth.constants import AUTH_MODEL
from database.repository import SQLModelRepository


class AuthRepository(SQLModelRepository[AUTH_MODEL]):
    def __init__(self, async_session: AsyncSession):
        super().__init__(async_session, AUTH_MODEL)

    async def get_user_by_username(self, username: str) -> AUTH_MODEL | None:
        """
        Gets a user by their username.

        Args:
            username (str): The username of the user.

        Returns:
            AUTH_MODEL: The user with the provided username.
        """
        statement = select(self._model).where(self._model.username == username)

        result = await self.async_session.execute(statement)

        return result.scalar_one_or_none()
