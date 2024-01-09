from mediatr import Mediator
from dependency_injector.wiring import Provide, inject
from uuid import UUID

from src.app.utils.DiContainer import DiContainer
from src.infrastructure.data.DataService import DataService


class DeleteUserRequest:
    user_id: UUID

    def __init__(self, id):
        self.user_id = id


@inject
async def delete_user_handler(user_id: UUID,
                              data_service: DataService = Provide[DiContainer.data_service_factory]):
    return await data_service.delete_user(user_id)


@Mediator.handler
def delete_user_handler_wrapper(request: DeleteUserRequest):
    return delete_user_handler(request.user_id)
