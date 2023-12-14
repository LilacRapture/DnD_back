from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import selectinload

from .dtos import Character, CharacterClass, Spell


class DataService:
    db_name = "database.db"
    url = f'sqlite+aiosqlite:///{db_name}'
    engine = create_async_engine(url, echo=True)

    async def list_characters(self) -> list[Character]:
        async with AsyncSession(self.engine) as session:
            statement = select(Character, CharacterClass).join(CharacterClass)
            characters_with_classes = (await session.exec(statement)).all()  # all() makes a list instead of a table
            characters = []
            for character, character_class in characters_with_classes:
                db_character = Character(id=character.id, name=character.name,
                                         character_class_id=character_class.id,
                                         character_class=character_class)
                characters.append(db_character)

        return characters

    async def read_character(self, character_id):
        async with AsyncSession(self.engine) as session:
            statement = (select(Character, CharacterClass).
                         join(CharacterClass).
                         where(Character.id == character_id).
                         options(selectinload(Character.spells)))  # load relationship
            result = await session.exec(statement)
            character, character_class = result.first()  # .one() if there should be only one
            db_character = Character(id=character.id, name=character.name,
                                     character_class_id=character_class.id,
                                     character_class=character_class)
            db_character.spells = character.spells

        return db_character

    async def read_character_class(self, character_class_id):
        async with AsyncSession(self.engine) as session:
            character_class = await session.get(CharacterClass, character_class_id)

        return character_class

    async def create_character(self, character):
        db_character = Character(id=character.id, name=character.name, character_class_id=character.character_class_id)
        async with AsyncSession(self.engine) as session:
            session.add(db_character)
            await session.commit()

    async def list_spells(self):
        async with AsyncSession(self.engine) as session:
            statement = select(Spell)
            result = await session.exec(statement)
            spells = result.all()

        return spells

    async def read_spell(self, spell_id):
        async with AsyncSession(self.engine) as session:
            db_spell = await session.get(Spell, spell_id)
        spell = Spell(id=db_spell.id, name=db_spell.name)

        return spell
