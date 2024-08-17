from pydantic import BaseModel, Field


class Stats(BaseModel):
    """
    Блок игровых характеристик персонажа
    """

    intelligence: int = Field(gt=7, lt=30)
    wisdom: int = Field(gt=7, lt=30)
    charisma: int = Field(gt=7, lt=30)
