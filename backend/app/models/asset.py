# models/asset.py
from pydantic import BaseModel

class AssetBase(BaseModel):
    symbol: str
    name: str
    decimals: int

class AssetCreate(AssetBase):
    pass

class AssetInDB(AssetBase):
    id: int

    class Config:
        orm_mode = True
