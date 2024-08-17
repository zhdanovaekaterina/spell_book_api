from typing import List

from pydantic import BaseModel


class GameClassInfo(BaseModel):
    alias: str
    subclasses: List[str]
    choose_subclass_level: int
