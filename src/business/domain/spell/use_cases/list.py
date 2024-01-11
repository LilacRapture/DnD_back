from automapper import mapper
from mediatr import Mediator
from dependency_injector.wiring import Provide, inject

from src.app.utils.DiContainer import DiContainer
from src.business.domain.spell.spell import Spell
from src.infrastructure.data.DataService import DataService


class ListSpellsRequest:
    pass


@inject
async def list_spells_handler(data_service: DataService = Provide[DiContainer.data_service_factory]):
    db_spells = await data_service.list_spells()
    spells = list(map(lambda spell:
                      mapper.to(Spell).map(spell), db_spells))

    return spells


@Mediator.handler
def list_spells_handler_wrapper(request: ListSpellsRequest):
    return list_spells_handler()
