from dependency_injector import containers, providers

from app.repository import DbRepository
from app.core import CasterService, InfoService


class Container(containers.DeclarativeContainer):

    # Настройки
    config = providers.Configuration()

    # Шлюз получения данных
    repository = providers.Singleton(
        DbRepository,
        url=config.db.url,
        registry=config.db.registry
    )

    # Служба работы с заклинателями
    caster_service = providers.Factory(CasterService, repository=repository)

    # Инфо-служба
    info_service = providers.Factory(InfoService, repository=repository)
