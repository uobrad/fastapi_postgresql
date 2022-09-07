import uuid
from database.connection import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    name = Column(String,  nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    photo = Column(String, nullable=True)
    verified = Column(Boolean, nullable=False, server_default='False')
    verification_code = Column(String, nullable=True, unique=True)
    role = Column(String, server_default='user', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))


class Post(Base):
    __tablename__ = 'posts'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    category = Column(String, nullable=False)
    image = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    user = relationship('User')

# from typing import Optional, List
#
# from sqlmodel import SQLModel, Field, Relationship

from database.connection import Base


# class SongBase(SQLModel):
#     name: str
#     artist: str
#     year: Optional[int] = None


# class Song(SongBase, table=True):
#     id: int = Field(default=None, primary_key=True)


# class SongCreate(SongBase):
#     pass

# class UserBase(SQLModel):
#     name: str = Field(index=True)
#     password: str
#     age: Optional[int] = Field(default=None, index=True)
#
# class User(UserBase, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#
#     posts: List["Post"] = Relationship(back_populates="user")
#
#
# class UserCreate(UserBase):
#     pass
#
#
# class UserRead(UserBase):
#     id: int
#
# class UserUpdate(SQLModel):
#     name: Optional[str] = None
#     secret_name: Optional[str] = None
#     age: Optional[int] = None
#
# class PostBase(SQLModel):
#     title: str = Field(index=True)
#     content: str
#     category: str = Field(index=True)
#
#     user_id: Optional[int] = Field(default=None, foreign_key="user.id")
#
#
# class Post(PostBase, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#
#     user: Optional[User] = Relationship(back_populates="posts")
#
#
# class PostCreate(PostBase):
#     pass
#
#
# class PostRead(PostBase):
#     id: int
#
#
# class PostUpdate(SQLModel):
#     name: Optional[str] = None
#     headquarters: Optional[str] = None