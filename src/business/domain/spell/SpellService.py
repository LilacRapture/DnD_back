from .spell import Spell


class SpellService:

    def read_spell(self, spell_id):
        spell = Spell(id=spell_id,
                      name="Vicious Mockery")
        return spell
