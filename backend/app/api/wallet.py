# api/wallet.py
from fastapi import APIRouter, HTTPException
from app.models.wallet import WalletCreate, WalletInDB
from app.services.wallet_service import create_wallet, get_wallet_by_id, list_wallets, update_balance

router = APIRouter()

@router.post("/", response_model=WalletInDB)
async def create_new_wallet(wallet: WalletCreate):
    return await create_wallet(wallet)

@router.get("/", response_model=list[WalletInDB])
async def read_wallets():
    return await list_wallets()

@router.get("/{wallet_id}", response_model=WalletInDB)
async def read_wallet(wallet_id: int):
    wallet = await get_wallet_by_id(wallet_id)
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet

@router.put("/{wallet_id}/balance", response_model=WalletInDB)
async def update_wallet_balance(wallet_id: int, amount: float):
    wallet = await update_balance(wallet_id, amount)
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet
