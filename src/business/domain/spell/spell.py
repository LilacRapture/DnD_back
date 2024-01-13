from automapper import mapper


class Spell:
    id: str
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def get_fields(cls):
        return ["id", "name"]


mapper.add_spec(Spell, Spell.get_fields)
