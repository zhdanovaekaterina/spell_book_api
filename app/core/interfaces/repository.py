from abc import ABC, abstractmethod
from typing import List

from app.core.interfaces.dto import GameClassInfo


class RepositoryInterface(ABC):
    """
    Интерфейс для загрузки внешних данных
    """

    # Справочные методы по классам

    @abstractmethod
    def get_all_classes(self) -> List[GameClassInfo]:
        """
        Получение списка классов
        # todo: пока что особо нигде не используется, возможно не нужен
        :param: full - флаг если нужно возвращать всю информацию
        :return: List[GameClassInfo]
        """

    @abstractmethod
    def get_one_class(self, alias: str) -> GameClassInfo:
        """
        Получение информации по одному классу по алиасу
        :param: alias
        :return: GameClassInfo
        :raise: KeyError - если класс не найден
        """

    # Справочные методы по заклинаниям

    @abstractmethod
    # todo: указать тип ParamsToGetSpellsAvailable у параметра
    # todo: указать тип SpellAggregate у возвращаемого значения
    def get_available_spells(self, class_info) -> dict:
        """
        Получение списка заклинаний, доступных для переданных параметров
        :param class_info: ParamsToGetSpellsAvailable
        :return: SpellAggregate
        """

    @abstractmethod
    def get_cells(self, class_info) -> dict:
        """
        Получение количества и уровней ячеек заклинаний для класса и уровня
        :param class_info: ParamsToGetCellsAvailable
        :return: CellAggregate
        """

    # CRUD для персонажей

    @abstractmethod
    # todo: указать тип Caster у даты и разобраться с циклическими импортами
    def add_caster(self, data) -> int:
        """
        Добавление нового персонажа
        :param data: Caster - модель персонажа
        :return: id заклинателя
        """

    @abstractmethod
    # todo: указать тип Caster у возвращаемого значения
    def get_caster(self, caster_id: int):
        """
        Получение персонажа по id
        :param caster_id:
        :return: Caster
        :raise: NotFoundException - если персонаж не найден по id
        """

    @abstractmethod
    def delete_caster(self, caster_id: int) -> bool:
        """
        Удаление персонажа по id
        :param caster_id:
        :return:
        :raise: NotFoundException - если персонаж не найден по id
        """
