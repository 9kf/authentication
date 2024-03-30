from pydantic import BaseModel
from datetime import datetime

class UserResponse(BaseModel):
    user_id: str
    username: str
    email: str
    first_name: str
    last_name: str
    profile_picture: str
    created_at: datetime
    updated_at: datetime

class UserForm(BaseModel):
    username: str
    email: str
    password: str