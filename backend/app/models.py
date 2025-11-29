# backend/app/models.py

import uuid
from sqlalchemy import Column, String, Boolean, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=True)
    password_hash = Column(Text, nullable=False)

    is_verified = Column(Boolean, nullable=False, default=False)
    verification_token = Column(Text, nullable=True)
    verification_token_expires = Column(TIMESTAMP, nullable=True)

    two_factor_enabled = Column(Boolean, nullable=False, default=False)
    two_factor_secret = Column(Text, nullable=True)

    provider = Column(String(20), nullable=False, default='local')

    avatar_url = Column(Text, nullable=True)
    preferred_currency = Column(String(10), nullable=False, default='USD')
    language = Column(String(10), nullable=False, default='en')

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
