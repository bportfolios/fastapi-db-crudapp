from pydantic import BaseModel

class Point(BaseModel):
    point_time:str
    point_value: str