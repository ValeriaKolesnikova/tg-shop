import asyncio
import config

from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart


bot = Bot(token=config.TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmnd_start(message: Message):
    await message.answer('Hello!')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print('Exit')