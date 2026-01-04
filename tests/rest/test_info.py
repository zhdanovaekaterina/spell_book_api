import pytest
from fastapi import status

from tests.mock.params import params_available_for_class_aggregated


@pytest.mark.parametrize("data, expected_spells", params_available_for_class_aggregated)
def test_get_available(client, data, expected_spells):

    # Получим доступные заклинания для песонажа
    response = client.get("/info/spells/available", params=data)
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert response_json["spells"] == expected_spells


params_not_available = [
    ({  # без данных
    },
        'missing'
    ),
    ({  # неверный уровень
        "alias": "wizard",
        "level": 21,
    },
        'less_than_equal'
    ),
    ({  # неверный класс
        "alias": "wizarddd",
    },
        'invalid_class'
    ),
    ({  # неверный подкласс для класса
        "alias": "cleric",
        "subclass": "subclass",
    },
        'invalid_subclass'
    ),
]


@pytest.mark.parametrize("data, expected_error_type", params_not_available)
def test_get_available_wrong(client, data, expected_error_type):
    response = client.get("/info/spells/available", params=data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    response_json = response.json()
    error_types = [e['type'] for e in response_json.get('detail')]
    assert expected_error_type in error_types
