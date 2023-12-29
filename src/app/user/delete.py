from typing import Annotated
from fastapi import Depends
from uuid import UUID

from src.business.domain.user.UserService import UserService


async def user_delete_handler(user_id: UUID,
                              user_service: Annotated[UserService, Depends(UserService)]):
    await user_service.delete_user(user_id)
