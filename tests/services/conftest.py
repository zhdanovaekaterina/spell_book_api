import pytest

from app.di import Container
from tests.mock.repository import MockRepository


@pytest.fixture(scope='module')
def container():
    """
    Конфигурация контейнера зависимостей
    :return:
    """

    container = Container()
    container.repository.override(MockRepository())
    return container


@pytest.fixture(scope='module')
def caster_service(container):
    """
    Создание службы для работы с персонажем
    :return: 
    """

    container.wire(modules=[
        'app.core.models.game_class'
    ])
    return container.caster_service()


@pytest.fixture(scope='module')
def info_service(container):
    """
    Создание инфо-службы
    :return:
    """

    return container.info_service()
