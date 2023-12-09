from automapper import mapper

from .spell import Spell
from src.infrastructure.data.DataService import DataService


mapper.add_spec(Spell, Spell.get_fields)


class SpellService:
    data = DataService()

    def list_spells(self):
        db_spells = self.data.list_spells()
        spells = list(map(lambda spell: mapper.to(Spell).map(spell), db_spells))

        return spells

    def read_spell(self, spell_id):
        db_spell = self.data.read_spell(spell_id)
        spell: Spell = mapper.to(Spell).map(db_spell)

        return spell
