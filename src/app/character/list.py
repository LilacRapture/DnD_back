from typing import Annotated
from fastapi import Depends
from pydantic import BaseModel

from src.business.domain.character.CharacterService import CharacterService


class Character(BaseModel):
    id: str
    name: str
    character_class_name: str


def character_list_handler(character_service: Annotated[CharacterService, Depends(CharacterService)]):
    return character_service.list()
