from sqlalchemy.orm import Session
import models, schemas
import datetime

def get_trade_orders(db: Session):
    return db.query(models.TradeOrders).all()


def add_trade_order(db: Session, trade_order: schemas.TradeOrder):
    new_order = models.TradeOrders(symbol=trade_order.symbol, price=trade_order.price, quantity=trade_order.quantity, order_type=trade_order.order_type, date=datetime.datetime.now())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order