from .spell import Spell


class SpellService:

    def read_spell(self):
        spell = Spell(id="12",
                      name="Vicious Mockery")
        return spell
