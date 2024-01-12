from pydantic import BaseModel
from typing import Annotated, Optional
from fastapi import Depends, Header
from mediatr import Mediator
from uuid import UUID, uuid4

from src.business.domain.character.character import CharacterCreateDto
from src.business.domain.character.use_cases.create import CreateCharacterRequest


class CharacterCreateApiDto(BaseModel):
    id: Optional[UUID] = None
    name: str
    character_class_id: UUID


async def character_create_handler(character_create_api_dto: CharacterCreateApiDto,
                                   mediator: Annotated[Mediator, Depends(Mediator)],
                                   x_dnd_auth: Annotated[str | None, Header()] = None):
    character: CharacterCreateDto = CharacterCreateDto(id=character_create_api_dto.id or uuid4(),
                                                       name=character_create_api_dto.name,
                                                       user_id=UUID(x_dnd_auth),
                                                       character_class_id=character_create_api_dto.character_class_id)
    await mediator.send_async(CreateCharacterRequest(character))
    return character
