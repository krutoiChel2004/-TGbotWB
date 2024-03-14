from aiogram.types import Message

from sqlalchemy.orm import Session

from bot.handlers.get_product.models import ProductCard

async def get_info_db_service(db: Session, message: Message): 
    cards = db.query(ProductCard).filter(ProductCard.user_id == message.from_user.id).order_by(ProductCard.id.desc()).limit(5)
    if cards is None:
        await message.answer("Записей нет")
        return None
    for card in cards:
        product_card = (
            f"""
            {card.name}
            Артикул:{card.article}
            Цена без скидки:{card.priceU}
            Цена со скидкой:{card.salePriceU}
            Рейтинг товара:{card.reviewRating}
            Кол-во:{card.qty}
            """
            )
        await message.answer(product_card)