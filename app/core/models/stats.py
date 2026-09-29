from pydantic import BaseModel, Field

from app.core.models.const import MIN_STAT_VALUE, MAX_STAT_VALUE


class Stats(BaseModel):
    """
    Блок игровых характеристик персонажа.
    Храним все ментальные с прицелом на мультикласс, чтобы не дублировать их в каждом классе.
    """

    intelligence: int = Field(gt=MIN_STAT_VALUE, lt=MAX_STAT_VALUE)
    wisdom: int = Field(gt=MIN_STAT_VALUE, lt=MAX_STAT_VALUE)
    charisma: int = Field(gt=MIN_STAT_VALUE, lt=MAX_STAT_VALUE)
