from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, func
from sqlmodel import Field

from database.base import BaseSQLModel


class User(BaseSQLModel, table=True):
    """
    This class represents the User model.
    """

    username: str = Field(max_length=50, unique=True)
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)
    email: str = Field(max_length=100, unique=True)
    hashed_password: Optional[str] = Field(default=None)
    is_active: bool = Field(default=True)
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=True,
        ),
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=True,
        ),
    )

    @property
    def full_name(self) -> str:
        """
        Returns the full name of the user.

        Returns:
            str: The full name of the user.
        """
        return f'{self.first_name} {self.last_name}'.title()
