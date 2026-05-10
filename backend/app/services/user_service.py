from pydantic import BaseModel

class UserProfile(BaseModel):
    email: str
    full_name: str | None = None
    two_factor_enabled: bool = False
