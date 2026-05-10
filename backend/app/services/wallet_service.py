# services/wallet_service.py
from typing import List
from app.models.wallet import WalletCreate, WalletInDB

_wallets: List[WalletInDB] = []
_next_id = 1

async def create_wallet(wallet: WalletCreate) -> WalletInDB:
    global _next_id
    new_wallet = WalletInDB(
        id=_next_id,
        user_id=wallet.user_id,
        address=wallet.address,
        balance=wallet.balance,
        created_at=None,
        updated_at=None,
    )
    _next_id += 1
    _wallets.append(new_wallet)
    return new_wallet

async def get_wallet_by_id(wallet_id: int) -> WalletInDB | None:
    for w in _wallets:
        if w.id == wallet_id:
            return w
    return None

async def list_wallets() -> List[WalletInDB]:
    return _wallets

async def update_balance(wallet_id: int, amount: float) -> WalletInDB | None:
    wallet = await get_wallet_by_id(wallet_id)
    if not wallet:
        return None
    wallet.balance += amount
    return wallet
