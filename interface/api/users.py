from fastapi import APIRouter, Depends, status
from application.service.user_service import UserService
from interface.dependencies import get_user_service
from interface.schema.users import UserCreateSchema

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreateSchema,
    service: UserService = Depends(get_user_service)
):
    user = service.create_user(user_data)
    return user