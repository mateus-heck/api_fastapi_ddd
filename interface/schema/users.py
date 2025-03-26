from pydantic import BaseModel, EmailStr

class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True