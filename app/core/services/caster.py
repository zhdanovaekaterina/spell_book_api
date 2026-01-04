from dependency_injector.wiring import inject, Provide

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

    def level_up(self):  # todo: это должны быть методы домена Caster, они не имеют отношения к службе
        """
        Повышение уровня персонажа
        :return:
        """
        pass

    def learn(self):  # todo: и это
        """
        Изучение заклинаний
        :return:
        """
        pass

    def prepare(self):  # todo: и это
        """
        Подготовка заклинаний
        :return:
        """
        pass

    def get_learnt(self):  # todo: и это
        """
        Получение изученных заклинаний
        :return:
        """
        pass

    def get_prepared(self):  # todo: и это
        """
        Получение подготовленных заклинаний
        :return:
        """
        pass

    def get_cells(self):  # todo: и это
        """
        Получить уровни и количество ячеек заклинаний
        :return:
        """
        pass

    @inject
    def get_available(self,  # todo: и это
                      caster_id: int,
                      info_service: Service = Provide['info_service']
                      ) -> dict:
        """
        Получить доступные заклинания
        :return: SpellAggregate
        :raise: NotFoundException - если персонаж не найден по id
        """
        caster = self.get(caster_id)
        alias = caster.get("classes")[0].get("alias")  # todo: пока что это все расчитано только на 1 класс
        level = caster.get("classes")[0].get("level")
        subclass = caster.get("classes")[0].get("subclass")

        return info_service.get_available(alias=alias, level=level, subclass=subclass)
