from mediatr import Mediator
from dependency_injector.wiring import Provide, inject
from uuid import UUID

from src.app.utils.DiContainer import DiContainer
from src.infrastructure.data.DataService import DataService


class DeleteSpellFromCharacterRequest:
    character_id: UUID
    spell_id: UUID

    def __init__(self, character_id, spell_id):
        self.character_id = character_id
        self.spell_id = spell_id


@inject
async def delete_spell_from_character_handler(character_id: UUID,
                                              spell_id: UUID,
                                              data_service: DataService = Provide[DiContainer.data_service_factory]):
    return await data_service.delete_spell_from_character(character_id, spell_id)


@Mediator.handler
def delete_spell_from_character_handler_wrapper(request: DeleteSpellFromCharacterRequest):
    # character_id = UUID(request.character_id)
    # spell_id = UUID(request.spell_id)
    return delete_spell_from_character_handler(request.character_id, request.spell_id)
