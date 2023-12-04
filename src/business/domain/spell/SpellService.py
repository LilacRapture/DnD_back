from .spell import Spell
from src.infrastructure.data.DataService import DataService


class SpellService:
    data = DataService()

    # def read_spell(self, spell_id):
    #     spell = Spell(id=spell_id,
    #                   name="Vicious Mockery")
    #     return spell
    #
    def read_spell(self, spell_id):
        dto_spell = self.data.read_spell(spell_id)
        spell = Spell(id=dto_spell.id, name=dto_spell.name)

        return spell
