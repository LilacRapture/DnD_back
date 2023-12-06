from typing import Annotated
from fastapi import Depends
from pydantic import BaseModel
from uuid import UUID
from automapper import mapper
import json

from src.business.domain.character.CharacterService import CharacterService


class Character(BaseModel):
    id: UUID
    name: str
    character_class_name: str


def character_list_handler(character_service: Annotated[CharacterService, Depends(CharacterService)]):
    characters = character_service.list_characters()
    characters_dtos = map(lambda db_character: mapper.to(Character).map(db_character), characters)
    # characters_dtos = []
    # for character in character_service.list_characters():  # those are not dtos?
    #     character = Character(id=character.id, name=character.name,
    #                           character_class_name=character.character_class.name)
    #     characters_dtos.append(character)
    return characters_dtos

