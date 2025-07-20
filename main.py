from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=engine)

class User(BaseModel):
    name: str
    lastname: str
    age: int
    email: str

@app.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.Users).all()

@app.post("/user")
def add_user(user:User, db: Session = Depends(get_db)):
    model = models.Users()
    model.name = user.name
    model.lastname = user.lastname
    model.age = user.age
    model.email = user.email

    db.add(model)
    db.commit()

    return {"message": "User was added"}

@app.put("/{user_id}")
def update_user(user_id : int,user: User, db: Session = Depends(get_db)):
    model = db.query(models.Users).filter(models.Users.id == user_id).first()
    if model is None:
        raise HTTPException(status_code=404, detail="ID doesn't exist")

    model.name = user.name
    model.lastname = user.lastname
    model.age = user.age
    model.email = user.email

    db.add(model)
    db.commit()

    return {"message": "User was updated"}

@app.delete("/{user_id}")
def delete_user(user_id : int, db: Session = Depends(get_db)):
    model = db.query(models.Users).filter(models.Users.id == user_id).first()
    if model is None:
        raise HTTPException(status_code=404, detail="ID doesn't exist")

    db.query(models.Users).filter(models.Users.id == user_id).delete()
    db.commit()

    return {"message": "User was deleted"}

