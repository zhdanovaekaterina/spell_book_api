from dependency_injector import containers, providers

from app.repository import PsqlRepository
from app.core import CasterService


class Container(containers.DeclarativeContainer):

    # Шлюз получения данных
    repository = providers.Singleton(PsqlRepository)

    # Служба работы с заклинателями
    caster_service = providers.Factory(
        CasterService,
        repository=repository
    )
