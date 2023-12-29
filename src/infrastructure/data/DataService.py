from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import selectinload
from uuid import UUID

from .dtos import User, Character, CharacterClass, Spell, CharacterSpell


class DataService:
    url = f'postgresql+psycopg://admin:WQk0R4PRpUWPAoIDNcUd6IanYmeun7Vn@dpg-cm19b4en7f5s73e5k8vg-a.frankfurt-postgres.render.com/main_5owc'
    engine = create_async_engine(url, echo=True)

    async def create_user(self):
        db_user = User()
        user_id = db_user.id
        async with AsyncSession(self.engine) as session:
            session.add(db_user)
            await session.commit()
        return user_id

    async def delete_user(self, user_id: UUID):
        async with AsyncSession(self.engine) as session:
            user_to_delete = await session.get(User, user_id)
            await session.delete(user_to_delete)
            await session.commit()

    async def list_characters(self, user_id: UUID) -> list[Character]:
        async with AsyncSession(self.engine) as session:
            statement = select(Character, CharacterClass).join(CharacterClass).where(Character.user_id == user_id)
            characters_with_classes = (await session.exec(statement)).all()  # all() makes a list instead of a table
            characters = []
            for character, character_class in characters_with_classes:
                db_character = Character(id=character.id, name=character.name,
                                         character_class_id=character_class.id,
                                         character_class=character_class)
                characters.append(db_character)

        return characters

    async def read_character(self, character_id: UUID):
        async with AsyncSession(self.engine) as session:
            statement = (select(Character, CharacterClass).
                         join(CharacterClass).
                         where(Character.id == character_id).
                         options(selectinload(Character.spells)))  # load relationship
            result = await session.exec(statement)
            result = result.first()
            if result is None:
                return None
            character, character_class = result  # .one() if there should be only one
            db_character = Character(id=character.id, name=character.name,
                                     character_class_id=character_class.id,
                                     character_class=character_class)
            db_character.spells = character.spells

        return db_character

    async def read_character_class(self, character_class_id: UUID):
        async with AsyncSession(self.engine) as session:
            character_class = await session.get(CharacterClass, character_class_id)

        return character_class

    async def list_character_classes(self):
        async with AsyncSession(self.engine) as session:
            statement = select(CharacterClass)
            result = await session.exec(statement)
            character_classes = result.all()

        return character_classes

    async def create_character(self, character):
        db_character = Character(id=character.id,
                                 name=character.name,
                                 user_id=character.user_id,
                                 character_class_id=character.character_class_id)
        async with AsyncSession(self.engine) as session:
            session.add(db_character)
            await session.commit()

    async def edit_character(self, character):
        async with AsyncSession(self.engine) as session:
            db_character = await session.get(Character, character.id)
            db_character.id = character.id
            db_character.name = character.name
            db_character.character_class_id = character.character_class_id
            session.add(db_character)

            await session.commit()
            await session.refresh(db_character)

    async def delete_character(self, character_id: UUID):
        async with (AsyncSession(self.engine) as session):
            character_to_delete = await session.get(Character, character_id)
            await session.delete(character_to_delete)
            await session.commit()

    async def list_spells(self):
        async with AsyncSession(self.engine) as session:
            statement = select(Spell)
            result = await session.exec(statement)
            spells = result.all()

        return spells

    async def read_spell(self, spell_id: UUID):
        async with AsyncSession(self.engine) as session:
            db_spell = await session.get(Spell, spell_id)
        spell = Spell(id=db_spell.id, name=db_spell.name)

        return spell

    async def add_spell_to_character(self, character_id: UUID, spell_id: UUID):
        db_character_spell = CharacterSpell(character_id=character_id, spell_id=spell_id)
        async with AsyncSession(self.engine) as session:
            session.add(db_character_spell)
            await session.commit()

    async def delete_spell_from_character(self, character_id: UUID, spell_id: UUID):
        async with (AsyncSession(self.engine) as session):
            statement = (select(CharacterSpell)
                         .where(CharacterSpell.character_id == character_id)
                         .where(CharacterSpell.spell_id == spell_id))
            spell_to_delete = (await session.exec(statement)).first()
            await session.delete(spell_to_delete)
            await session.commit()
