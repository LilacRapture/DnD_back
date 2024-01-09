from automapper import mapper
from mediatr import Mediator
from dependency_injector.wiring import Provide, inject
from uuid import UUID

from src.app.utils.DiContainer import DiContainer
from src.business.domain.character.character import Character, CharacterClass
from src.infrastructure.data.DataService import DataService


class ListCharactersRequest:
    def __init__(self, id):
        self.user_id = id


@inject
async def list_characters_handler(user_id: UUID,
                                  data_service: DataService = Provide[DiContainer.data_service_factory]):
    db_characters = await data_service.list_characters(user_id)

    # characters = []
    # for db_character in db_characters:
    #     character: Character = mapper.to(Character).map(db_character, fields_mapping={
    #         "character_class": mapper.to(CharacterClass).map(db_character.character_class)
    #     })
    #     characters.append(character)
    characters = list(map(lambda character: mapper.to(Character).map(character, fields_mapping={
            "character_class": mapper.to(CharacterClass).map(character.character_class)
        }), db_characters))

    return characters


@Mediator.handler
def list_characters_handler_wrapper(request: ListCharactersRequest):
    user_id = UUID(request.user_id)
    characters = list_characters_handler(user_id)
    return characters
