from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from bot.database.database import SessionLocal
from sqlalchemy.orm import Session

from bot.handlers.get_product.service import get_product_card

router = Router()

class GetProduct(StatesGroup):
    item_number = State()

@router.message(F.text == 'Получить информацию по товару:')
async def input_item_number_first(message: Message, state: FSMContext):
    await state.set_state(GetProduct.item_number)
    await message.answer("Введите артикул товара")

@router.message(GetProduct.item_number)
async def input_item_number_second(message: Message, state: FSMContext):
    await state.update_data(item_number=message.text)
    data = await state.get_data()
    db = SessionLocal()
    product_card = get_product_card(data["item_number"], message.from_user.id, db)
    await message.answer(product_card)
    await state.clear()