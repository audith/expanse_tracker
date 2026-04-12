from sqlalchemy.orm import Session
from app import models,schemas
from sqlalchemy import func

def create_transaction(db:Session,transaction:schemas.TransactionCreate):
    db_transaction=models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def get_transactions(db:Session):
    return db.query(models.Transaction).all()

def get_transaction(db:Session,transaction_id:int):
    return db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()


def update_transaction(db:Session,transaction_id:int,transaction:schemas.TransactionCreate):
    db_transaction=get_transaction(db,transaction_id)
    if db_transaction:
        for key,value in transaction.dict().items():
            setattr(db_transaction,key,value)
        db.commit()
        db.refresh(db_transaction)
    return db_transaction

def delete_transaction(db:Session,transaction_id:int):
    db_transaction=get_transaction(db,transaction_id)
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
    return db_transaction

def get_summary(db:Session):
    total_income=db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.type=="Income").scalar() or 0
    total_expense=db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.type == "expense").scalar() or 0
    return {"total_income": total_income,"total_expense":total_expense, "balance":total_income-total_expense}

def get_category_breakdown(db:Session):
    result = db.query(models.Transaction.category, func.sum(models.Transaction.amount).label("total"))\
               .group_by(models.Transaction.category).all()
    return [{"category":r[0],"total":r[1]}for r in result]
