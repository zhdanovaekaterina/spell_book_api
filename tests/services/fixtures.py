import pytest

from app.di import Container
from tests.mock.repository import MockRepository


@pytest.fixture(scope='module')
def caster_service():
    """
    Внедрение зависимостей и создание служб
    :return: 
    """

    container = Container()
    container.repository.override(MockRepository())
    return container.caster_service()
