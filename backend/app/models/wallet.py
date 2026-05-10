# models/wallet.py
from pydantic import BaseModel
from datetime import datetime

class WalletBase(BaseModel):
    user_id: int
    address: str
    balance: float = 0.0

class WalletCreate(WalletBase):
    pass

class WalletInDB(WalletBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
