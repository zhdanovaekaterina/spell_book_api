from app.core.base.service import Service
from app.core.models.game_class import ParamsToGetSpellsAvailable, ParamsToGetCellsAvailable


class InfoService(Service):
    """
    Служба для получения справочной информации по заклинателям
    """

    def get_available(self, **data) -> dict:
        """
        Получить доступные заклинания
        :return: SpellAggregate
        """

        info = ParamsToGetSpellsAvailable(**data)
        return self.repository.get_available_spells(info)

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

    def get_cells(self, **data) -> dict:
        """
        Получить доступные ячейки
        :return: CellAggregate
        """

        params = ParamsToGetCellsAvailable(**data)
        return self.repository.get_cells(params)
