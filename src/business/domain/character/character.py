from uuid import UUID
from src.business.domain.character_class.CharacterClass import CharacterClass


class Character:
    id: str
    name: str
    character_class: CharacterClass
    spells: []

    def __init__(self, id, name, character_class):
        self.id = id
        self.name = name
        self.character_class = character_class

    @staticmethod
    def get_fields(cls):
        return ["id", "name", "character_class"]


class CharacterCreateDto:
    id: UUID
    name: str
    user_id: UUID
    character_class_id: UUID

    def __init__(self, id, name, user_id, character_class_id):
        self.id = id
        self.name = name
        self.user_id = user_id
        self.character_class_id = character_class_id


class CharacterEditDto:
    id: UUID
    name: str
    character_class_id: UUID

    def __init__(self, id, name, character_class_id):
        self.id = id
        self.name = name
        self.character_class_id = character_class_id
