from mediatr import Mediator
from dependency_injector.wiring import Provide, inject
from uuid import UUID

from src.app.utils.DiContainer import DiContainer
from src.infrastructure.data.DataService import DataService


class DeleteCharacterRequest:
    user_id: UUID
    character_id: UUID

    def __init__(self, user_id, character_id):
        self.user_id = user_id
        self.character_id = character_id


@inject
async def delete_character_handler(user_id: UUID,
                                   character_id: UUID,
                                   data_service: DataService = Provide[DiContainer.data_service_factory]):
    return await data_service.delete_character(user_id, character_id)


@Mediator.handler
def delete_character_handler_wrapper(request: DeleteCharacterRequest):
    return delete_character_handler(request.user_id, request.character_id)
