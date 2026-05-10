# services/transaction_service.py
from typing import List
from app.models.transaction import TransactionCreate, TransactionInDB

_transactions: List[TransactionInDB] = []
_next_id = 1

async def create_transaction(tx: TransactionCreate) -> TransactionInDB:
    global _next_id
    new_tx = TransactionInDB(
        id=_next_id,
        wallet_id=tx.wallet_id,
        asset_id=tx.asset_id,
        amount=tx.amount,
        tx_hash=tx.tx_hash,
        status=tx.status,
        created_at=None,
        updated_at=None,
    )
    _next_id += 1
    _transactions.append(new_tx)
    return new_tx

async def get_transaction_by_id(tx_id: int) -> TransactionInDB | None:
    for t in _transactions:
        if t.id == tx_id:
            return t
    return None

async def list_transactions() -> List[TransactionInDB]:
    return _transactions

async def update_status(tx_id: int, status: str) -> TransactionInDB | None:
    tx = await get_transaction_by_id(tx_id)
    if not tx:
        return None
    tx.status = status
    return tx
