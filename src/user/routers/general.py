from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession

from auth.dependencies import authentication
from core.schemas.responses import ResponseSchema
from core.tags import OpenAPITags
from database.session import get_session
from user.models.general import User
from user.schemas.general import UserSchema
from user.schemas.requests import UserCreateRequestBody, UserUpdateRequestBody
from user.services.general import UserGeneralService
from user.services.repository import UserRepository

_MODULE = 'user'
router = APIRouter(
    prefix=f'/{_MODULE}',
    tags=[OpenAPITags.USERS],
    dependencies=[Depends(authentication)],
)


@router.get(
    '/me',
    description='Retrieve the current user.',
)
async def get_current_user(
    user: Annotated[User, Depends(authentication)],
) -> ResponseSchema[UserSchema]:
    """
    Get the current user.

    Parameters:
    - user: The authenticated user.

    Returns:
    - ResponseSchema[UserSchema]: The response containing the user data.

    """
    return ResponseSchema(
        code=0,
        data=UserSchema.model_validate(user, from_attributes=True),
        status_code=status.HTTP_200_OK,
    )


@router.get('')
async def get_all_users(
    db_session: AsyncSession = Depends(get_session),
) -> ResponseSchema[list[UserSchema]]:
    """
    Retrieves a list of all users from the database.

    Parameters:
        db_session: The database session to use for the operation.

    Returns:
        A ResponseSchema object containing the serialized list of UserResponse objects.
    """
    _service = UserGeneralService(UserRepository(db_session))
    user_list = await _service.get_all()
    return ResponseSchema(
        code=0,
        data=user_list,
        status_code=status.HTTP_200_OK,
    )


@router.post('')
async def create_user(
    data: UserCreateRequestBody, async_session: AsyncSession = Depends(get_session)
) -> ResponseSchema[UserSchema]:
    """
    Create a new user.

    Args:
        data (UserRequestBody): The request body containing user data.

    Returns:
        ResponseSchema[UserResponse]: The response schema containing user data.
    """
    _service = UserGeneralService(UserRepository(async_session))
    user = await _service.create(data)

    return ResponseSchema(
        code=0,
        data=user,
        status_code=status.HTTP_201_CREATED,
    )


@router.get('/{id}')
async def get_user_by_id(
    id: int, db_session: AsyncSession = Depends(get_session)
) -> ResponseSchema[UserSchema]:
    """
    Retrieve a user by their ID.

    Args:
        id (int): The ID of the user to retrieve.
        db_session (AsyncSession, optional): The database session. Defaults to Depends(get_session).

    Returns:
        ResponseSchema[UserResponse]: The response schema containing the user data.

    """
    _service = UserGeneralService(UserRepository(db_session))
    user = await _service.get(id)
    return ResponseSchema(
        code=0,
        data=user,
        status_code=status.HTTP_200_OK,
    )


@router.put('/{id}')
async def update_user(
    id: int, data: UserUpdateRequestBody, db_session: AsyncSession = Depends(get_session)
) -> ResponseSchema[UserSchema]:
    """
    Update a user with the given user_id using the provided data.

    Args:
        id (int): The ID of the user to update.
        data (UserUpdateRequestBody): The data to update the user with.
        db_session (AsyncSession, optional): The database session. Defaults to Depends(get_session).

    Returns:
        ResponseSchema[UserSchema]: The response schema containing the updated user data.

    """
    _service = UserGeneralService(UserRepository(db_session))
    user = await _service.update(id, data)

    return ResponseSchema(
        code=0,
        data=user,
        status_code=status.HTTP_200_OK,
    )


@router.delete('/{user_id}')
async def delete_user(
    id: int, db_session: AsyncSession = Depends(get_session)
) -> ResponseSchema[UserSchema]:
    """
    Delete a user by their ID.

    Args:
        user_id (int): The ID of the user to delete.
        db_session (AsyncSession, optional): The database session. Defaults to Depends(get_session).

    Returns:
        ResponseSchema[UserResponse]: The response schema containing the deleted user data.
    """
    _service = UserGeneralService(UserRepository(db_session))
    user = await _service.delete(id)

    return ResponseSchema(
        code=0,
        data=user,
        status_code=status.HTTP_200_OK,
    )
