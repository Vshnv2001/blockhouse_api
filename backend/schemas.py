from pydantic import BaseModel
from typing import Optional
import datetime
import uuid

class TradeOrder(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str
    
    class Config:
        orm_mode = True