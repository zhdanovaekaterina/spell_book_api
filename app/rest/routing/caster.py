from typing import List

from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from app.core import CasterService, SpellAggregate
from app.rest.dto import CasterCreateInDto, IdDto, ExcDto, CasterDto, OkDto


router = APIRouter(prefix='/caster', tags=["Caster"])


@router.post(
    '/create',
    summary="Создание персонажа",
    description="Создает персонажа первого уровня",
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

    caster_id = service.create(**data)
    return IdDto(id=caster_id)


@router.get(
    '/{caster_id}',
    summary="Получение персонажа",
    description="Возвращает информацию о персонаже по его id",
    status_code=status.HTTP_200_OK,
    response_model=CasterDto,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ExcDto
        },
    }
)
@inject
def get_caster(
    caster_id: int,
    service: CasterService = Depends(Provide['caster_service']),
):
    caster = service.get(caster_id)
    return CasterDto(**caster)


@router.delete(
    '/{caster_id}',
    summary="Удаление персонажа",
    description="Удаляет персонажа по его id",
    status_code=status.HTTP_200_OK,
    response_model=OkDto,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ExcDto
        },
    }
)
@inject
def delete_caster(
    caster_id: int,
    service: CasterService = Depends(Provide['caster_service']),
):
    service.delete(caster_id)
    return OkDto()


@router.get(
    "/{caster_id}/spells/available",
    summary="Получение доступных заклинаний для персонажа",
    description="Возвращает список доступных заклинаний для конкретного персонажа по его id",
    status_code=status.HTTP_200_OK,
    response_model=SpellAggregate,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ExcDto
        },
    }
)
@inject
def get_spells_available(
    caster_id: int,
    service: CasterService = Depends(Provide['caster_service']),
):
    return service.get_available(caster_id)
