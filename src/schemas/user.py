from pydantic import BaseModel


class CreateUser(BaseModel):
    name: str
    email: str

class UserInfo(BaseModel):
    id: int
    name: str
    email:str