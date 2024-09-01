import pytest

from pydantic import ValidationError

from app.core.base.exc_type import CoreExcType
from app.core.models.game_class import GameClass


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
    },
        'missing',
        'Field required'
    ),
    ({  # с неверным подклассом
        'alias': 'cleric',
        'subclass': 'transmutation',
    },
        CoreExcType.INVALID_SUBCLASS.value,
        'invalid subclass provided'
    ),
    ({  # не передан подкласс, когда он нужен
        'alias': 'cleric',
    },
        CoreExcType.MISSING_SUBCLASS.value,
        'on level 1 must have a subclass'
    ),
    ({  # неверное значение класса
        'alias': 'wizarddddd',
    },
        CoreExcType.INVALID_CLASS.value,
        "invalid class 'wizarddddd' provided"
    ),
    ({  # неверное значение подкласса
        'alias': 'cleric',
        'subclass': 'lifeeeee',
    },
        CoreExcType.INVALID_SUBCLASS.value,
        'invalid subclass provided'
    ),
    ({  # неверное значение уровня
        'alias': 'wizard',
        'subclass': 'transmutation',
        'level': 0
    },
        'greater_than_equal',
        'should be greater than or equal to 1'
    ),
    ({  # неверное значение уровня
        'alias': 'wizard',
        'subclass': 'transmutation',
        'level': 21
    },
        'less_than_equal',
        'should be less than or equal to 20'
    ),
]


@pytest.mark.parametrize(
    "data, expected_error_type, expected_error_msg",
    params_class_invalid
)
def test_create_invalid(di, data, expected_error_type, expected_error_msg):
    with pytest.raises(ValidationError) as exc_info:
        GameClass(**data)

    error_types = [e.get('type') for e in exc_info.value.errors()]
    assert expected_error_type in error_types

    error_msg = [e.get('msg') for e in exc_info.value.errors()][0]
    assert expected_error_msg in error_msg


def test_create_excess(di):
    data = {
        # передан подкласс для класса, который его не требует на 1 уровне
        # - ожидаем класс без подкласса
        'alias': 'wizard',
        'subclass': 'transmutation',
    }

    game_class = GameClass(**data)
    assert game_class.subclass is None
