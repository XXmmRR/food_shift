from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from db.mongodb_utils import connect_to_mongo, close_mongo_connection


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


    return application


app = get_application()