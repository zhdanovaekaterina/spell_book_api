from typing import List

from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from app.core import InfoService, SpellAggregate
from app.core.models.const import MAX_CASTER_LEVEL
from app.rest.dto import ExcDto


router = APIRouter(prefix='/info', tags=["Info"])


@router.get(
    '/spells/available',
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
