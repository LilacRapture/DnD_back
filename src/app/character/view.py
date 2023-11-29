from pydantic import BaseModel


class CharacterClass(BaseModel):
    id: str
    name: str


class Spell(BaseModel):
    id: str
    name: str


class Character(BaseModel):
    id: str
    name: str
    character_class_name: CharacterClass  # id, name
    spells: list[Spell]


def character_handler(character_id):
    j_class_name = CharacterClass(id="5",
                                  name="Bard")

    mockery = Spell(id="12",
                    name="Vicious Mockery")

    crown = Spell(id="25",
                  name="Crown of Madness")

    j = Character(id="a1b32133-e947-43a6-b731-e535e66684ad",
                  name="Jaskier",
                  character_class_name=j_class_name,
                  spells=[mockery, crown])
    return j


def spell_handler(spell_id):
    spell = Spell(id="12",
                  name="Vicious Mockery")
    return spell
