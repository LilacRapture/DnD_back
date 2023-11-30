from typing import Annotated
from fastapi import Depends
from pydantic import BaseModel

from src.business.domain.spell.SpellService import SpellService


class Spell(BaseModel):
    id: str
    name: str


def spell_handler(spell_service: Annotated[SpellService, Depends(SpellService)]):
    return spell_service.read_spell()
