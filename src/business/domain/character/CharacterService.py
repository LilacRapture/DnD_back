from .character import Character, CharacterClass
from src.business.domain.spell.spell import Spell


class CharacterService:

    def list_characters(self):
        a_class = CharacterClass(id='1',
                                 name='Barbarian')
        a = Character(id='e87aa451-d3cc-4bd6-b1b9-efc9453b1735',
                      name='Geralt',
                      character_class=a_class)

        b_class = CharacterClass(id='2',
                                 name='Bard')
        b = Character(id='a1b32133-e947-43a6-b731-e535e66684ad',
                      name='Jaskier',
                      character_class=b_class)

        c_class = CharacterClass(id='3',
                                 name='Wizard')
        c = Character(id='a7132ed1-109e-4708-8d92-cad7bc40a4a9',
                      name='Yennefer',
                      character_class=c_class)

        return [a, b, c]

    def read_character(self):
        j_class = CharacterClass(id="5",
                                 name="Bard")
        j = Character(id="a1b32133-e947-43a6-b731-e535e66684ad",
                      name="Jaskier",
                      character_class=j_class)
        mockery = Spell(id="12",
                        name="Vicious Mockery")
        crown = Spell(id="25",
                      name="Crown of Madness")
        j.spells = [mockery, crown]
        return j
