from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class Houses(BaseModel):
    id: int
    description: str
    price: str
    rooms: str
    area: str
    tax: str
    date: str
    user: int

    class Config:
        orm_mode = True