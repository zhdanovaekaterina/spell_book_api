from typing import List

from app.core import NotFoundException
from app.core.models.const import MAX_CASTER_LEVEL
from app.core.models.enums import SpellCharacteristic
from app.core.models.spell import Spell, SpellAggregate
from app.core.models.cell import CellAggregate
from app.core.models.game_class import GameClass, ParamsToGetSpellsAvailable
from app.core.models.ids import CasterId
from app.core.interfaces.repository import RepositoryInterface
from app.core.interfaces.dto import GameClassInfo
from tests.mock.params import params_available_for_class


class MockRepository(RepositoryInterface):
    """
    Шлюз-заглушка для тестирования
    """

    # эмуляция таблицы 'caster'
    caster = []

    # эмуляция таблицы 'game_class'
    game_class = {
        'wizard': GameClassInfo(**{
            'alias': 'wizard',
            'subclasses': ['transmutation', 'evocation'],
            'choose_subclass_level': 2,
            'spell_char': SpellCharacteristic.INT
        }),
        'cleric': GameClassInfo(**{
            'alias': 'cleric',
            'subclasses': ['life', 'peace', 'light'],
            'choose_subclass_level': 1,
            'spell_char': SpellCharacteristic.WIS
        }),
        'ranger': GameClassInfo(**{
            'alias': 'ranger',
            'subclasses': [],
            'choose_subclass_level': 3,
            'spell_char': SpellCharacteristic.WIS
        }),
        'bard': GameClassInfo(**{
            'alias': 'bard',
            'subclasses': [],
            'choose_subclass_level': 3,
            'spell_char': SpellCharacteristic.CHA
        }),
        'artificier': GameClassInfo(**{
            'alias': 'artificier',
            'subclasses': [],
            'choose_subclass_level': 2,
            'spell_char': SpellCharacteristic.INT
        })
    }

    # эмуляция связей данных классов и заклинаний
    spell_to_class = {}

    def __init__(self):
        self.caster = []

        for param in params_available_for_class:
            key = self._get_key_from_dict(param[0])
            self.spell_to_class[key] = [Spell(**p) for p in param[1]]

    def get_all_classes(self) -> List[GameClassInfo]:
        return list(self.game_class.values())

    def get_one_class(self, alias: str) -> GameClassInfo:
        return self.game_class[alias]

    def get_available_spells(self, class_info: ParamsToGetSpellsAvailable) \
            -> SpellAggregate:

        key = self._get_key_from_dict(class_info.model_dump())
        spells_raw = self.spell_to_class.get(key, [])
        return SpellAggregate(input=spells_raw)

    def add_caster(self, data) -> CasterId:
        data.id = CasterId(len(self.caster) + 1)
        self.caster.append(data)
        return data.id

    def get_caster(self, caster_id: CasterId):

        index = None
        for num, caster in enumerate(self.caster):
            if caster.id == caster_id:
                index = num

        if index is not None:
            return self.caster[index]
        else:
            raise NotFoundException

    def delete_caster(self, caster_id: CasterId) -> None:

        index = None
        for num, caster in enumerate(self.caster):
            if caster.id == caster_id:
                index = num

        if index is not None:
            self.caster.pop(index)
        else:
            raise NotFoundException

    def get_cells(self, class_info) -> dict:

        data = CellAggregate()
        
        if class_info.alias == "wizard":
            if class_info.level == 1:
                data[1] += 2
            elif class_info.level == 10:
                data[1] += 4
                data[2] += 3
                data[3] += 3
                data[4] += 3
                data[5] += 2
        elif class_info.alias == "ranger":
            if class_info.level == 10:
                data[1] += 4
                data[2] += 3
                data[3] += 2
        
        return data

    def get_spells_count(self, alias, level, spell_char_value) -> dict:
        return {}

    @staticmethod
    def _get_key_from_dict(dict_data: dict) -> str:
        """
        Получение ключа из словаря параметров
        :param dict_data:
        :return:
        """

        keys_list = [
            str(dict_data.get('alias', None)),
            str(dict_data.get('subclass', None)),
            str(dict_data.get('level', MAX_CASTER_LEVEL)),
        ]
        return '_'.join(keys_list)
