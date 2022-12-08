from fastapi import APIRouter
from models.points import Point
from config.database import connection
from schemas.points import pointEntity, listOfPointEntity

point_router = APIRouter()

@point_router.get('/points')
async def find_all_points():
    return listOfPointEntity(connection.local.point.find())