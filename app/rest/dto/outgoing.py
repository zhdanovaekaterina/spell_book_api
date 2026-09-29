from typing import List

from pydantic import BaseModel

from app.core import CasterModel
from app.core.models.ids import CasterId


class ExcDataDto(BaseModel):
    type: str
    msg: str = ''


class ExcDto(BaseModel):
    detail: List[ExcDataDto]


class OkDto(BaseModel):
    detail: str = 'OK'


class CasterIdDto(BaseModel):
    id: int

class CasterDto(CasterModel):  # здесь обязательно должен возвращаться id
    id: CasterId
