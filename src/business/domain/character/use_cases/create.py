from mediatr import Mediator
from dependency_injector.wiring import Provide, inject

from src.app.utils.DiContainer import DiContainer
from src.business.domain.character.character import CharacterCreateDto
from src.infrastructure.data.DataService import DataService


class CreateCharacterRequest:
    character: CharacterCreateDto

    def __init__(self, character):
        self.character = character


@inject
async def create_character_handler(character: CharacterCreateDto,
                                   data_service: DataService = Provide[DiContainer.data_service_factory]):
    await data_service.create_character(character)


@Mediator.handler
def create_character_handler_wrapper(request: CreateCharacterRequest):
    return create_character_handler(request.character)
