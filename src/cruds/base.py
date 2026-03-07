from typing import Generic, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.decl_api import DeclarativeBase

ModelType = TypeVar("ModelType", bound=DeclarativeBase)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseCRUD(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_by_id(
            self,
            db: AsyncSession,
            *,
            id: int
    ) -> ModelType | None:
        statement = select(self.model).where(self.model.id == id)
        result = await db.execute(statement)
        return result.scalars().first()

    async def create(
            self,
            db: AsyncSession,
            *,
            obj_in: CreateSchemaType,
            commit: bool = True
    ) -> ModelType:
        db_obj = self.model(**obj_in.model_dump())
        db.add(db_obj)
        if commit:
            await db.commit()
            await db.refresh(db_obj)
        return db_obj
