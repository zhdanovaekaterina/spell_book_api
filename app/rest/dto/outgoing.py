from typing import List

from pydantic import BaseModel

from app.core import CasterModel, SpellModel


class ExcDataDto(BaseModel):
    type: str
    msg: str = ''


class ExcDto(BaseModel):
    detail: List[ExcDataDto]


class OkDto(BaseModel):
    detail: str = 'OK'


class IdDto(BaseModel):
    id: int


class CasterDto(CasterModel):
    id: int


class SpellDto(SpellModel):
    ...
