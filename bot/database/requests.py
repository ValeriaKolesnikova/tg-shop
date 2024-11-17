from .models import User, Category, Item, Cart, async_session
from sqlalchemy import select, update, delete, and_


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id==tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))


async def get_items(category_id):
    async with async_session() as session:
        return await session.scalars(select(Item).where(
            and_(Item.category==category_id,
                 Item.availability==True)
        ))


async def get_item(item_id):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.id==item_id))