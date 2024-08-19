import pytest

from app.di import Container
from app.repository.db.models import Base, GameClass, GameSubclass
from tests.db.params import game_class_table_data, game_subclass_table_data


@pytest.fixture(scope='module')
def clean_db():
    """
    Возвращает пустую in-memory БД с инициализированной схемой
    """

    container = Container()
    container.config.from_dict({
        'db': {
            'url': 'sqlite:///:memory:',
            'registry': Base
        }
    })

    db = container.repository()
    db.registry.metadata.create_all(db.engine)  # Создание таблиц

    return db


@pytest.fixture(scope='module')
def full_db(clean_db):
    """
    Заполняет базу тестовыми данными
    :return:
    """

    game_class_obj_list = [GameClass(**d) for d in game_class_table_data]
    game_subclass_obj_list\
        = [GameSubclass(**d) for d in game_subclass_table_data]

    with clean_db.session as session:
        with session.begin():
            session.bulk_save_objects(game_class_obj_list)
            session.bulk_save_objects(game_subclass_obj_list)

    return clean_db
