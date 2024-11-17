from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, 
    InlineKeyboardButton, InlineKeyboardMarkup
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from database.requests import get_categories, get_items

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Поиск')],
    [KeyboardButton(text='Контакты')],
])
async def item_buttons(item_id):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='В корзину', callback_data=f'cart_{item_id}')],
        [InlineKeyboardButton(text='Назад', callback_data='back')],
    ])
    return keyboard


async def build_kb(data, param):
    keyboard = InlineKeyboardBuilder()

    for item in data:
        keyboard.add(InlineKeyboardButton(
            text=item.name, 
            callback_data=f'{param}_{item.id}')
        )
    return keyboard.adjust(2).as_markup()


async def get_catalog_kb():
   return await build_kb(await get_categories(), param='category')


async def get_items_kb(category_id):
    return await build_kb(await get_items(category_id), param='items')