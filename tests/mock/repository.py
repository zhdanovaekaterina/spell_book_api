from typing import List

from app.core.interfaces.repository import RepositoryInterface
from app.core.interfaces.dto import GameClassInfo


class MockRepository(RepositoryInterface):
    """
    Шлюз-заглушка для тестирования
    """

    # эмуляция таблицы 'caster'
    caster = []

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
            raise KeyError

    def delete_caster(self, caster_id: int) -> None:

        index = None
        for num, caster in enumerate(self.caster):
            if caster.id == caster_id:
                index = num

        if index is not None:
            self.caster.pop(index)
        else:
            raise KeyError
