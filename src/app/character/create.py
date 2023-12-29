from pydantic import BaseModel
from typing import Annotated, Optional
from fastapi import Depends, Header
from uuid import UUID, uuid4

from src.business.domain.character.character import CharacterCreateDto
from src.business.domain.character.CharacterService import CharacterService


class CharacterCreateApiDto(BaseModel):
    id: Optional[UUID] = None
    name: str
    character_class_id: UUID


async def character_create_handler(character_create_api_dto: CharacterCreateApiDto,
                                   character_service: Annotated[CharacterService, Depends(CharacterService)],
                                   x_dnd_auth: Annotated[str | None, Header()] = None):
    character: CharacterCreateDto = CharacterCreateDto(id=character_create_api_dto.id or uuid4(),
                                                       name=character_create_api_dto.name,
                                                       user_id=UUID(x_dnd_auth),
                                                       character_class_id=character_create_api_dto.character_class_id)
    await character_service.create_character(character)
    # return {"id": character.id}
    return character
