from automapper import mapper

from .character import Character, CharacterClass
from src.business.domain.spell.spell import Spell
from src.infrastructure.data.DataService import DataService

mapper.add_spec(Character, Character.get_fields)
mapper.add_spec(CharacterClass, CharacterClass.get_fields)


class CharacterService:
    data = DataService()

    async def list_characters(self):
        db_characters = await self.data.list_characters()

        characters = []
        for db_character in db_characters:
            character: Character = mapper.to(Character).map(db_character, fields_mapping={
                "character_class": mapper.to(CharacterClass).map(db_character.character_class)
            })
            characters.append(character)

        return characters

    async def read_character(self, character_id):
        db_character = await self.data.read_character(character_id)

        character: Character = mapper.to(Character).map(db_character, fields_mapping={
            "character_class": mapper.to(CharacterClass).map(db_character.character_class)})
        character.spells = list(map(lambda spell: mapper.to(Spell).map(spell), db_character.spells))

        return character

    async def create_character(self, character):
        await self.data.create_character(character)
