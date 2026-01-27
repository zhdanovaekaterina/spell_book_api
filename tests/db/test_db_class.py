"""
Тесты для коннектора к реляционной БД (игровые классы).
Закрывают функционал выборок с помощью ORM.
Для тестирования используется in-memory sqlite
"""

import pytest

from app.core.interfaces.dto import GameClassInfo
from tests.db.params import game_class_result


@pytest.mark.order(1)
@pytest.mark.dependency(scope="session")
def test_one_class(mock_db):
    first_class = game_class_result[0]

    one_class = mock_db.get_one_class(first_class.get('alias'))
    assert type(one_class) is GameClassInfo
    assert one_class.alias == first_class.get('alias')
    assert (one_class.choose_subclass_level
            == first_class.get('choose_subclass_level'))
    assert len(one_class.subclasses) == len(first_class.get('subclasses'))


def test_get_non_existing_class(mock_db):
    with pytest.raises(KeyError):
        mock_db.get_one_class('wizarddd')


@pytest.mark.dependency(depends=["test_one_class"])
def test_get_all_classes(mock_db):
    all_classes = mock_db.get_all_classes()
    assert len(all_classes) == len(game_class_result)
    assert type(all_classes[0]) is GameClassInfo
