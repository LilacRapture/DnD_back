from typing import Annotated
from fastapi import Depends
from pydantic import BaseModel
from uuid import UUID
from automapper import mapper

from src.business.domain.character.CharacterService import CharacterService


class Character(BaseModel):
    id: UUID
    name: str
    character_class_name: str


def map_character(character):
    return mapper.to(Character).map(character, fields_mapping={
        "character_class_name": character.character_class.name})


async def character_list_handler(character_service: Annotated[CharacterService, Depends(CharacterService)]):
    characters = await character_service.list_characters()
    characters_dtos = list(map(map_character, characters))
    return characters_dtos

