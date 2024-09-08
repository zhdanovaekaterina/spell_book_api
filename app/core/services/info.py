from typing import List

from app.core.base.service import Service
from app.core.interfaces.dto import ParamsToGetSpellsAvailable


class InfoService(Service):
    """
    Служба для получения справочной информации по заклинателям
    """

    def get_available(self, **data) -> List[dict]:
        """
        Получить доступные заклинания
        :return:
        """

        info = ParamsToGetSpellsAvailable(**data)
        spells = self.repository.get_available_spells(info)
        return [spell.model_dump() for spell in spells]

    def get_game_classes(self):
        """
        Получить информацию по классам:
            - название, алиас
            - заклинательную характеристику
            - уровень, на котором берется подкласс
            - доступные подклассы
            - тип кастера (фул-, полу-, четверть-кастер)
        :return:
        """
        pass

    def get_cells(self):
        """
        Получить доступные ячейки
        :return:
        """
        pass
