from typing import List, Optional

from pydantic import BaseModel, Field

from app.core.models.const import MAX_CASTER_LEVEL


class GameClassInfo(BaseModel):
    """
    Данные о классе из репозитория
    """

    alias: str
    subclasses: List[str]
    choose_subclass_level: int = Field(ge=1, le=3)


class ParamsToGetSpellsAvailable(BaseModel):
    """
    Параметры для получения списка доступных заклинаний
    """

    game_class: str
    game_subclass: Optional[str] = None
    level: Optional[int] = MAX_CASTER_LEVEL


class SpellInfo(BaseModel):
    """
    Данные о заклинании из репозитория
    """
    id: int
    alias: str
    title: str
