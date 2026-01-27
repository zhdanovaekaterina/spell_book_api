import pytest
from sqlalchemy import event

from app.di import Container
from app.repository.db.models import Base


@pytest.fixture(scope='module')
def mock_db():
    """
    Возвращает in-memory БД с инициализированной схемой, заполненную тестовыми данными
    """

    # инициализируем базу
    container = Container()
    container.config.from_dict({
        'db': {
            'url': 'sqlite:///:memory:',
            'registry': Base
        }
    })
    container.wire(modules=[
        'app.core.models.game_class'
    ])

    db = container.repository()

    # включаем поддержку внешних ключей для sqlite
    @event.listens_for(db.engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

    # создаем таблицы
    db.registry.metadata.create_all(db.engine)

    # наполняем БД мок-данными
    with open("tests/db/init.sql", "r") as file:
        data = file.read()

    with db.engine.begin() as conn:
        conn.connection.executescript(data)

    return db
