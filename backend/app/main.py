# main.py
from fastapi import FastAPI
from app.api import user, wallet, transaction, asset
from app.services import user_service, wallet_service, transaction_service

app = FastAPI(title="Digital Asset Platform API")

# Include routers
app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(wallet.router, prefix="/api/wallets", tags=["wallets"])
app.include_router(transaction.router, prefix="/api/transactions", tags=["transactions"])
app.include_router(asset.router, prefix="/api/assets", tags=["assets"])

@app.get("/")
async def root():
    return {"message": "Welcome to Digital Asset Platform API"}
