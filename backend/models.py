from sqlalchemy import Column, String, Float, BigInteger, Date
from database import Base

class TradeOrders(Base):
    __tablename__ = "trade_orders"
    
    id = Column(BigInteger, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)
    quantity = Column(BigInteger)
    order_type = Column(String)
    date = Column(Date)