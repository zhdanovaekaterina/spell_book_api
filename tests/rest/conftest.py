import pytest
from fastapi.testclient import TestClient

from app.rest.main import app, container
from tests.mock.repository import MockRepository


@pytest.fixture(scope='class')
def client():
    """
    Клиент для тестирования
    """

    container.repository.override(MockRepository())
    return TestClient(app)
