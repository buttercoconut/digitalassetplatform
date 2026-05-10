from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from ..services.user_service import UserService

router = APIRouter(prefix="/user", tags=["user"])

class UserProfile(BaseModel):
    email: str
    full_name: str | None = None
    two_factor_enabled: bool = False

@router.get("/profile", response_model=UserProfile)
async def get_profile(user_service: UserService = Depends(UserService)):
    return user_service.get_profile()

@router.put("/profile", response_model=UserProfile)
async def update_profile(profile: UserProfile, user_service: UserService = Depends(UserService)):
    try:
        return user_service.update_profile(profile)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
