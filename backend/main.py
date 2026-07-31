from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine, SessionLocal
from models import User
from schemas import UserCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

"""post and get user"""
@app.post("/login")
def login(user: UserCreate):
    

    """post logic"""
    
    db.add(new_user)
    db.commit()
    return {"message": "Inserted Successfully"}

@app.get("/users")
def get_users():
    db = SessionLocal()

    """get logic"""
    
    
    return users


"""update user"""

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate):
    db = SessionLocal()

    """update logic"""

    db.commit()

    return {"message": "User Updated Successfully"}




"""delete user"""

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()

    """delete logic"""
    db.commit()

    return {"message": "User Deleted Successfully"}