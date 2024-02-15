from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from db.mongodb_utils import connect_to_mongo, close_mongo_connection
from api.routes.user.auth import router as AuthRouter
from api.routes.user.mail import router as MailRouter
from api.routes.user.register import router as RegisterRouter
from api.routes.user.user import router as UserRouter

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
    return application


app = get_application()