from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from app import models,schemas,crud
from app.database import engine,get_db
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app=FastAPI(title="Expense Tracker App")

origins=[
    "http://localhost:3000",
    "http://;pcalhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@app.post("/transaction/",response_model=schemas.Transaction)
def create_transaction(transaction:schemas.TransactionCreate,db:Session=Depends(get_db)):
    return crud.create_transaction(db,transaction)

@app.get("/transaction/",response_model=list[schemas.Transaction])
def read_transaction(db:Session=Depends(get_db)):
    return crud. get_transactions(db)


@app.get("/transaction/{transaction_id}" ,response_model=schemas.Transaction)
def read_transaction(transaction_id:int,db:Session=Depends(get_db)):
    db_transaction=crud.get_transaction(db,transaction_id)
    if not db_transaction:
        raise HTTPException(status_code=404 ,detail="Transaction not found")
    return db_transaction

@app.put("/transaction/{transaction_id}",response_model=schemas.Transaction)
def update_transaction(transaction_id:int,transaction:schemas.TransactionCreate,db:Session=Depends(get_db)):
    return crud.update_transaction(db,transaction_id,transaction)

@app.delete("/transaction/{transaction_id}")
def delete_transaction(transaction_id:int,db:Session=Depends(get_db)):
    crud.delete_transaction(db,transaction_id)
    return {"massage":"Transaction Delete successfully"}

@app.get("/summary")
def summary(db:Session=Depends(get_db)):
    return crud.get_summary(db)

@app.get("/categorycal_brakdown")
def category_breakbown(db:Session=Depends(get_db)):
    return crud.get_category_breakdown(db)


