from sqlmodel import Session, create_engine, select

from .dtos import Character, CharacterClass, Spell


class DataService:
    db_name = "database.db"
    url = f'sqlite:///{db_name}'
    engine = create_engine(url, echo=True)

    def list_characters(self) -> list[Character]:
        with Session(self.engine) as session:
            statement = select(Character, CharacterClass).join(CharacterClass)
            characters_with_classes = session.exec(statement).all()  # all() makes a list instead of a table
            characters = []
            for character, character_class in characters_with_classes:
                db_character = Character(id=character.id, name=character.name,
                                         character_class_id=character_class.id,
                                         character_class=character_class)
                characters.append(db_character)

        return characters

    def read_character(self, character_id):
        with Session(self.engine) as session:
            statement = select(Character, CharacterClass).join(CharacterClass).where(Character.id == character_id)
            character, character_class = session.exec(statement).first()  # .one() if there should be only one
            db_character = Character(id=character.id, name=character.name,
                                     character_class_id=character_class.id,
                                     character_class=character_class)
            db_character.spells = character.spells

        return db_character

    def read_character_class(self, character_class_id):
        with Session(self.engine) as session:
            character_class = session.get(CharacterClass, character_class_id)

        return character_class

    def read_spell(self, spell_id):
        with Session(self.engine) as session:
            db_spell = session.get(Spell, spell_id)
        spell = Spell(id=db_spell.id, name=db_spell.name)

        return spell


# req = DataService()
# print(req.read_character("7af6be762a6743e583f12b4cb9cf46c3"))
