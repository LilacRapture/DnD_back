class CharacterClass:
    id: str
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def get_fields(cls):
        return ["id", "name"]


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
