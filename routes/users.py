from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from database.models import *
from database.connection import get_db
from database.models import *
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database.schemas import *

user_router = APIRouter(
    tags=["User"],
)

@user_router.post("/user")
async def add_song(user: CreateUserSchema, session: AsyncSession = Depends(get_db)):
    user=User(name=user.name, email=user.email, password=user.password, photo=user.photo, role=user.role)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
# @user_router.get("/test")
# async def test():
#     return {"test":"test"}
#
#
#
#
# @user_router.post("/signup")
# async def sign_user_up(user: CreateUserSchema) -> dict:
#     user_exist = await User.find_one(User.email == user.email)
#
#     if user_exist:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail="User with email provided exists already."
#         )
#     # await user_database.save(user)
#
#     return {
#         "message": "User created successfully"
#     }