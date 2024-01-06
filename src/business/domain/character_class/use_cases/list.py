from automapper import mapper
from mediatr import Mediator
from dependency_injector.wiring import Provide, inject

from src.app.utils.DiContainer import DiContainer
from src.business.domain.character_class.CharacterClass import CharacterClass
from src.infrastructure.data.DataService import DataService


class ListCharacterClassesRequest:
    pass


@inject
async def list_character_classes_handler(data_service: DataService = Provide[DiContainer.data_service_factory]):
    db_character_classes = await data_service.list_character_classes()
    character_classes = list(map(lambda character_class:
                                 mapper.to(CharacterClass).map(character_class), db_character_classes))

    return character_classes


@Mediator.handler
def list_character_classes_handler_wrapper(request: ListCharacterClassesRequest):
    print('hello')
    return list_character_classes_handler()
