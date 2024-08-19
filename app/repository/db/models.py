from sqlalchemy import String, Column, ForeignKey, SmallInteger
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


class GameSubclass(Base, Prettify):
    """
    Справочник подклассов
    """

    __tablename__ = 'd_subclass'
    class_alias = Column(String(32), ForeignKey('d_class.alias'), nullable=False)
    alias = Column(String(32), primary_key=True)
    title = Column(String(255), nullable=False)

    game_class = relationship('GameClass', back_populates='subclasses')
