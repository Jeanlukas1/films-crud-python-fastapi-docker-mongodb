from fastapi import FastAPI
from src.routes.film_route import router

app = FastAPI()
app.include_router(router)