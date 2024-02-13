import logging
from beanie import init_beanie, Document
from pydantic import BaseModel
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient
from core.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from .mongodb import db
from beanie import init_beanie
    

async def connect_to_mongo():
    logging.info("mongo has started")
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)
    print(db)
    await init_beanie(database=db.client.food_shift, document_models=[])


async def close_mongo_connection():
    db.client.close()
    logging.info("mongodb closed ")