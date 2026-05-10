# services/user_service.py
from typing import List
from app.models.user import UserCreate, UserInDB, UserUpdate
from app.models.user import UserBase
from app.config import settings
import bcrypt

# In-memory store for demo purposes
_users: List[UserInDB] = []
_next_id = 1

async def create_user(user: UserCreate) -> UserInDB:
    global _next_id
    hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()
    new_user = UserInDB(
        id=_next_id,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed.decode(),
        is_active=True,
        is_superuser=False,
        created_at=None,
        updated_at=None,
    )
    _next_id += 1
    _users.append(new_user)
    return new_user

async def get_user_by_id(user_id: int) -> UserInDB | None:
    for u in _users:
        if u.id == user_id:
            return u
    return None

async def get_user_by_email(email: str) -> UserInDB | None:
    for u in _users:
        if u.email == email:
            return u
    return None

async def list_users() -> List[UserInDB]:
    return _users

async def update_user(user_id: int, data: UserUpdate) -> UserInDB | None:
    user = await get_user_by_id(user_id)
    if not user:
        return None
    if data.full_name is not None:
        user.full_name = data.full_name
    if data.password is not None:
        user.hashed_password = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt()).decode()
    return user
