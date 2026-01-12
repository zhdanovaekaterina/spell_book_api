from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from app.core import InfoService, SpellAggregate
from app.core.models.const import MAX_CASTER_LEVEL
from app.rest.dto import ExcDto


router = APIRouter(prefix='/info', tags=["Info"])


@router.get(
    '/spells/available',
    summary="Получение доступных заклинаний",
    description="Возвращает весь список доступных заклинаний по переданным параметрам",
    status_code=status.HTTP_200_OK,
    response_model=SpellAggregate,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            'model': ExcDto
        },
    }
)
@inject
def get_spells_available(
    alias: str,
    subclass: str = None,
    level: int = MAX_CASTER_LEVEL,
    service: InfoService = Depends(Provide['info_service']),
):

    return service.get_available(alias=alias, subclass=subclass, level=level)


@router.get(
    '/cells',
    summary="Получение доступных ячеек заклинаний",
    description="Возвращает количество и уровни доступных ячеек для одного класса указанного уровня",
    status_code=status.HTTP_501_NOT_IMPLEMENTED
)
def get_cells(
    alias: str,
    level: int = MAX_CASTER_LEVEL
):
    ...
