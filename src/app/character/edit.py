from pydantic import BaseModel
from typing import Annotated
from fastapi import Depends
from uuid import UUID

from src.business.domain.character.CharacterService import CharacterService
from src.business.domain.character.character import CharacterEditDto


class CharacterEditApiDto(BaseModel):
    id: UUID
    name: str
    character_class_id: UUID


async def character_edit_handler(character_edit_api_dto: CharacterEditApiDto,
                                 character_service: Annotated[CharacterService, Depends(CharacterService)]):
    character: CharacterEditDto = CharacterEditDto(id=character_edit_api_dto.id,
                                                   name=character_edit_api_dto.name,
                                                   character_class_id=character_edit_api_dto.character_class_id)
    await character_service.edit_character(character)
    return {"id": character.id}
