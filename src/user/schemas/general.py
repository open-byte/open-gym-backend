from datetime import datetime

from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    """
    This is a response schema for the User model.

    We use this schema to serialize/deserialize User model data.
    """

    id: int = Field(examples=[1, 2])
    username: str = Field(examples=['john_doe', 'jane_doe'])
    first_name: str = Field(examples=['John', 'Jane'])
    last_name: str = Field(examples=['Doe'])
    email: str = Field(examples=['test@test.com'])
    is_active: bool = Field(examples=[True, False])
    created_at: datetime = Field(examples=[datetime.utcnow()])
    updated_at: datetime = Field(examples=[datetime.utcnow()])
