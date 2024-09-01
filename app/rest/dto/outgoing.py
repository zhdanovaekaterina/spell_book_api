from typing import List

from pydantic import BaseModel


class ExcDataDto(BaseModel):
    type: str
    msg: str


class ExcDto(BaseModel):
    detail: List[ExcDataDto]


class IdDto(BaseModel):
    id: int
