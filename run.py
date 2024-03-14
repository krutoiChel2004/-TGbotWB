import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.database.database import engine, Base

from bot.handlers.get_product.router import router as get_product_router
from bot.handlers.get_info_db.router import router as get_info_db_router
from bot.handlers.start import router as start_router

bot = Bot(token='6841413813:AAFtkQ8sZAEaAqLeoAW4-kLLJLULZMVZS1A')
dp = Dispatcher()


async def main():
    Base.metadata.create_all(bind=engine)

    dp.include_router(start_router)
    dp.include_router(get_product_router)
    dp.include_router(get_info_db_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")