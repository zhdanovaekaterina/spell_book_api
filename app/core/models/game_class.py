from typing import Optional

from pydantic import BaseModel, Field, model_validator
from pydantic_core import PydanticCustomError
from dependency_injector.wiring import inject, Provide

from app.core.models.const import MIN_CASTER_LEVEL, MAX_CASTER_LEVEL
from app.core.base.exc_type import CoreExcType
from app.core.interfaces.repository import RepositoryInterface


class GameClass(BaseModel):
    """
    Модель игрового класса
    """

    alias: str
    level: int = Field(default=1, ge=MIN_CASTER_LEVEL, le=MAX_CASTER_LEVEL)
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
            raise PydanticCustomError(
                CoreExcType.INVALID_CLASS.value,
                "invalid class '{class}' provided",
                {'class': self.alias}
            )

        # Проверяем необходимость наличия подкласса
        if self.level < game_class.choose_subclass_level:  # не должно быть
            self.subclass = None  # очищаем, если вдруг передан
            return self

        elif self.subclass is None:  # должен быть, но его нет
            raise PydanticCustomError(
                CoreExcType.MISSING_SUBCLASS.value,
                "class '{class}' on level {level} must have a subclass",
                {'class': self.alias, 'level': self.level}
            )

        else:  # должен быть и он есть
            # Проверяем валидный подкласс для класса
            if self.subclass not in game_class.subclasses:
                raise PydanticCustomError(
                    CoreExcType.INVALID_SUBCLASS.value,
                    "invalid subclass provided for a class {class}",
                    {'class': self.alias}
                )

            return self
