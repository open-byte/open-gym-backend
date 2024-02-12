from typing import Optional

from sqlmodel import Field, SQLModel


class BaseSQLModel(SQLModel):
    """
    Base SQLModel class with an optional id field.
    We can use this class as a base class for all our models.
    if we need to add new id field, we can override the id field in the subclass.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
