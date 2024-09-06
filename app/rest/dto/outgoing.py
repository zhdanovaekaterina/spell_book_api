from typing import List

from pydantic import BaseModel

from app.core import CasterModel


class ExcDataDto(BaseModel):
    type: str
    msg: str = ''


class ExcDto(BaseModel):
    detail: List[ExcDataDto]


class IdDto(BaseModel):
    id: int


class CasterDto(CasterModel):
    id: int
