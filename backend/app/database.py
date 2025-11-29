# backend/app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:mahdia14@localhost:5432/MyWallet"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import os

# DATABASE_URL = os.getenv(
#     "DATABASE_URL",
#     "postgresql+psycopg2://postgres:mahdia14@localhost:5432/MyWallet"
# )

# engine = create_engine(DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(bind=engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
