from pydantic import BaseModel
from typing import Annotated
from fastapi import Depends, Header
from mediatr import Mediator
from uuid import UUID

from src.business.domain.character.use_cases.edit import EditCharacterRequest
from src.business.domain.character.character import CharacterEditDto


class CharacterEditApiDto(BaseModel):
    id: UUID
    name: str
    character_class_id: UUID


async def character_edit_handler(character_edit_api_dto: CharacterEditApiDto,
                                 mediator: Annotated[Mediator, Depends(Mediator)],
                                 x_dnd_auth: Annotated[str | None, Header()] = None):
    character: CharacterEditDto = CharacterEditDto(id=character_edit_api_dto.id,
                                                   name=character_edit_api_dto.name,
                                                   user_id=x_dnd_auth,
                                                   character_class_id=character_edit_api_dto.character_class_id)
    await mediator.send_async(EditCharacterRequest(character))
    return character
