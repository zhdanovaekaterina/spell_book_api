from typing import List

from pydantic import BaseModel, Field

from app.core.models.enums import SpellCharacteristic


class GameClassInfo(BaseModel):
    """
    Данные о классе из репозитория
    """

    alias: str
    subclasses: List[str]
    choose_subclass_level: int = Field(ge=1, le=3)
    spell_char: SpellCharacteristic
