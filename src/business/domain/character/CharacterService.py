from automapper import mapper

from .character import Character, CharacterClass
from src.business.domain.spell.spell import Spell
from src.infrastructure.data.DataService import DataService

mapper.add_spec(Character, Character.get_fields)
mapper.add_spec(CharacterClass, CharacterClass.get_fields)


class CharacterService:
    data = DataService()

    def list_characters(self):
        db_characters = self.data.list_characters()

        characters = []
        for db_character in db_characters:
            character: Character = mapper.to(Character).map(db_character, fields_mapping={
                "character_class": mapper.to(CharacterClass).map(db_character.character_class)
            })
            characters.append(character)

            # print(vars(character))
            # print(vars(character.character_class))

        # characters = map(lambda db_char: mapper.to(Character).map(db_char, fields_mapping={
        #     "character_class": mapper.to(CharacterClass).map(db_char.character_class)
        # }), db_characters)

        return characters

    def read_character(self, character_id):
        db_character = self.data.read_character(character_id)

        character: Character = mapper.to(Character).map(db_character, fields_mapping={
            "character_class": mapper.to(CharacterClass).map(db_character.character_class)})
        # character.spells = db_character.spells
        print(vars(character))

        return character
