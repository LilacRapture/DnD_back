from typing import Annotated
from fastapi import Depends

from src.business.domain.character.CharacterService import CharacterService


async def character_delete_handler(character_id,
                                   character_service: Annotated[CharacterService, Depends(CharacterService)]):
    await character_service.delete_character(character_id)
