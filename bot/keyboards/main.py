from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, 
    InlineKeyboardButton, InlineKeyboardMarkup
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Шлю нахуй')],
    [KeyboardButton(text='Люблю')],
], resize_keyboard=True, input_field_placeholder='Выбери мое действие')

main_inlline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Корзина', callback_data='cart')],
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacs')],
])

async def catalog_kb():
    all_data = ('Nike', 'Adidas', 'Puma')

    keyboard = ReplyKeyboardBuilder()

    for data in all_data:
        keyboard.add(KeyboardButton(text=data))
    return keyboard.adjust(2).as_markup()