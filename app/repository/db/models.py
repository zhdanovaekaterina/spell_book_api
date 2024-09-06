from sqlalchemy import String, Column, ForeignKey, SmallInteger, Integer
from sqlalchemy.orm import registry, relationship

from app.repository.db.prettify import Prettify


mapper_registry = registry()
Base = mapper_registry.generate_base()


class GameClass(Base, Prettify):
    """
    Справочник классов
    """

    __tablename__ = 'd_class'
    alias = Column(String(32), primary_key=True)
    title = Column(String(255), nullable=False)
    choose_subclass_level = Column(SmallInteger)

    subclasses = relationship('GameSubclass', back_populates='game_class')
    caster_class = relationship('CasterClass', back_populates='game_class')


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

