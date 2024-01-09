from automapper import mapper
from uuid import UUID

from .character import Character, CharacterClass
from src.business.domain.spell.spell import Spell
from src.infrastructure.data.DataService import DataService

mapper.add_spec(Character, Character.get_fields)
mapper.add_spec(CharacterClass, CharacterClass.get_fields)


class CharacterService:
    data = DataService()

    # async def list_characters(self, user_id: UUID):
    #     db_characters = await self.data.list_characters(user_id)
    #
    #     characters = []
    #     for db_character in db_characters:
    #         character: Character = mapper.to(Character).map(db_character, fields_mapping={
    #             "character_class": mapper.to(CharacterClass).map(db_character.character_class)
    #         })
    #         characters.append(character)
    #
    #     return characters

    # async def list_character_classes(self):
    #     db_character_classes = await self.data.list_character_classes()
    #     character_classes = list(map(lambda character_class:
    #                                  mapper.to(CharacterClass).map(character_class), db_character_classes))
    #
    #     return character_classes

    async def read_character(self, user_id: UUID, character_id: UUID):
        db_character = await self.data.read_character(user_id, character_id)
        if db_character is None:
            return None

        character: Character = mapper.to(Character).map(db_character, fields_mapping={
            "character_class": mapper.to(CharacterClass).map(db_character.character_class)})
        character.spells = list(map(lambda spell: mapper.to(Spell).map(spell), db_character.spells))

        return character

    async def create_character(self, character):
        await self.data.create_character(character)

    async def edit_character(self, character):
        await self.data.edit_character(character)

    async def delete_character(self, character_id: UUID):
        await self.data.delete_character(character_id)

    async def add_spell_to_character(self, character_id: UUID, spell_id: UUID):
        await self.data.add_spell_to_character(character_id, spell_id)

    async def delete_spell_from_character(self, character_id: UUID, spell_id: UUID):
        await self.data.delete_spell_from_character(character_id, spell_id)
