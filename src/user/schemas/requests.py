from typing import Any

from pydantic import BaseModel, Field, root_validator


class UserCreateRequestBody(BaseModel):
    """
    This is a request body schema for creating a new user.
    """

    username: str = Field(examples=['john_doe', 'jane_doe'])
    first_name: str = Field(examples=['John', 'Jane'])
    last_name: str = Field(examples=['Doe', 'Doe'])
    email: str = Field(examples=['test@test.com'])
    password: str = Field(examples=['password123'])
    verify_password: str = Field(examples=['password123'])

    @root_validator(pre=True)
    def verify_passwords_match(cls, values: dict[str, Any]) -> dict[str, Any]:
        """
        Check if the password and verify_password fields in the given values dictionary match.

        Args:
            values (dict[str, Any]): A dictionary containing the values to be checked.

        Raises:
            ValueError: If the password and verify_password fields do not match.

        Returns:
            dict[str, Any]: The original values dictionary.

        """
        if values.get('password') != values.get('verify_password'):
            raise ValueError('password and verify_password do not match')

        return values


class UserUpdateRequestBody(BaseModel):
    """
    This is a request body schema for updating a user.
    """

    username: str = Field(examples=['john_doe', 'jane_doe'])
    first_name: str = Field(examples=['John', 'Jane'])
    last_name: str = Field(examples=['Doe', 'Doe'])
    email: str = Field(examples=['test1@test.com'])
