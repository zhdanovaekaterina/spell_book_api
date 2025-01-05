from sqlalchemy import String, Column, ForeignKey, SmallInteger, Integer
from sqlalchemy.orm import registry, relationship

from app.repository.db.prettify import Prettify


mapper_registry = registry()
Base = mapper_registry.generate_base()


# Справочники - d_

class GameClass(Base, Prettify):
    """
    Справочник классов
    """

    __tablename__ = 'd_class'
    alias = Column(String(32), primary_key=True)
    title = Column(String(255), nullable=False)
    choose_subclass_level = Column(SmallInteger)
    type = Column(String(32), nullable=False)  # full, half etc., todo связь с GameClassType

    subclasses = relationship('GameSubclass', back_populates='game_class')
    caster_class = relationship('CasterClass', back_populates='game_class')
    spell_available = relationship('SpellAvailability', back_populates='game_class')


class GameSubclass(Base, Prettify):
    """
    Справочник подклассов
    """

    __tablename__ = 'd_subclass'
    class_alias = Column(String(32), ForeignKey('d_class.alias'), nullable=False)
    alias = Column(String(32), primary_key=True)
    title = Column(String(255), nullable=False)

    game_class = relationship('GameClass', back_populates='subclasses')
    caster_class = relationship('CasterClass', back_populates='game_subclass')
    spell_available = relationship('SpellAvailability',
                                   back_populates='game_subclass')


class GameClassType(Base, Prettify):
    """
    Типы заклинателей - фуллкастер, полукастер итд.
    Плюс прогресс по количеству и уровням ячеек в зависимости от
    уровня персонажа
    todo: составной ключ из первых 3х колонок
    """

    __tablename__ = 'd_game_class_type'
    alias = Column(String(32), primary_key=True)  # todo: тут Enum
    class_level = Column(SmallInteger, primary_key=True)
    cell_level = Column(SmallInteger, primary_key=True)
    cell_add_amount = Column(SmallInteger, nullable=False)


class Spell(Base, Prettify):
    """
    Справочник заклинаний
    """

    __tablename__ = 'd_spell'
    id = Column(Integer, primary_key=True, autoincrement=True)
    alias = Column(String(255), nullable=False, unique=True)
    title = Column(String(255), nullable=False)
    level = Column(SmallInteger, nullable=False)

    spell_available = relationship('SpellAvailability', back_populates='spell')


# Таблицы связей между справочниками - dl_

class SpellAvailability(Base, Prettify):
    """
    Доступность заклинаний классам и подклассам
    """

    __tablename__ = 'dl_spell_availability'
    id = Column(Integer, primary_key=True, autoincrement=True)
    spell_id = Column(Integer, ForeignKey('d_spell.id'), nullable=False)
    class_alias = Column(String(32), ForeignKey('d_class.alias'), nullable=False)
    subclass_alias = Column(String(32), ForeignKey('d_subclass.alias'))

    spell = relationship('Spell', back_populates='spell_available')
    game_class = relationship('GameClass', back_populates='spell_available')
    game_subclass = relationship('GameSubclass', back_populates='spell_available')


# Рабочие таблицы - g_

class Caster(Base, Prettify):
    """
    Рабочая таблица персонажей
    """

    __tablename__ = 'g_caster'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    intelligence = Column(SmallInteger)
    wisdom = Column(SmallInteger)
    charisma = Column(SmallInteger)

    caster_class = relationship('CasterClass',
                                back_populates='caster',
                                cascade='all,delete',
                                passive_deletes=True)


# Таблицы связей - l_

class CasterClass(Base, Prettify):
    """
    Таблица связей персонажей с классами
    """

    __tablename__ = 'l_caster_class'
    id = Column(Integer, primary_key=True, autoincrement=True)
    caster_id = Column(Integer, ForeignKey('g_caster.id', ondelete='CASCADE'), nullable=False)
    class_alias = Column(String(32), ForeignKey('d_class.alias'), nullable=False)
    subclass_alias = Column(String(32), ForeignKey('d_subclass.alias'))
    level = Column(SmallInteger)

    caster = relationship('Caster', back_populates='caster_class')
    game_class = relationship('GameClass', back_populates='caster_class')
    game_subclass = relationship('GameSubclass', back_populates='caster_class')

