from pydantic import BaseModel
from domain.models.users import User

class UserCreateDTO(BaseModel):
    name: str
    email: str
    password: str

class UserResponseDTO(User):
    pass