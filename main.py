from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from db.mongodb_utils import connect_to_mongo, close_mongo_connection
from api.routes.user.auth import router as AuthRouter
from api.routes.user.mail import router as MailRouter
from api.routes.user.register import router as RegisterRouter
from api.routes.user.user import router as UserRouter
from api.routes.institutions.institution import router as InstitutionRouter
from api.routes.user.address import router as AddressRouter
from api.routes.institutions.tags import router as TagRouter
from api.routes.user.favorites import router as FavoriteRouter
from api.routes.institutions.food import router as FoodRouter
from api.routes.institutions.category import router as CategoryRouter
from api.routes.institutions.rating import router as RatingRouter
from api.routes.chats.chat import router as ChatRouter
from api.routes.metrics.health_check import router as HealthRouter
from api.routes.institutions.order import router as OrderRouter
from prometheus_fastapi_instrumentator import Instrumentator
from loguru import logger



def get_application() -> FastAPI:
    logger.info("App started")
    application = FastAPI()

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler("startup", connect_to_mongo)
    application.add_event_handler("shutdown", close_mongo_connection)
    application.include_router(AuthRouter, prefix='api/v1')
    application.include_router(MailRouter, prefix='api/v1')
    application.include_router(RegisterRouter, prefix='api/v1')
    application.include_router(UserRouter, prefix='api/v1')
    application.include_router(InstitutionRouter, prefix='api/v1')
    application.include_router(TagRouter, prefix='api/v1')
    application.include_router(AddressRouter, prefix='api/v1')
    application.include_router(FavoriteRouter, prefix='api/v1')
    application.include_router(FoodRouter, prefix='api/v1')
    application.include_router(CategoryRouter, prefix='api/v1')
    application.include_router(RatingRouter, prefix='api/v1')
    application.include_router(ChatRouter, prefix='api/v1')
    application.include_router(HealthRouter, prefix='api/v1')
    application.include_router(OrderRouter, prefix='api/v1')
    Instrumentator().instrument(application).expose(application)
    return application


app = get_application()
