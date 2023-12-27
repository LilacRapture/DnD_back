from pydantic import BaseModel
from typing import Annotated
from fastapi import Depends
from uuid import UUID
from automapper import mapper

from src.app.spell.view import Spell
from src.business.domain.character.CharacterService import CharacterService
from src.business.domain.character.character import Character as CharacterModel


class CharacterClass(BaseModel):
    id: UUID
    name: str


class Character(BaseModel):
    id: UUID
    name: str
    character_class: CharacterClass  # id, name
    spells: list[Spell]


def create_fields_mapping(character: CharacterModel):
    return {"character_class": {"id": character.character_class.id, "name": character.character_class.name},
            "spells": list(map(lambda spell: {"id": spell.id, "name": spell.name}, character.spells))}


async def character_handler(character_id,
                            character_service: Annotated[CharacterService, Depends(CharacterService)],):
    character = await character_service.read_character(character_id)
    if character is None:
        return None

    character_dto: Character = mapper.to(Character).map(character, fields_mapping=create_fields_mapping(character))
    return character_dto
