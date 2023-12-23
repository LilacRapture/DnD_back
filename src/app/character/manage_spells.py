from typing import Annotated
from fastapi import Depends

from src.business.domain.character.CharacterService import CharacterService


async def add_spell_to_character_handler(character_id,
                                         spell_id,
                                         character_service: Annotated[CharacterService, Depends(CharacterService)]):
    await character_service.add_spell_to_character(character_id, spell_id)


async def delete_spell_from_character_handler(character_id,
                                              spell_id,
                                              character_service: Annotated[CharacterService, Depends(CharacterService)]):
    await character_service.delete_spell_from_character(character_id, spell_id)
