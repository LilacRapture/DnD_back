from automapper import mapper
from mediatr import Mediator
from dependency_injector.wiring import Provide, inject
from uuid import UUID

from src.app.utils.DiContainer import DiContainer
from src.business.domain.character.character import Character, CharacterClass
from src.business.domain.spell.spell import Spell
from src.infrastructure.data.DataService import DataService


class ReadCharacterRequest:
    user_id: UUID
    character_id: UUID

    def __init__(self, user_id, character_id):
        self.user_id = user_id
        self.character_id = character_id


@inject
async def read_character_handler(user_id: UUID,
                                 character_id: UUID,
                                 data_service: DataService = Provide[DiContainer.data_service_factory]):
    db_character = await data_service.read_character(user_id, character_id)
    if db_character is None:
        return None

    character: Character = mapper.to(Character).map(db_character, fields_mapping={
        "character_class": mapper.to(CharacterClass).map(db_character.character_class)})
    character.spells = list(map(lambda spell: mapper.to(Spell).map(spell), db_character.spells))

    return character


@Mediator.handler
def read_character_handler_wrapper(request: ReadCharacterRequest):
    user_id = UUID(request.user_id)
    character_id = UUID(request.character_id)
    character = read_character_handler(user_id, character_id)
    return character

