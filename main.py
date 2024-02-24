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


def get_application() -> FastAPI:

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
    application.include_router(AuthRouter)
    application.include_router(MailRouter)
    application.include_router(RegisterRouter)
    application.include_router(UserRouter)
    application.include_router(InstitutionRouter)
    application.include_router(TagRouter)
    application.include_router(AddressRouter)
    application.include_router(FavoriteRouter)
    application.include_router(FoodRouter)
    application.include_router(CategoryRouter)
    application.include_router(RatingRouter)
    application.include_router(ChatRouter)
    application.include_router(HealthRouter)
    return application


app = get_application()
