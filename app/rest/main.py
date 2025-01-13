from os import environ

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.di import Container
from app.core import NotFoundException
from app.repository.db.models import Base
from app.rest.routing import caster_router, info_router


# конфигурация контейнера зависимостей
container = Container()
container.config.from_dict({
    'db': {
        'url': "postgresql+psycopg2:"
            f"//{environ.get('POSTGRES_USER')}"
            f":{environ.get('POSTGRES_PASSWORD')}"
            f"@db/{environ.get('POSTGRES_DB')}",
        'registry': Base
    }
})
container.wire(modules=[
    'app.rest.routing.caster',
    'app.rest.routing.info',
    'app.core.models.game_class'
])


# конфигурация приложения
app = FastAPI(
    openapi_url="/system/docs/openapi.json",
    docs_url="/system/docs_old",
    redoc_url="/system/docs"
)


# подключение роутеров
app.include_router(caster_router)
app.include_router(info_router)


# подключение глобальных обработчиков ошибок
@app.exception_handler(ValidationError)
async def validation_error_handler(request: Request, exc: ValidationError):

    errs = [{
        'type': e.get('type'),
        'msg': e.get('msg')
    } for e in exc.errors()]

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={'detail': errs}
    )


@app.exception_handler(NotFoundException)
async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={'detail': [exc.error()]}
    )
