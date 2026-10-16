from pydantic import BaseModel

class Room(BaseModel):
    id: int
    number: int
    note: str