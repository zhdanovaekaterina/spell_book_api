from abc import ABC, abstractmethod
from typing import List, Union

from app.core.interfaces.dto import GameClassInfo


class RepositoryInterface(ABC):
    """
    Интерфейс для загрузки внешних данных
    """

    @abstractmethod
    def get_all_classes(self, full: bool = False)\
            -> Union[List[GameClassInfo], List[str]]:
        """
        Получение списка классов
        :param: full - флаг если нужно возвращать всю информацию
        :return: Union[List[GameClassInfo], List[str]]
        """

    @abstractmethod
    def get_one_class(self, alias: str) -> GameClassInfo:
        """
        Получение информации по одному классу по алиасу
        :param: alias
        :return: GameClassInfo
        :raise: KeyError - если класс не найден
        """

    @abstractmethod
    # todo: указать тип Caster у даты и разобраться с циклическими импортами
    def save_caster(self, data) -> int:
        """
        Сохранение персонажа
        При сохранении присваивает модели id
        :param data: модель персонажа
        :return: id заклинателя
        """

    @abstractmethod
    # todo: указать тип Caster у возвращаемого значения
    def get_caster(self, caster_id: int):
        """
        Получение персонажа по id
        :param caster_id:
        :return:
        :raise: KeyError - если персонаж не найден по id
        """

    @abstractmethod
    def delete_caster(self, caster_id: int) -> bool:
        """
        Удаление персонажа по id
        :param caster_id:
        :return:
        :raise: KeyError - если персонаж не найден по id
        """
