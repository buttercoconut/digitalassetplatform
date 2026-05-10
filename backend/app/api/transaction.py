# api/transaction.py
from fastapi import APIRouter, HTTPException
from app.models.transaction import TransactionCreate, TransactionInDB
from app.services.transaction_service import create_transaction, get_transaction_by_id, list_transactions, update_status

router = APIRouter()

@router.post("/", response_model=TransactionInDB)
async def create_new_transaction(tx: TransactionCreate):
    return await create_transaction(tx)

@router.get("/", response_model=list[TransactionInDB])
async def read_transactions():
    return await list_transactions()

@router.get("/{tx_id}", response_model=TransactionInDB)
async def read_transaction(tx_id: int):
    tx = await get_transaction_by_id(tx_id)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx

@router.put("/{tx_id}/status", response_model=TransactionInDB)
async def update_tx_status(tx_id: int, status: str):
    tx = await update_status(tx_id, status)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx
