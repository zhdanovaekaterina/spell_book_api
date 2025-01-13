from typing import List

from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from app.core import InfoService
from app.core.models.const import MAX_CASTER_LEVEL
from app.rest.dto import SpellDto, ExcDto


router = APIRouter(prefix='/info')


@router.get(
    '/spells/available',
    status_code=status.HTTP_200_OK,
    response_model=List[SpellDto],
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

    spells = service.get_available(
        alias=alias, subclass=subclass, level=level
    )

    return [SpellDto(**s) for s in spells]
