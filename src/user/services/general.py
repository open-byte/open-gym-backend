from user.exceptions import UserNotFoundException
from user.models.general import User
from user.schemas.general import UserSchema
from user.schemas.requests import UserCreateRequestBody, UserUpdateRequestBody
from user.services.repository import UserRepository


class UserGeneralService:
    _repository: UserRepository

    def __init__(self, repository: UserRepository):
        """
        Initializes a new instance of the UserGeneralService class.

        Args:
            repository (UserRepository): The repository used for data access.
        """
        self._repository = repository

    async def get(self, id: int) -> UserSchema:
        """
        Retrieves a user by ID.

        Args:
            id (int): The ID of the user to retrieve.

        Returns:
            User: The retrieved user.

        Raises:
            APIHTTPException: If the user is not found.
        """
        user = await self._repository.get(id)

        if user is None:
            raise UserNotFoundException

        return UserSchema.model_validate(user, from_attributes=True)

    async def get_all(self) -> list[UserSchema]:
        """
        Retrieves all users.

        Returns:
            Sequence[User]: A sequence of all users.
        """
        user_list = await self._repository.get_all()

        return [UserSchema.model_validate(user, from_attributes=True) for user in user_list]

    async def create(self, data: UserCreateRequestBody) -> UserSchema:
        """
        Creates a new user.

        Args:
            user (User): The user to create.

        Returns:
            User: The created user.
        """

        user = User.model_validate(data, from_attributes=True)

        user = await self._repository.create(user)

        user = await self._repository.set_password(user, data.password)

        return UserSchema.model_validate(user, from_attributes=True)

    async def update(self, id: int, data: UserUpdateRequestBody) -> UserSchema:
        """
        Updates a user by ID.

        Args:
            id (int): The ID of the user to update.
            user (User): The updated user data.

        Returns:
            User: The updated user.

        Raises:
            APIHTTPException: If the user is not found.
        """
        user = User.model_validate(data, from_attributes=True)
        updated_user = await self._repository.update(id, user)

        if updated_user is None:
            raise UserNotFoundException

        return UserSchema.model_validate(updated_user, from_attributes=True)

    async def delete(self, id: int) -> UserSchema:
        """
        Deletes a user by ID.

        Args:
            id (int): The ID of the user to delete.

        Returns:
            User: The deleted user.

        Raises:
            APIHTTPException: If the user is not found.
        """
        deleted_user = await self._repository.delete(id)
        if deleted_user is None:
            raise UserNotFoundException

        return UserSchema.model_validate(deleted_user, from_attributes=True)
