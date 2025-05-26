import os
from dotenv import load_dotenv

load_dotenv()

class Envs:
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DATABASE = os.getenv("POSTGRES_DB")
    
    POSTGRES_ASYNC_DB_URL = f"postgresql+asyncpg://{ POSTGRES_USER }:{ POSTGRES_PASSWORD }@{ POSTGRES_HOST }:{ POSTGRES_PORT }/{ POSTGRES_DATABASE }"
    
envs = Envs()
