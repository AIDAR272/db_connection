from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import engine, SessionLocal
import models


async def get_db():
    async with SessionLocal() as session:
        yield session

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

    yield
app = FastAPI(lifespan=lifespan)

class User(BaseModel):
    name: str
    lastname: str
    age: int
    email: str

@app.get("/")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Users))
    users = result.scalars().all()
    return users

@app.post("/user")
async def add_user(user:User, db: AsyncSession = Depends(get_db)):
    model = models.Users(**user.dict())
    db.add(model)
    await db.commit()

    return {"message": "User was added"}

@app.put("/{user_id}")
async def update_user(user_id : int,user: User, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Users).where(models.Users.id == user_id))
    model = result.scalar_one_or_none()
    if model is None:
        raise HTTPException(status_code=404, detail="ID doesn't exist")

    model.name = user.name
    model.lastname = user.lastname
    model.age = user.age
    model.email = user.email
    await db.commit()

    return {"message": "User was updated"}

@app.delete("/{user_id}")
async def delete_user(user_id : int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Users).where(models.Users.id == user_id))
    model = result.scalar_one_or_none()
    if model is None:
        raise HTTPException(status_code=404, detail="ID doesn't exist")

    await db.delete(model)
    await db.commit()

    return {"message": "User was deleted"}
