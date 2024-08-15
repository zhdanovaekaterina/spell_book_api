from abc import ABC

from app.core.interfaces.repository import RepositoryInterface


class Service(ABC):
    """
    Базовый класс для служб
    """

    def __init__(self, repository: RepositoryInterface):
        self.repository = repository
