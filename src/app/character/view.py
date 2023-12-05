from pydantic import BaseModel
from typing import Annotated
from fastapi import Depends
from uuid import UUID

from src.app.spell.view import Spell
from src.business.domain.character.CharacterService import CharacterService


class CharacterClass(BaseModel):
    id: UUID
    name: str


class Character(BaseModel):
    id: UUID
    name: str
    character_class: CharacterClass  # id, name
    spells: list[Spell]


def character_handler(character_id, character_service: Annotated[CharacterService, Depends(CharacterService)]):
    character = character_service.read_character(character_id)
    spells = []
    for character_spell in character.spells:
        spell = Spell(id=character_spell.id, name=character_spell.name)
        spells.append(spell)
    character_dto = Character(id=character.id,
                              name=character.name,
                              character_class=CharacterClass(id=character.character_class.id,
                                                             name=character.character_class.name),
                              spells=spells)
    return character_dto
