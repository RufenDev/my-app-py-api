import os
from dotenv import load_dotenv

load_dotenv()

class Envs:
    POSGRES_DB_URL = os.getenv("POSGRES_DB_URL")
    
envs = Envs()
