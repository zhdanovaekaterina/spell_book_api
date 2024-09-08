from typing import List
from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from app.core.base.core_exception import NotFoundException
from app.core.models.caster import Caster as CoreCaster
from app.core.interfaces.dto import (GameClassInfo,
                                     ParamsToGetSpellsAvailable, SpellInfo)
from app.core.interfaces.repository import RepositoryInterface
from app.repository.db.models import (GameClass, GameSubclass,
                                      Caster as DbCaster, CasterClass)


class DbRepository(RepositoryInterface):
    """
    Шлюз для подключения к БД
    """

    def __init__(self, url, registry):
        self.registry = registry
        self.engine = create_engine(url, echo=(environ.get('MODE') == 'DEV'))
        self.session = Session(self.engine)

    def get_all_classes(self) -> List[GameClassInfo]:

        with self.session:
            data = self.session\
                .query(GameClass)\
                .join(GameSubclass)\
                .all()

            return [self._parse_class_to_out(g_class) for g_class in data]

    def get_one_class(self, alias: str) -> GameClassInfo:

        with self.session:
            try:
                data = self.session\
                    .query(GameClass)\
                    .join(GameSubclass)\
                    .where(GameClass.alias == alias)\
                    .one()
            except NoResultFound:
                raise KeyError

            return self._parse_class_to_out(data)

    def get_available_spells(self, class_info: ParamsToGetSpellsAvailable)\
            -> List[SpellInfo]:
        ...

    def add_caster(self, data) -> int:
        model = self._parse_model_to_in(data)

        with Session(self.engine) as session:
            with session.begin():
                session.add(model)
                session.flush()
                return model.id

    def get_caster(self, caster_id: int):
        with self.session:
            try:
                data = self.session\
                    .query(DbCaster)\
                    .where(DbCaster.id == caster_id)\
                    .one()
            except NoResultFound:
                raise NotFoundException

            return self._parse_in_to_model(data)

    def delete_caster(self, caster_id: int) -> bool:
        with Session(self.engine) as session:
            with session.begin():
                deleted_rows = session.query(DbCaster)\
                    .where(DbCaster.id == caster_id)\
                    .delete()

        if not deleted_rows:
            raise NotFoundException

        return True

    @staticmethod
    def _parse_class_to_out(data) -> GameClassInfo:
        """
        Парсинг данных класса из модели в DTO
        :param data: GameClass
        :return:
        """

        class_data = {
            'alias': data.alias,
            'choose_subclass_level': data.choose_subclass_level,
            'subclasses': []
        }

        for subclass in data.subclasses:
            class_data['subclasses'].append(subclass.alias)

        return GameClassInfo(**class_data)

    @staticmethod
    def _parse_model_to_in(data: CoreCaster) -> DbCaster:
        """
        Парсинг модели персонажа ядра на модель базы
        :param data:
        :return:
        """

        # todo: разобраться почему не работает генерация модели из словаря
        caster = DbCaster(
            name=data.name,
            intelligence=data.stats.intelligence,
            wisdom=data.stats.wisdom,
            charisma=data.stats.charisma,
            caster_class=[]
        )

        for cl in data.classes:
            caster.caster_class.append(CasterClass(
                class_alias=cl.alias,
                subclass_alias=cl.subclass,
                level=cl.level
            ))

        return caster

    @staticmethod
    def _parse_in_to_model(data) -> CoreCaster:
        """
        Парсинг моделей базы в модели ядра
        :param data:
        :return:
        """

        return CoreCaster(**{
            'id': data.id,
            'name': data.name,
            'stats': {
                'intelligence': data.intelligence,
                'wisdom': data.wisdom,
                'charisma': data.charisma
            },
            'classes': [{
                'alias': cl.class_alias,
                'subclass': cl.subclass_alias,
                'level': cl.level
            } for cl in data.caster_class]
        })
