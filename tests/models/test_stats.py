import pytest

from pydantic import ValidationError

from app.core.models.stats import Stats


params_stats_valid = [
    ({  # валидный
        'intelligence': 16,
        'wisdom': 10,
        'charisma': 10,
    }),
]


@pytest.mark.parametrize("data", params_stats_valid)
def test_valid_stats(data):
    stats = Stats(**data)
    assert stats.intelligence == data.get('intelligence')
    assert stats.wisdom == data.get('wisdom')
    assert stats.charisma == data.get('charisma')


params_stats_invalid = [
    ({  # неверные значения характеристик
        'intelligence': 16,
        'wisdom': 7,
        'charisma': 31,
    }),
    ({  # переданы не все характеристики
        'intelligence': 16,
    }),
    ({  # не передана ни одна характеристика
    }),
]


@pytest.mark.parametrize("data", params_stats_invalid)
def test_create_invalid(data):
    with pytest.raises(ValidationError):
        Stats(**data)
