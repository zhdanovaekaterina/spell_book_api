from os import environ

from fastapi import FastAPI

from app.di import Container
from app.repository.db.models import Base
from app.rest.routing import caster_router


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
