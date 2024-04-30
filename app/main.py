from fastapi import FastAPI
from .routers import cars_view


app = FastAPI()
app.include_router(cars_view.router)