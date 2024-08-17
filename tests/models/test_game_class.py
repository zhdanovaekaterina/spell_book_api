import pytest

from pydantic import ValidationError

from app.core.models.game_class import GameClass
from tests.models.fixtures import di


params_class_valid = [
    ({  # валидный
        'alias': 'wizard',
    }),
    ({  # с подклассом
        'alias': 'cleric',
        'subclass': 'life',
    }),
    ({  # уровня выше 1
        'alias': 'wizard',
        'subclass': 'transmutation',
        'level': 5
    }),
]


@pytest.mark.parametrize("data", params_class_valid)
def test_create_valid(di, data):
    game_class = GameClass(**data)
    assert game_class.alias == data.get('alias')
    assert game_class.subclass == data.get('subclass')

    if not data.get('level'):
        assert game_class.level == 1
    else:
        assert game_class.level == data.get('level')


params_class_invalid = [
    ({  # без данных
    }),
    ({  # с неверным подклассом
        'alias': 'cleric',
        'subclass': 'transmutation',
    }),
    ({  # не передан подкласс, когда он нужен
        'alias': 'cleric',
    }),
    ({  # неверное значение класса
        'alias': 'wizarddddd',
    }),
    ({  # неверное значение подкласса
        'alias': 'cleric',
        'subclass': 'lifeeeee',
    }),
    ({  # неверное значение уровня
        'alias': 'wizard',
        'subclass': 'transmutation',
        'level': 0
    }),
    ({  # неверное значение уровня
        'alias': 'wizard',
        'subclass': 'transmutation',
        'level': 21
    }),
]


@pytest.mark.parametrize("data", params_class_invalid)
def test_create_invalid(di, data):
    with pytest.raises(ValidationError):
        GameClass(**data)


def test_create_excess(di):
    data = {
        # передан подкласс для класса, который его не требует на 1 уровне
        # - ожидаем класс без подкласса
        'alias': 'wizard',
        'subclass': 'transmutation',
    }

    game_class = GameClass(**data)
    assert game_class.subclass is None
