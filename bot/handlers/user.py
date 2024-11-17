import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.enums import ChatAction

import keyboards.main as kb

router = Router()


@router.message(CommandStart())
async def cmnd_start(message: Message):
    await message.answer(text='Привет!')
