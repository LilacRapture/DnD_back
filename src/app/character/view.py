from pydantic import BaseModel
from typing import Annotated
from fastapi import Depends

from src.app.spell.view import Spell
from src.business.domain.character.CharacterService import CharacterService


class CharacterClass(BaseModel):
    id: str
    name: str


class Character(BaseModel):
    id: str
    name: str
    character_class_name: CharacterClass  # id, name
    spells: list[Spell]


def character_handler(character_service: Annotated[CharacterService, Depends(CharacterService)]):
    return character_service.read_character()
