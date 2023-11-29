from .character import Character, CharacterClass


class CharacterService:

    def list(self):
        a_class = CharacterClass()
        a_class.id = '1'
        a_class.name = 'Barbarian'
        a = Character()
        a.id = 'e87aa451-d3cc-4bd6-b1b9-efc9453b1735',
        a.name = 'Geralt',
        a.character_class = a_class

        b_class = CharacterClass()
        b_class.id = '2'
        b_class.name = 'Bard'
        b = Character()
        b.id = 'a1b32133-e947-43a6-b731-e535e66684ad',
        b.name = 'Jaskier',
        b.character_class = b_class

        c_class = CharacterClass()
        c_class.id = '3'
        c_class.name = 'Wizard'
        c = Character()
        c.id = 'a7132ed1-109e-4708-8d92-cad7bc40a4a9',
        c.name = 'Yennefer',
        c.character_class = c_class

        return [a, b, c]
