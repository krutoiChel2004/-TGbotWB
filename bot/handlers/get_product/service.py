import requests

from sqlalchemy.orm import Session

from bot.handlers.get_product.models import ProductCard

def get_JSON_product(item_number: str):
    result = requests.get(f"https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={item_number}").json()
    try:
        return result["data"]["products"][0]
    except:
        return None

def all_qty(list_sizes: list):
    summ = 0
    for i in list_sizes:
        for j in i["stocks"]:
            summ += j["qty"]
    return summ

def get_product_card(item_number: str, user_id: int, db: Session):
    result = get_JSON_product(item_number)

    if result is None:
        return "Вы ввели несуществующий артикул"

    product_dict = {
        "name": result["name"],
        "article": result["id"],
        "priceU": str(result["priceU"])[0:-2],
        "salePriceU": str(result["salePriceU"])[0:-2],
        "reviewRating": result["reviewRating"],
        "qty": all_qty(result["sizes"]),
    }

    product_card_db = ProductCard(
        name=product_dict["name"],
        article=product_dict["article"],
        priceU=int(product_dict["priceU"]),
        salePriceU=int(product_dict["salePriceU"]),
        reviewRating=product_dict["reviewRating"],
        qty=product_dict["qty"],
        user_id=user_id
    )

    db.add(product_card_db)
    db.commit()
    db.refresh(product_card_db)

    product_card = (
    f"""
    {product_dict["name"]}
    Артикул:{product_dict["article"]}
    Цена без скидки:{product_dict["priceU"]}
    Цена со скидкой:{product_dict["salePriceU"]}
    Рейтинг товара:{product_dict["reviewRating"]}
    Кол-во:{product_dict["qty"]}
    """
    )

    return product_card