import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Dispatcher, Bot

from handlers.user import router as user_router
from handlers.admin import router as admin_router
from database.models import async_main


async def main():
    load_dotenv()

    await async_main()

    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(user_router, admin_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')