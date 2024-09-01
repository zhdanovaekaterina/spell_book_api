from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from dependency_injector.wiring import inject, Provide

from app.core import CasterService
from app.rest.dto import CasterCreateInDto, IdDto, ExcDto


router = APIRouter(prefix='/caster')


@router.post(
    '/create',
    status_code=status.HTTP_201_CREATED,
    response_model=IdDto,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            'model': ExcDto
        },
    }
)
@inject
def create_caster(
        caster: CasterCreateInDto,
        service: CasterService = Depends(Provide['caster_service']),
    ):

    # маппинг
    data = {
        'name': caster.name,
        'classes': [{
            'alias': caster.game_class,
            'subclass': caster.game_subclass
        }],
        'stats': {
            'intelligence': caster.intelligence,
            'wisdom': caster.wisdom,
            'charisma': caster.charisma,
        }
    }

    try:
        caster_id = service.create(**data)
        return IdDto(id=caster_id)

    except ValidationError as err:

        errs = [{
            'type': e.get('type'),
            'msg': e.get('msg')
        } for e in err.errors()]

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={'detail': errs}
        )
