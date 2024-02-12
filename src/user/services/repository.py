from sqlalchemy.ext.asyncio import AsyncSession

from auth.utils import get_password_hash
from database.repository import SQLModelRepository
from user.models.general import User


class UserRepository(SQLModelRepository[User]):
    def __init__(self, async_session: AsyncSession):
        super().__init__(async_session, User)

    async def set_password(self, user: User, password: str) -> User:
        """
        Sets the password for a user.

        Args:
            id (str): The ID of the user.
            password (str): The password to set.

        Returns:
            User: The user with the updated password.
        """
        salt = user.created_at.isoformat()  # type: ignore

        user.hashed_password = get_password_hash(password=password, salt=salt)

        self.async_session.add(user)
        await self.async_session.commit()
        await self.async_session.refresh(user)

        return user
