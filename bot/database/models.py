import os
from dotenv import load_dotenv

from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, 
    AsyncAttrs
)

load_dotenv()
engine = create_async_engine(
    url=os.getenv('SQLACLCHEMY_URL'), echo=True
)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=25))


class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=50))
    description: Mapped[str] = mapped_column(String(length=250))
    category: Mapped[int] = mapped_column(ForeignKey(column='categories.id'))
    price: Mapped[str] = mapped_column(String(length=10))
    availability: Mapped[bool] = mapped_column()
    quantity: Mapped[int] = mapped_column()

class Cart(Base):
    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    item: Mapped[int] = mapped_column(ForeignKey('items.id'))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
