from mediatr import Mediator
from dependency_injector.wiring import Provide, inject

from src.app.utils.DiContainer import DiContainer
from src.infrastructure.data.DataService import DataService


class CreateUserRequest:
    pass


@inject
async def create_user_handler(data_service: DataService = Provide[DiContainer.data_service_factory]):
    return await data_service.create_user()


@Mediator.handler
def create_user_handler_wrapper(request: CreateUserRequest):
    return create_user_handler()
