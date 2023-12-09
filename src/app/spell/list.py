from typing import Annotated
from fastapi import Depends
from pydantic import BaseModel
from uuid import UUID
from automapper import mapper

from src.business.domain.spell.SpellService import SpellService


class Spell(BaseModel):
    id: UUID
    name: str


def spell_list_handler(spell_service: Annotated[SpellService, Depends(SpellService)]):
    spells = spell_service.list_spells()
    spell_dtos = list(map(lambda spell: mapper.to(Spell).map(spell), spells))
    return spell_dtos
