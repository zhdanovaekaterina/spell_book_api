"""
Тесты для коннектора к реляционной БД.
Закрывают функционал выборок с помощью ORM.
Для тестирования используется in-memory sqlite
"""

import pytest

from app.core.models.caster import Caster as CoreCaster
from app.core.interfaces.dto import GameClassInfo
from app.repository.db.models import Caster as DbCaster, CasterClass as DbCasterClass
from tests.db.params import game_class_result


@pytest.mark.dependency(name="one_class")
def test_one_class(full_db):
    first_class = game_class_result[0]

    one_class = full_db.get_one_class(first_class.get('alias'))
    assert type(one_class) is GameClassInfo
    assert one_class.alias == first_class.get('alias')
    assert (one_class.choose_subclass_level
            == first_class.get('choose_subclass_level'))
    assert len(one_class.subclasses) == len(first_class.get('subclasses'))


def test_get_non_existing_class(full_db):
    with pytest.raises(KeyError):
        full_db.get_one_class('wizarddd')


@pytest.mark.dependency(depends=["one_class"])
def test_get_all_classes(full_db):
    all_classes = full_db.get_all_classes()
    assert len(all_classes) == len(game_class_result)
    assert type(all_classes[0]) is GameClassInfo


# todo: по факту зависит еще и от успешного прохождения
#  тестов на создание модели - tests.models.test_caster
@pytest.mark.dependency(name="save_caster", depends=["one_class"])
def test_save_caster(full_db):
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
    caster_id = full_db.add_caster(caster)  # act
    assert type(caster_id) is int
    assert caster_id == 1

    with full_db.session:
        rows_count = full_db.session.query(DbCaster.id).count()
        assert rows_count == 1

        caster_from_db = full_db.session.query(DbCaster).one()
        assert caster_from_db.name == data.get('name')
        assert caster_from_db.caster_class[0].class_alias\
            == data.get('classes')[0].get('alias')


@pytest.mark.dependency(name="get_caster", depends=["save_caster"])
def test_get_caster(full_db):
    caster = full_db.get_caster(1)  # act
    assert type(caster) is CoreCaster
    assert caster.name == 'Player1'
    assert caster.classes[0].alias == 'wizard'


@pytest.mark.dependency(name="get_caster_non_exist", depends=["save_caster"])
def test_get_caster_non_exist(full_db):
    with pytest.raises(KeyError):
        full_db.get_caster(2)  # act - пытаемся получить несуществующую запись


@pytest.mark.dependency(depends=["save_caster", "get_caster_non_exist"])
def test_delete_caster(full_db):
    full_db.delete_caster(1)  # act
    with pytest.raises(KeyError):
        full_db.get_caster(1)  # если удаление успешно, получение выкинет ошибку

    with full_db.session:  # убедимся что связанная таблица также очищена
        rows_count = full_db.session.query(DbCasterClass.id).count()
        assert rows_count == 0


def test_delete_caster_non_exist(full_db):
    with pytest.raises(KeyError):
        full_db.delete_caster(2)  # act - пытаемся удалить несуществующую запись
