from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from app.core.interfaces.dto import GameClassInfo
from app.core.interfaces.repository import RepositoryInterface
from app.repository.db.models import GameClass, GameSubclass


class DbRepository(RepositoryInterface):
    """
    Шлюз для подключения к БД
    """

    def __init__(self, url, registry):
        self.registry = registry
        self.engine = create_engine(url)
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

    def save_caster(self, data) -> int:
        pass

    def get_caster(self, caster_id: int):
        pass

    def delete_caster(self, caster_id: int) -> bool:
        pass

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
