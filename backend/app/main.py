from fastapi import FastAPI
from .api import user

app = FastAPI(title="Digital Asset Platform API")
app.include_router(user.router)
