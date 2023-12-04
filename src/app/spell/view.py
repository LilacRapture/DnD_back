from typing import Annotated
from fastapi import Depends
from pydantic import BaseModel
from uuid import UUID

from src.business.domain.spell.SpellService import SpellService


class Spell(BaseModel):
    id: UUID
    name: str


def spell_handler(spell_id, spell_service: Annotated[SpellService, Depends(SpellService)]):
    spell = spell_service.read_spell(spell_id)
    spell_dto = Spell(id=spell.id, name=spell.name)
    return spell_dto
