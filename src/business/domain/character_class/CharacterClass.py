class CharacterClass:
    id: str
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def get_fields(cls):
        return ["id", "name"]
