# api/user.py
from fastapi import APIRouter, Depends, HTTPException, status
from app.models.user import UserCreate, UserInDB, UserUpdate
from app.services.user_service import create_user, get_user_by_id, list_users, update_user

router = APIRouter()

@router.post("/", response_model=UserInDB)
async def register_user(user: UserCreate):
    existing = await get_user_by_email(user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await create_user(user)

@router.get("/", response_model=list[UserInDB])
async def read_users():
    return await list_users()

@router.get("/{user_id}", response_model=UserInDB)
async def read_user(user_id: int):
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserInDB)
async def update_user_info(user_id: int, data: UserUpdate):
    user = await update_user(user_id, data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
