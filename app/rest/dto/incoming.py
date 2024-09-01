from typing import Optional

from pydantic import BaseModel, Field


class CasterCreateInDto(BaseModel):
    """
    Входящие параметры для создания персонажа
    """

    name: str = Field(examples=["Player"])
    game_class: str = Field(examples=["cleric"])
    game_subclass: Optional[str] = Field(
        default=None,
        examples=["c_life"],
        description="Подкласс требуется, если класс его выбирает на первом уровне"
    )
    intelligence: int = Field(examples=[16])
    wisdom: int = Field(examples=[10])
    charisma: int = Field(examples=[10])
