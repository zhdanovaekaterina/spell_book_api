"""
Тесты для коннектора к реляционной БД (персонажи).
Закрывают функционал выборок с помощью ORM.
Для тестирования используется in-memory sqlite
"""

import pytest

from app.core import NotFoundException
from app.core.models.caster import Caster as CoreCaster
from app.repository.db.models import Caster as DbCaster, CasterClass as DbCasterClass


# todo: по факту зависит еще и от успешного прохождения
#  тестов на создание модели - tests.models.test_caster
@pytest.mark.dependency(scope="session",
                        name="save_caster",
                        depends=["tests/db/test_db_class.py::test_one_class"])
def test_save_caster(mock_db):
    data = {
        'name': 'Player1',
        'classes': [{
            'alias': 'wizard',
        }],
        'stats': {
            'intelligence': 16,
            'wisdom': 10,
            'charisma': 12,
        }
    }

    caster = CoreCaster(**data)
    caster_id = mock_db.add_caster(caster)  # act
    assert type(caster_id) is int
    assert caster_id == 1

    with mock_db.session:
        rows_count = mock_db.session.query(DbCaster.id).count()
        assert rows_count == 1

        caster_from_db = mock_db.session.query(DbCaster).one()
        assert caster_from_db.name == data.get('name')
        assert caster_from_db.caster_class[0].class_alias\
            == data.get('classes')[0].get('alias')


@pytest.mark.dependency(name="get_caster", depends=["save_caster"])
def test_get_caster(mock_db):
    caster = mock_db.get_caster(1)  # act
    assert type(caster) is CoreCaster
    assert caster.name == 'Player1'
    assert caster.classes[0].alias == 'wizard'


@pytest.mark.dependency(name="get_caster_non_exist", depends=["save_caster"])
def test_get_caster_non_exist(mock_db):
    with pytest.raises(NotFoundException):
        mock_db.get_caster(2)  # act - пытаемся получить несуществующую запись


@pytest.mark.dependency(depends=["save_caster", "get_caster_non_exist"])
def test_delete_caster(mock_db):
    mock_db.delete_caster(1)  # act
    with pytest.raises(NotFoundException):
        mock_db.get_caster(1)  # если удаление успешно, получение выкинет ошибку

    with mock_db.session:  # убедимся что связанная таблица также очищена
        rows_count = mock_db.session.query(DbCasterClass.id).count()
        assert rows_count == 0


def test_delete_caster_non_exist(mock_db):
    with pytest.raises(NotFoundException):
        mock_db.delete_caster(2)  # act - пытаемся удалить несуществующую запись
