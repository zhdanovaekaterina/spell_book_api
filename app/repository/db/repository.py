from typing import Union, List

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.interfaces.dto import GameClassInfo
from app.core.interfaces.repository import RepositoryInterface


class DbRepository(RepositoryInterface):
    """
    Шлюз для подключения к БД
    """

    def __init__(self, url, registry):
        self.registry = registry
        self.engine = create_engine(url)
        self.session = Session(self.engine)

    def get_all_classes(self, full: bool = False) \
            -> Union[List[GameClassInfo], List[str]]:
        pass

    def get_one_class(self, alias: str) -> GameClassInfo:
        pass

    def save_caster(self, data) -> int:
        pass

    def get_caster(self, caster_id: int):
        pass

    def delete_caster(self, caster_id: int) -> bool:
        pass
