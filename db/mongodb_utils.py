import logging
from beanie import init_beanie, Document
from pydantic import BaseModel
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from .mongodb import db
from beanie import init_beanie
from db.models import Address, Institution, User, Food, Tag, Rating
from core.config import CONFIG


async def connect_to_mongo():
    logging.info("mongo has started")
    db.client = AsyncIOMotorClient(str(CONFIG.MONGODB_URL),
                                   maxPoolSize=CONFIG.MAX_CONNECTIONS_COUNT,
                                   minPoolSize=CONFIG.MIN_CONNECTIONS_COUNT)
    await init_beanie(database=db.client.food_shift, document_models=[
                                                                Address,
                                                                User,
                                                                Food,
                                                                Tag,
                                                                Rating,
                                                                Institution
        ])


async def close_mongo_connection():
    db.client.close()
    logging.info("mongodb closed ")