from fastapi import FastAPI
from routes.points import point_router

app=FastAPI()
app.include_router(point_router)