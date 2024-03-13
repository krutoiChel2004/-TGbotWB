from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

import bot.keyboards.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Начало работы", reply_markup=kb.main)
