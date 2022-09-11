from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from database.schemas import *
from database.models import *
from database.connection import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update

import logging


postv1_router = APIRouter(
    tags=["Posts"]
)


# @post_router.get("/posts/", response_model=List[PostResponse])
# async def get_all_posts(db: AsyncSession = Depends(async_session)):
#     return await db.execute(select(Post))
#
# @post_router.post("/posts")
# async def add_post(post: CreatePostSchema, session: AsyncSession = Depends(async_session)):
#     post = Post(title=post.title, content=post.content, category=post.category, image=post.image)
#     session.add(post)
#     await session.commit()
#     await session.refresh(post)
#     return post

@postv1_router.get("/")
async def retrieve_all_posts(session: AsyncSession = Depends(get_db)):
    result = await session.execute(select(Post))
    posts = result.scalars().all()
    return posts


@postv1_router.post("/post")
async def add_post(post: CreatePostSchema, session: AsyncSession = Depends(get_db)):
    post = Post(title=post.title, content=post.content, category=post.category, image=post.image, user_id=post.user_id)
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post

@postv1_router.put("/update/{id}")
async def update_post(id: int, body: UpdatePostSchema, session: AsyncSession = Depends(get_db)):
    current_post = await session.execute(update(Post).where(Post.id == id).values(
        title=body.title, content=body.content, category=body.category, image=body.image
    ))

    await session.commit()
    await session.refresh(current_post)
    return current_post


@postv1_router.delete("/post/{id}")
async def delete_post(id: int, session: AsyncSession = Depends(get_db)):
    current_post = await session.get(Post, id)
    # logging.warning(current_post)
    await session.delete(current_post)
    # await session.refresh(current_post)
    await session.commit()
    return "Post je izbrisan"



@postv1_router.get("/post/{id}")
async def update_post(id: int, session: AsyncSession = Depends(get_db)):
    result = await session.get(Post, id)
    return result




#
# @postv1_router.get("/{id}")
# async def retrieve_event(session: AsyncSession = Depends(async_session)):
#     post = await session.get(id)
#     if not post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Event with supplied ID does not exist"
#         )
#     return post


