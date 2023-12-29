from pydantic import BaseModel

class AddBody(BaseModel):
    x: int
    y: int