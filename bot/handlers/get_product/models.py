from sqlalchemy import Column, Integer, String, Float, DateTime
import pytz 
from datetime import datetime

from bot.database.database import Base

def get_time():
    return datetime.now(pytz.timezone('Europe/Moscow'))

class ProductCard(Base):
    __tablename__ = "product_card"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(1000))
    article = Column(String)
    priceU = Column(Integer)
    salePriceU = Column(Integer)
    reviewRating = Column(Float)
    qty = Column(Integer)
    date_request = Column(DateTime, nullable=False, default=get_time)
    user_id = Column(Integer, default=0)