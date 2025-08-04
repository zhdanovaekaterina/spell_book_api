import pytest
from fastapi.testclient import TestClient

from app.rest.main import app, container
from tests.mock.repository import MockRepository
from tests.mock.caster_service import MockCasterService


@pytest.fixture(scope='class')
def client():
    """
    Клиент для тестирования
    """

    container.repository.override(MockRepository())
    return TestClient(app)


@pytest.fixture(scope='class')
def client_mocked_caster_service():

    container.repository.override(MockRepository())
    container.caster_service.override(MockCasterService())
    return TestClient(app)
