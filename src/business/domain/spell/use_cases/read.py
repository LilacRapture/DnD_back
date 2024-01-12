from automapper import mapper
from mediatr import Mediator
from dependency_injector.wiring import Provide, inject
from uuid import UUID

from src.app.utils.DiContainer import DiContainer
from src.business.domain.spell.spell import Spell
from src.infrastructure.data.DataService import DataService


class ReadSpellRequest:
    spell_id: UUID

    def __init__(self, spell_id):
        self.spell_id = spell_id


@inject
async def read_spell_handler(spell_id: UUID,
                             data_service: DataService = Provide[DiContainer.data_service_factory]):
    db_spell = await data_service.read_spell(spell_id)
    spell: Spell = mapper.to(Spell).map(db_spell)

    return spell


@Mediator.handler
def read_spell_handler_wrapper(request: ReadSpellRequest):
    return read_spell_handler(request.spell_id)
