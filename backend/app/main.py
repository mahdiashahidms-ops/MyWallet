# backend/app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from . import users       # functions from users.py
from . import models, schemas
from .database import engine, get_db


app = FastAPI(title="MyWallet API")

'''# Link to frontend files
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

class UserRegistration(BaseModel):
    first_name: str
    last_name: str
    email: str
    birth_date: str
    state: str | None = None
    city: str | None = None
    zip_code: str | None = None
    phone: str | None = None'''


# -----------------------------
# Create database tables on startup (SYNC)
# -----------------------------
@app.on_event("startup")
def startup_event():
    models.Base.metadata.create_all(bind=engine)


# -----------------------------
# Root endpoint
# -----------------------------
@app.get("/")
def root():
    return {"message": "MyWallet API is running"}


# -----------------------------
# Create a new user
# -----------------------------
@app.post("/users/", response_model=schemas.UserRead)
def create_user_endpoint(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    try:
        return users.create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# -----------------------------
# Get all users
# -----------------------------
@app.get("/users/", response_model=List[schemas.UserRead])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


# -----------------------------
# Get a user by ID
# -----------------------------
@app.get("/users/{user_id}", response_model=schemas.UserRead)
def get_user(user_id: UUID, db: Session = Depends(get_db)):
    user = users.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# -----------------------------
# Update a user
# -----------------------------
@app.put("/users/{user_id}", response_model=schemas.UserRead)
def update_user(
    user_id: UUID,
    user_update: schemas.UserUpdate,
    db: Session = Depends(get_db)
):
    user = users.update_user(db, user_id, user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# -----------------------------
# Delete a user
# -----------------------------
@app.delete("/users/{user_id}")
def delete_user(user_id: UUID, db: Session = Depends(get_db)):
    success = users.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}

# -----------------------------
'''
@app.get("/register", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
async def register_user(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    birth_date: str = Form(...),
    state: str = Form(""),
    city: str = Form(""),
    zip_code: str = Form(""),
    phone: str = Form("")
):
    user = UserRegistration(
        first_name=first_name,
        last_name=last_name,
        email=email,
        birth_date=birth_date,
        state=state,
        city=city,
        zip_code=zip_code,
        phone=phone,
    )

    # Save to DB if needed

    return {"message": "User registered", "data": user.dict()}
'''