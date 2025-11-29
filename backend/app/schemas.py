# backend/app/schemas.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: Optional[str] = None
    provider: Optional[str] = "local"
    preferred_currency: Optional[str] = "USD"
    language: Optional[str] = "en"

class UserCreate(UserBase):
    password_hash: str  # hashed password

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    preferred_currency: Optional[str] = None
    language: Optional[str] = None

class UserRead(UserBase):
    id: UUID
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
