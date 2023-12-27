from sqlmodel import Field, Session, SQLModel, create_engine, Relationship, UniqueConstraint
from typing import Optional

import uuid as uuid_pkg


class ModelBase(SQLModel):
    """
    Base class for UUID-based models.
    """
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )


class User(ModelBase, table=True):
    name: Optional[str] = Field(nullable=True)
    email: Optional[str] = Field(nullable=True)
    password: Optional[str] = Field(nullable=True)

    characters: list["Character"] = Relationship(back_populates='user')


class CharacterClassSpell(ModelBase, table=True):
    character_class_id: uuid_pkg.UUID = Field(foreign_key='character_class.id', nullable=False)
    spell_id: uuid_pkg.UUID = Field(foreign_key='spell.id', nullable=False)


class CharacterSpell(ModelBase, table=True):
    __table_args__ = (
        UniqueConstraint("character_id", "spell_id"),
    )
    character_id: uuid_pkg.UUID = Field(foreign_key='character.id', nullable=False)
    spell_id: uuid_pkg.UUID = Field(foreign_key='spell.id', nullable=False)


class CharacterClass(ModelBase, table=True):
    __tablename__ = 'character_class'
    name: str = Field(max_length=256)

    characters: list["Character"] = Relationship(back_populates='character_class')
    spells: list['Spell'] = Relationship(back_populates='character_classes', link_model=CharacterClassSpell)


class Spell(ModelBase, table=True):
    name: str = Field(max_length=256)

    character_classes: list['CharacterClass'] = Relationship(back_populates='spells', link_model=CharacterClassSpell)
    characters: list["Character"] = Relationship(back_populates='spells', link_model=CharacterSpell)


class Character(ModelBase, table=True):
    name: str = Field(max_length=256)

    user_id: uuid_pkg.UUID = Field(foreign_key='user.id', nullable=False)
    user: User = Relationship(back_populates='characters')

    character_class_id: uuid_pkg.UUID = Field(foreign_key='character_class.id', nullable=False)
    character_class: CharacterClass = Relationship(back_populates='characters')

    spells: list["Spell"] = Relationship(back_populates='characters', link_model=CharacterSpell)


url = f'postgresql+psycopg://admin:WQk0R4PRpUWPAoIDNcUd6IanYmeun7Vn@dpg-cm19b4en7f5s73e5k8vg-a.frankfurt-postgres.render.com/main_5owc'
engine = create_engine(url, echo=True)


def create_characters():
    user = User()

    bard = CharacterClass(name="Bard")
    mockery = Spell(name="Vicious Mockery")
    crown = Spell(name="Crown of Madness")
    jaskier = Character(name="Jaskier",
                        user=user,
                        character_class=bard,
                        spells=[mockery, crown])

    wizard = CharacterClass(name="Wizard")
    fireball = Spell(name="Fireball")
    shield = Spell(name="Shield")
    yennefer = Character(name="Yennefer",
                         user=user,
                         character_class=wizard,
                         spells=[fireball, shield])

    with Session(engine) as session:
        session.add(user)

        session.add(bard)
        session.add(mockery)
        session.add(crown)
        session.add(jaskier)

        session.add(wizard)
        session.add(fireball)
        session.add(shield)
        session.add(yennefer)

        session.commit()


if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
    create_characters()
