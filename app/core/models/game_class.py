from typing import Optional

from pydantic import BaseModel, Field, model_validator
from dependency_injector.wiring import inject, Provide

from app.core.interfaces.repository import RepositoryInterface


class GameClass(BaseModel):
    """
    Модель игрового класса
    """

    alias: str
    level: int = Field(default=1, ge=1, le=20)
    subclass: Optional[str] = None

    @model_validator(mode='after')
    @inject
    def valid_model(self,
                    repo: RepositoryInterface = Provide['repository']
                    ) -> BaseModel:

        # Проверяем валидно введенный класс
        try:
            game_class = repo.get_one_class(self.alias)
        except KeyError:
            raise ValueError(
                f'invalid class \'{self.alias}\' provided'
            )

        # Проверяем необходимость наличия подкласса
        if self.level < game_class.choose_subclass_level:  # не должно быть
            self.subclass = None  # очищаем, если вдруг передан
            return self

        elif self.subclass is None:  # должен быть, но его нет
            raise ValueError(
                f'class \'{self.alias}\' on level \'{self.level}\''
                f'must have a subclass'
            )

        else:  # должен быть и он есть
            # Проверяем валидный подкласс для класса
            if self.subclass not in game_class.subclasses:
                raise ValueError(
                    f'invalid subclass provided for a class \'{self.alias}\''
                )

            return self
