from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class JWTTokenSchema(BaseModel):
    access_token: str = Field(
        description='JWT access token',
        examples=[
            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ'
        ],
    )
    token_type: str = Field(description='Token type', examples=['Bearer'])


class JWTPasswordCredentialsSchema(BaseModel):
    username: str = Field(
        description='Username',
        examples=['john_doe'],
    )
    password: str = Field(
        description='Password',
        examples=['password'],
    )


class JWTUserSchema(BaseModel):
    id: int = Field(
        description='User ID',
        examples=[1],
    )
    username: str = Field(
        description='Username',
        examples=['john_doe'],
    )
    email: str = Field(
        description='Email',
        examples=['test@test.com'],
    )
    full_name: Optional[str] = Field(
        description='Full name',
        examples=['John Doe'],
    )


class JWTTokenDataSchema(BaseModel):
    sub: Optional[str] = Field(description='Subject', examples=['john_doe'])
    user: JWTUserSchema = Field(description='User')
    exp: Optional[datetime] = Field(
        default=None, description='Expiration time', examples=[datetime.now()]
    )

    model_config = {
        'validate_assignment': True,
    }
