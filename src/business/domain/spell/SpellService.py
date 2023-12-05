from .spell import Spell
from src.infrastructure.data.DataService import DataService


class SpellService:
    data = DataService()

    def read_spell(self, spell_id):
        db_spell = self.data.read_spell(spell_id)
        spell = Spell(id=db_spell.id, name=db_spell.name)

        return spell
