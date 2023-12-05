from .character import Character, CharacterClass
from src.business.domain.spell.spell import Spell
from src.infrastructure.data.DataService import DataService


class CharacterService:
    data = DataService()

    def list_characters(self):
        characters = []
        for db_character_and_class in self.data.list_characters():
            db_character, db_character_class = db_character_and_class
            character_class = CharacterClass(id=db_character_class.id, name=db_character_class.name)
            character = Character(id=db_character.id, name=db_character.name,
                                  character_class=character_class)
            characters.append(character)

        return characters

    def read_character(self, character_id):
        db_character, db_character_class = self.data.read_character(character_id)
        character_class = CharacterClass(id=db_character_class.id, name=db_character_class.name)
        spells = []
        for character_spell in db_character.spells:
            spell = Spell(id=character_spell.id, name=character_spell.name)
            spells.append(spell)
        character = Character(id=db_character.id, name=db_character.name, character_class=character_class)
        character.spells = spells

        return character
