from aiogram import F, Router
from aiogram.types import Message

from bot.database.database import SessionLocal

from bot.handlers.get_info_db.service import get_info_db_service

from bot.handlers.get_product.models import ProductCard

router = Router()


@router.message(F.text == "получить информацию из БД")
async def get_info_db(message: Message):
    db = SessionLocal()
    await get_info_db_service(db, message)