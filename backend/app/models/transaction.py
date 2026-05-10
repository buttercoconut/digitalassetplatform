# models/transaction.py
from pydantic import BaseModel
from datetime import datetime

class TransactionBase(BaseModel):
    wallet_id: int
    asset_id: int
    amount: float
    tx_hash: str | None = None
    status: str = "pending"

class TransactionCreate(TransactionBase):
    pass

class TransactionInDB(TransactionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
