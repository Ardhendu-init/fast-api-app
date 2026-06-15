from fastapi import APIRouter, HTTPException
from app.models import UserCreate
from app.database import users_collection

router = APIRouter()


@router.post("/users", status_code=201)
async def create_user(user: UserCreate):
    existing = await users_collection.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=409, detail="A user with this email already exists")

    result = await users_collection.insert_one(user.model_dump())
    return {"id": str(result.inserted_id)}
