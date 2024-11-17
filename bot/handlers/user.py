import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import keyboards.main as kb
from database import requests as rq

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id) 
    await message.answer(
        text='Привет! Добро пожаловать в наш магазин',
        reply_markup=kb.main
    )


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer(
        text='Выберете бренд товара',
        reply_markup=await kb.get_catalog_kb()
    )


@router.callback_query(F.data.startswith('category_'))
async def category_items(callback: CallbackQuery):
    await callback.answer('Pick')
    await callback.message.answer(
        'Pick', 
        reply_markup=await kb.get_items_kb(callback.data.split('_')[1])
    )


@router.callback_query(F.data.startswith('items_'))
async def item_card(callback: CallbackQuery):
    item = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.answer(
        f'Название: {item.name}\nОписание: {item.description}\n'
        f'Стоимость: {item.price}\nКол-во: {item.quantity}',
        reply_markup=await kb.item_buttons(item)
    )
