from typing import List

from app.core import NotFoundException
from app.core.models.const import MAX_CASTER_LEVEL
from app.core.interfaces.repository import RepositoryInterface
from app.core.interfaces.dto import (GameClassInfo,
                                     ParamsToGetSpellsAvailable, SpellInfo)
from tests.mock.params import params_available_for_class


class MockRepository(RepositoryInterface):
    """
    Шлюз-заглушка для тестирования
    """

    # эмуляция таблицы 'caster'
    caster = []

    # эмуляция связей данных классов и заклинаний
    spell_to_class = {}

    def __init__(self):
        self.caster = []

        for param in params_available_for_class:
            key = self._get_key_from_dict(param[0])
            self.spell_to_class[key] = [SpellInfo(**p) for p in param[1]]

    def get_all_classes(self) -> List[GameClassInfo]:

        return [
            GameClassInfo(**{
                'alias': 'wizard',
                'subclasses': ['transmutation', 'evocation'],
                'choose_subclass_level': 2
            }),
            GameClassInfo(**{
                'alias': 'cleric',
                'subclasses': ['life', 'peace', 'light'],
                'choose_subclass_level': 1
            })
        ]

    def get_one_class(self, alias: str) -> GameClassInfo:

        if alias == 'wizard':
            return GameClassInfo(**{
                'alias': 'wizard',
                'subclasses': ['transmutation', 'evocation'],
                'choose_subclass_level': 2
            })
        elif alias == 'cleric':
            return GameClassInfo(**{
                'alias': 'cleric',
                'subclasses': ['life', 'peace', 'light'],
                'choose_subclass_level': 1
            })
        else:
            raise KeyError()

    def get_available_spells(self, class_info: ParamsToGetSpellsAvailable) \
            -> List[SpellInfo]:

        key = self._get_key_from_dict(class_info.model_dump())
        return self.spell_to_class.get(key, [])

    def add_caster(self, data) -> int:
        data.id = len(self.caster) + 1
        self.caster.append(data)
        return data.id

    def get_caster(self, caster_id: int):

        index = None
        for num, caster in enumerate(self.caster):
            if caster.id == caster_id:
                index = num

        if index is not None:
            return self.caster[index]
        else:
            raise NotFoundException

    def delete_caster(self, caster_id: int) -> None:

        index = None
        for num, caster in enumerate(self.caster):
            if caster.id == caster_id:
                index = num

        if index is not None:
            self.caster.pop(index)
        else:
            raise NotFoundException

    @staticmethod
    def _get_key_from_dict(dict_data: dict) -> str:
        """
        Получение ключа из словаря параметров
        :param dict_data:
        :return:
        """

        keys_list = [
            str(dict_data.get('game_class', None)),
            str(dict_data.get('game_subclass', None)),
            str(dict_data.get('level', MAX_CASTER_LEVEL)),
        ]
        return '_'.join(keys_list)
