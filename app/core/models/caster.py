from typing import Optional

from pydantic import BaseModel, Field, model_validator

from app.core.models.game_class import GameClass
from app.core.models.stats import Stats


class Caster(BaseModel):
    """
    Модель заклинателя
    """

    id: Optional[int] = None
    name: str = Field(frozen=True)
    classes: list[GameClass]
    stats: Stats

    @model_validator(mode='after')
    def valid_model(self) -> BaseModel:
        assert len(self.classes) == 1  # временно, до реализации мультикласса
        return self
