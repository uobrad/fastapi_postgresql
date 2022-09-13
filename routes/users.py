from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from database.models import *
from database.connection import get_db
from database.models import *
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database.schemas import *

from auth.hash_password import HashPassword
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token
import logging

user_router = APIRouter(
    tags=["User"],
)

hash_password = HashPassword()

@user_router.post("/signup")
async def add_user(user: CreateUserSchema, session: AsyncSession = Depends(get_db)):
    user=User(name=user.name, email=user.email, password=user.password, photo=user.photo, role=user.role)
    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password
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
@user_router.post("/signin")
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_db)):
    # user_exist = await User.find_one(User.email == user.username)
    # response_model = TokenResponse
    user_exist = (await session.execute(select(User).where(User.email == user.username))).scalar_one() #fetchone vraca listu, scalar vraca objekat sa atributom
    print(type(user_exist))





    # logging.warning(user_exist)
    # return user_exist
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist."
        )
    if hash_password.verify_hash(user.password, user_exist.password): #user_exist ne dohvata atribut password
        access_token = create_access_token(user_exist.email)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed."
    )