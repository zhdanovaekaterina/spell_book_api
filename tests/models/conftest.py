import pytest

from app.di import Container
from tests.mock.repository import MockRepository


@pytest.fixture(scope='module')
def di():
    """
    Внедрение тестовых зависимостей
    """

    container = Container()
    container.repository.override(MockRepository())
    container.wire(modules=[
        'app.core.models.game_class'
    ])
