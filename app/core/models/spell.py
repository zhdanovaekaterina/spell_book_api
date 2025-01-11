from pydantic import BaseModel, Field

from app.core.models.const import MIN_SPELL_LEVEL, MAX_SPELL_LEVEL


class Spell(BaseModel):
    """
    Модель заклинания
    """

    id: int
    alias: str
    title: str
    level: int = Field(default=1, ge=MIN_SPELL_LEVEL, le=MAX_SPELL_LEVEL)
