from .character import Character, CharacterClass
from src.business.domain.spell.spell import Spell
from src.infrastructure.data.DataService import DataService


class CharacterService:
    data = DataService()

    def list_characters(self):
        characters = []
        for dto_character in self.data.list_characters():
            dto_character_class = self.data.read_character_class(dto_character.character_class_id)
            character_class = CharacterClass(id=dto_character_class.id, name=dto_character_class.name)
            character = Character(id=dto_character.id, name=dto_character.name, character_class=character_class)
            characters.append(character)

        return characters

    def read_character(self, character_id):
        dto_character = self.data.read_character(character_id)
        dto_character_class = self.data.read_character_class(dto_character.character_class_id)

        character_class = CharacterClass(id=dto_character_class.id, name=dto_character_class.name)
        character = Character(id=dto_character.id, name=dto_character.name, character_class=character_class)

        return character
