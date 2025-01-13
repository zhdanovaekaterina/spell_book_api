from typing import List

from pydantic import BaseModel, Field


class GameClassInfo(BaseModel):
    """
    Данные о классе из репозитория
    """

    alias: str
    subclasses: List[str]
    choose_subclass_level: int = Field(ge=1, le=3)
