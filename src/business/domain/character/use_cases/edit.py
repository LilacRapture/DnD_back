from mediatr import Mediator
from dependency_injector.wiring import Provide, inject

from src.app.utils.DiContainer import DiContainer
from src.business.domain.character.character import CharacterEditDto
from src.infrastructure.data.DataService import DataService


class EditCharacterRequest:
    character: CharacterEditDto

    def __init__(self, character):
        self.character = character


@inject
async def edit_character_handler(character: CharacterEditDto,
                                 data_service: DataService = Provide[DiContainer.data_service_factory]):
    await data_service.edit_character(character)


@Mediator.handler
def edit_character_handler_wrapper(request: EditCharacterRequest):
    return edit_character_handler(request.character)
