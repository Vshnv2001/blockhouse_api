from fastapi import FastAPI, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 


@app.get('/') # get method to empty endpoint
def first_response(db: Session = Depends(get_db)):
    return crud.get_trade_orders(db)

@app.get('/orders')
def get_orders(db: Session = Depends(get_db)):
    return crud.get_trade_orders(db)

@app.post('/orders')
def create_order(trade_order: schemas.TradeOrder, db: Session = Depends(get_db)):
    try:
        crud.add_trade_order(db, trade_order)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
    return {"response": "success"}