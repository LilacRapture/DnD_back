from mediatr import Mediator
from dependency_injector.wiring import Provide, inject
from uuid import UUID

from src.app.utils.DiContainer import DiContainer
from src.infrastructure.data.DataService import DataService


class AddSpellToCharacterRequest:
    character_id: UUID
    spell_id: UUID

    def __init__(self, character_id, spell_id):
        self.character_id = character_id
        self.spell_id = spell_id


@inject
async def add_spell_to_character_handler(character_id: UUID,
                                         spell_id: UUID,
                                         data_service: DataService = Provide[DiContainer.data_service_factory]):
    return await data_service.add_spell_to_character(character_id, spell_id)


@Mediator.handler
def add_spell_to_character_handler_wrapper(request: AddSpellToCharacterRequest):
    return add_spell_to_character_handler(request.character_id, request.spell_id)
