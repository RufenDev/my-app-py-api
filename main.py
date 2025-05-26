from fastapi import FastAPI
from api.routes import router as routes_api
#from fastapi.middleware.cors import CORSMiddleware

API_PREFIX = "/api/v1"

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=envs.CORS_ORIGINS,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(routes_api, prefix=API_PREFIX)
