from pydantic import BaseModel
from typing import Annotated
from fastapi import Depends
from uuid import UUID
from automapper import mapper

from src.app.spell.view import Spell
from src.business.domain.character.CharacterService import CharacterService


class CharacterClass(BaseModel):
    id: UUID
    name: str

    @staticmethod
    def get_fields(cls):
        return ["id", "name"]


class Character(BaseModel):
    id: UUID
    name: str
    character_class: CharacterClass  # id, name
    # spells: list[Spell]

    @staticmethod
    def get_fields(cls):
        return ["id", "name", "character_class"]


mapper.add_spec(Character, Character.get_fields)
mapper.add_spec(CharacterClass, CharacterClass.get_fields)


def character_handler(character_id, character_service: Annotated[CharacterService, Depends(CharacterService)]):
    character = character_service.read_character(character_id)
    # print(vars(character))
    # print(vars(character.character_class))

    character_dto: Character = mapper.to(Character).map(character, fields_mapping={
        "character_class": mapper.to(CharacterClass).map(character.character_class)
    })

    return character_dto
