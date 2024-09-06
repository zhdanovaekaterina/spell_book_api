from app.core.base.service import Service
from app.core.models.caster import Caster


class CasterService(Service):
    """
    Служба для работы с заклинателями
    """

    def create(self, **data: dict) -> int:
        """
        Создание нового персонажа
        :return: id персонажа
        """

        caster = Caster(**data)
        return self.repository.add_caster(caster)

    def get(self, caster_id: int) -> dict:
        """
        Получение информации о персонаже по его id
        :return: словарь с данными персонажа
        :raise: NotFoundException - если персонаж не найден по id
        """

        caster = self.repository.get_caster(caster_id)
        return caster.model_dump()

    def delete(self, caster_id: int) -> None:
        """
        Удаление персонажа по его id
        :return:
        :raise: NotFoundException - если персонаж не найден по id
        """

        self.repository.delete_caster(caster_id)

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
