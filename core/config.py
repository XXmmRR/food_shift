from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv('MONGODB_URL')
MIN_CONNECTIONS_COUNT = os.getenv('MIN_CONNECTIONS_COUNT')
MAX_CONNECTIONS_COUNT= os.getenv('MAX_CONNECTIONS_COUNT')

SECRET_KEY = os.getenv('SECRET_KEY')

