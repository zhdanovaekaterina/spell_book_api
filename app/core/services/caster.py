from app.core.base.service import Service


class CasterService(Service):
    """
    Служба для работы с заклинателями
    """

    def create(self):
        """
        Создание нового персонажа
        :return:
        """
        pass

    def get(self):
        """
        Получение информации о персонаже по его id
        :return:
        """
        pass

    def delete(self):
        """
        Удаление персонажа
        :return:
        """
        pass

    def level_up(self):
        """
        Повышение уровня персонажа
        :return:
        """
        pass

    def learn(self):
        """
        Изучение заклинаний
        :return:
        """
        pass

    def prepare(self):
        """
        Подготовка заклинаний
        :return:
        """
        pass

    def get_learnt(self):
        """
        Получение изученных заклинаний
        :return:
        """
        pass

    def get_prepared(self):
        """
        Получение подготовленных заклинаний
        :return:
        """
        pass

    def get_cells(self):
        """
        Получить уровни и количество ячеек заклинаний
        :return:
        """
        pass

    def get_available(self):
        """
        Получить доступные заклинания
        :return:
        """
        pass
