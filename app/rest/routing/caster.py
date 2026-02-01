from typing import List

from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from app.core import CasterService
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
    '/{id}',
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
    id: int,
    service: CasterService = Depends(Provide['caster_service']),
):
    caster = service.get(id)
    return CasterDto(**caster)


@router.delete(
    '/{id}',
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
    id: int,
    service: CasterService = Depends(Provide['caster_service']),
):
    service.delete(id)
    return OkDto()


@router.get(
    "/{id}/spells/available",
    summary="Получение доступных заклинаний для персонажа",
    description="Возвращает общий список доступных заклинаний для конкретного персонажа по его id, " \
        "с пометкой, если какое-либо уже изучено или подготовлено.",
    status_code=status.HTTP_200_OK,
    response_model=dict,  # SpellAggregate тут не работает, потому что возвращается насквозь из ядра и повторная валидация не нужна
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ExcDto
        },
    }
)
@inject
def get_spells_available(
    id: int,
    service: CasterService = Depends(Provide['caster_service']),
    # todo: добавить флаг (only_new), при передаче которого будут выводиться только те заклинания, которые еще не изучены/не подготовлены
):
    return service.get_available(id)


@router.get(
    "/{id}/spells/learn",
    summary="Заклинания для изучения",
    description="Возвращает доступные персонажу заклинания за вычетом уже изученных. " \
        "Для классов, которые не изучают заклинания, возвращает 405 Method Not Allowed",
    status_code=status.HTTP_501_NOT_IMPLEMENTED
)
def get_spells_learn(
    id: int
):
    ...


@router.post(
    "/{id}/spells/learn",
    summary="Изучение заклинаний",
    description="Фиксирует заклинания как изученные данным персонажем. " \
        "Для классов, которые не изучают заклинания, возвращает 405 Method Not Allowed",
    status_code=status.HTTP_501_NOT_IMPLEMENTED
)
def post_spells_learn(
    id: int
):
    ...


@router.get(
    "/{id}/spells/prepare",
    summary="Заклинания для подготовки",
    description="Возвращает заклинания, доступные персонажу для подготовки. " \
        "Для классов, которые не готовят заклинания, возвращает 405 Method Not Allowed",
    status_code=status.HTTP_501_NOT_IMPLEMENTED
)
def get_spells_prepare(
    id: int
):
    ...


@router.post(
    "/{id}/spells/prepare",
    summary="Подготовка заклинаний",
    description="Фиксирует заклинания как подготовленные данным персонажем. " \
        "Для классов, которые не изучают заклинания, возвращает 405 Method Not Allowed",
    status_code=status.HTTP_501_NOT_IMPLEMENTED
)
def post_spells_prepare(
    id: int
):
    ...


@router.get(
    "/{id}/spells/use",
    summary="Заклинания для использования",
    description="Возвращает заклинания, доступные персонажу для использования. " \
        "В этот список будут входить те заклинания, которые изучены и/или подготовлены, в зависимости от класса",
    status_code=status.HTTP_501_NOT_IMPLEMENTED
)
def get_spells_use(
    id: int
):
    ...


@router.get(
    '/{id}/spells/count',
    summary="Получение количества заклинаний",
    description="Возвращает информацию по количеству доступных заклинаний для подготовки или/и изучения. " \
        "Отдельно выводится общее количество и отдельно доступное с учетом уже изученных/подготовленных заклинаний",
    status_code=status.HTTP_501_NOT_IMPLEMENTED
)
def get_spells_count(
    id: int
):
    ...


@router.get(
    '/{id}/cells',
    summary="Получение доступных ячеек заклинаний для персонажа",
    description="Возвращает количество и уровни доступных ячеек для конкретного персонажа",
    status_code=status.HTTP_501_NOT_IMPLEMENTED
)
def get_cells(
    id: int
):
    ...
