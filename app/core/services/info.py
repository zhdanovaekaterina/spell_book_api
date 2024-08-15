from app.core.base.service import Service


class InfoService(Service):
    """
    Служба для получения справочной информации по заклинателям
    """

    def get_available(self):
        """
        Получить доступные заклинания
        :return:
        """
        pass

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

    def get_cell_progress(self):
        """
        Получить прогресс ячеек в зависимости от типа кастера
        :return:
        """
        pass
