from pydantic import BaseModel
from typing import Annotated, Optional
from fastapi import Depends
from uuid import UUID, uuid4

from src.business.domain.user.UserService import UserService


class UserDto(BaseModel):
    token: str


async def user_create_handler(user_service: Annotated[UserService, Depends(UserService)]):
    user_id = await user_service.create_user()
    user = UserDto(token=str(user_id))
    print(user)
    return user
