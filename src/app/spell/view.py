from typing import Annotated
from fastapi import Depends
from pydantic import BaseModel
from uuid import UUID
from automapper import mapper

from src.business.domain.spell.SpellService import SpellService


class Spell(BaseModel):
    id: UUID
    name: str


async def spell_handler(spell_id, spell_service: Annotated[SpellService, Depends(SpellService)]):
    spell = await spell_service.read_spell(spell_id)
    spell_dto: Spell = mapper.to(Spell).map(spell)

    return spell_dto
