from typing import List, Union

from app.core.interfaces.repository import RepositoryInterface
from app.core.interfaces.dto import GameClassInfo


class MockRepository(RepositoryInterface):
    """
    Шлюз-заглушка для тестирования
    """

    def get_all_classes(self, full: bool = False)\
            -> Union[List[GameClassInfo], List[str]]:

        if full:

            return [
                GameClassInfo(**{
                    'alias': 'wizard',
                    'subclasses': ['transmutation', 'evocation'],
                    'choose_subclass_level': 3
                }),
                GameClassInfo(**{
                    'alias': 'cleric',
                    'subclasses': ['life', 'peace', 'light'],
                    'choose_subclass_level': 1
                })
            ]

        else:

            return ['wizard', 'cleric']

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
