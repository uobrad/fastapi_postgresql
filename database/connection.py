from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import settings

DATABASE_URL = f"postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.DATABASE_PORT}/{settings.POSTGRES_DB}"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()