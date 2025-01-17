from typing import List, Set, Dict
from typing_extensions import Annotated
from collections import defaultdict

from pydantic import BaseModel, Field, model_validator

from app.core.models.const import MIN_SPELL_LEVEL, MAX_SPELL_LEVEL


class Spell(BaseModel):
    """
    Модель заклинания
    """

    id: int
    alias: str
    title: str
    level: int = Field(default=1, ge=MIN_SPELL_LEVEL, le=MAX_SPELL_LEVEL)

    def __eq__(self, other):
        return self.id == other.id


class SpellAggregate(BaseModel):
    """
    Сущность для представления списка заклинаний
    """

    levels_: Set[int] = Field(default_factory=set, exclude=False, repr=False)
    levels: List[int] = Field(default_factory=list)
    count: int = 0
    input: Annotated[List[Spell], Field(exclude=False, repr=False)]
    spells: Dict[int, List[Spell]] = Field(default=defaultdict(list))
    # todo: проверка что ключи являются валидными уровнями заклинаний

    @model_validator(mode='after')
    def proceed_input(self) -> BaseModel:
        [self._add(s) for s in self.input if s not in self.spells[s.level]]
        self.levels = sorted(self.levels_)
        return self

    def _add(self, s: Spell):
        self.spells[s.level].append(s)
        self.levels_.add(s.level)
        self.count += 1

    def __len__(self):
        return self.count
