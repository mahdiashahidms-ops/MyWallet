# backend/app/users.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from .models import User
from .schemas import UserCreate, UserUpdate
from typing import Optional
from uuid import UUID

# CREATE USER
def create_user(db: Session, user: UserCreate) -> User:
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        phone_number=user.phone_number,
        password_hash=user.password_hash,
        provider=user.provider or "local",
        preferred_currency=user.preferred_currency or "USD",
        language=user.language or "en"
    )

    db.add(new_user)

    try:
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        raise ValueError("Email already exists")


# GET USER BY ID
def get_user_by_id(db: Session, user_id: UUID) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


# GET USER BY EMAIL
def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


# UPDATE USER
def update_user(db: Session, user_id: UUID, user_update: UserUpdate) -> Optional[User]:
    existing_user = get_user_by_id(db, user_id)
    if not existing_user:
        return None

    for k, v in user_update.dict(exclude_unset=True).items():
        setattr(existing_user, k, v)

    db.commit()
    db.refresh(existing_user)
    return existing_user


# DELETE USER
def delete_user(db: Session, user_id: UUID) -> bool:
    user = get_user_by_id(db, user_id)
    if not user:
        return False

    db.delete(user)
    db.commit()
    return True


# backend/app/users.py

# from sqlalchemy.orm import Session
# from sqlalchemy.exc import IntegrityError
# from sqlalchemy import update, delete
# from typing import Optional
# from uuid import UUID
# from .models import User
# from .schemas import UserCreate, UserUpdate

# # ---------------------------
# # CREATE USER
# # ---------------------------
# def create_user(db: Session, user: UserCreate) -> User:
#     new_user = User(
#         first_name=user.first_name,
#         last_name=user.last_name,
#         email=user.email,
#         phone_number=user.phone_number,
#         password_hash=user.password_hash,
#         provider=user.provider or "local",
#         preferred_currency=user.preferred_currency or "USD",
#         language=user.language or "en"
#     )
#     db.add(new_user)
#     try:
#         db.commit()
#         db.refresh(new_user)
#         return new_user
#     except IntegrityError:
#         db.rollback()
#         raise ValueError("Email already exists")


# # ---------------------------
# # GET USER BY ID
# # ---------------------------
# def get_user_by_id(db: Session, user_id: UUID) -> Optional[User]:
#     return db.query(User).filter(User.id == user_id).first()


# # ---------------------------
# # GET USER BY EMAIL
# # ---------------------------
# def get_user_by_email(db: Session, email: str) -> Optional[User]:
#     return db.query(User).filter(User.email == email).first()


# # ---------------------------
# # UPDATE USER
# # ---------------------------
# def update_user(db: Session, user_id: UUID, user_update: UserUpdate) -> Optional[User]:
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         return None
#     for key, value in user_update.dict(exclude_unset=True).items():
#         setattr(user, key, value)
#     db.commit()
#     db.refresh(user)
#     return user


# # ---------------------------
# # DELETE USER
# # ---------------------------
# def delete_user(db: Session, user_id: UUID) -> bool:
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         return False
#     db.delete(user)
#     db.commit()
#     return True
