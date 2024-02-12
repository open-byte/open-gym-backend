from abc import ABC, abstractmethod
from typing import Any, Generic, Sequence, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from database.base import BaseSQLModel

_M = TypeVar('_M', bound=BaseSQLModel)


class BaseRepository(ABC, Generic[_M]):
    def __init__(self, async_session: AsyncSession):
        self.async_session = async_session

    @abstractmethod
    async def get(self, id: Any) -> _M | None:
        pass

    @abstractmethod
    async def get_all(self) -> Sequence[_M]:
        pass

    @abstractmethod
    async def create(self, obj: _M) -> _M:
        pass

    @abstractmethod
    async def update(self, oid: Any, bj: _M) -> _M | None:
        pass

    @abstractmethod
    async def delete(self, obj: _M) -> _M | None:
        pass


class SQLModelRepository(BaseRepository[_M]):
    _model: Type[_M]

    def __init__(self, async_session: AsyncSession, model: Type[_M]):
        """
        Initializes a new instance of the SQLModelRepository class.

        Args:
            async_session (AsyncSession): The async session used for database operations.
            model (Type[_M]): The model type associated with the repository.
        """
        self._model = model
        super().__init__(async_session)

    async def get(self, id: Any) -> _M | None:
        """
        Retrieves an object from the database based on its ID.

        Args:
            id (Any): The ID of the object to retrieve.

        Returns:
            _M | None: The retrieved object, or None if the object does not exist.
        """
        statement = select(self._model).where(self._model.id == id)
        result = await self.async_session.execute(statement)
        return result.scalar_one_or_none()

    async def get_all(self) -> Sequence[_M]:
        """
        Retrieves all objects from the database.

        Returns:
            Sequence[_M]: A sequence of all objects in the database.
        """
        statement = select(self._model)
        result = await self.async_session.execute(statement)
        return result.scalars().all()

    async def create(self, obj: _M) -> _M:
        """
        Creates a new object in the database.

        Args:
            obj (_M): The object to create.

        Returns:
            _M: The created object.
        """
        self.async_session.add(obj)
        await self.async_session.commit()
        await self.async_session.refresh(obj)
        return obj

    async def update(self, id: Any, obj: _M) -> _M | None:
        """
        Updates an existing object in the database.

        Args:
            id (Any): The ID of the object to update.
            obj (_M): The object to update.

        Returns:
            _M | None: The updated object, or None if the object does not exist.
        """
        record = await self.get(id)
        if record is None:
            return None

        for attr, value in obj.model_dump(exclude_none=True).items():
            setattr(record, attr, value)

        self.async_session.add(record)
        await self.async_session.commit()
        await self.async_session.refresh(record)
        return record

    async def delete(self, id: Any) -> _M | None:
        """
        Deletes an object from the database.

        Args:
            id (Any): The ID of the object to delete.

        Returns:
            _M | None: The deleted object, or None if the object does not exist.
        """
        record = await self.get(id)
        if record is None:
            return None
        await self.async_session.delete(record)
        await self.async_session.commit()
        return record
