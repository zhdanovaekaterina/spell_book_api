import pytest

from pydantic import ValidationError

from app.core.models.caster import Caster


params_new_caster_valid = [
    ({  # валидный
        'name': 'Player1',
        'classes': [{
            'alias': 'wizard',
        }],
        'stats': {
            'intelligence': 16,
            'wisdom': 10,
            'charisma': 10,
        }
    }),
]


@pytest.mark.parametrize("data", params_new_caster_valid)
def test_create_valid(di, data):
    caster = Caster(**data)
    assert caster.name == data.get('name')


params_new_caster_invalid = [
    ({  # без данных
    }),
    ({  # без имени
        'classes': [{
            'alias': 'wizard',
        }],
        'stats': {
            'intelligence': 16,
            'wisdom': 10,
            'charisma': 10,
        }
    }),
    ({  # без класса
        'name': 'Player1',
        'stats': {
            'intelligence': 16,
            'wisdom': 10,
            'charisma': 10,
        }
    }),
    ({  # без характеристик
        'name': 'Player1',
        'classes': [{
            'alias': 'wizard',
        }],
    }),
]


@pytest.mark.parametrize("data", params_new_caster_invalid)
def test_create_invalid(di, data):
    with pytest.raises(ValidationError):
        Caster(**data)
