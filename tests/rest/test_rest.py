import pytest
from fastapi import status

from app.core.base.exc_type import CoreExcType


param_valid_caster = [
    ({
        "name": "Player",
        "game_class": "wizard",
        "intelligence": 16,
        "wisdom": 10,
        "charisma": 10
    }, 1),
]


# todo: зависит от тестов службы и модели кастера
@pytest.mark.dependency(name="create_valid")
@pytest.mark.parametrize("data, caster_id", param_valid_caster)
def test_create_valid(client, data, caster_id):
    # Создадим персонажа
    response = client.post("/caster/create", json=data)
    assert response.status_code == status.HTTP_201_CREATED
    response_json = response.json()
    assert response_json.get('id') == caster_id


param_invalid_caster = [
    ({  # без данных
    },
        'missing'
    ),
    ({  # не все параметры переданы
        "name": "Player",
        "game_class": "wizard",
        "intelligence": 16,
    },
        'missing'
    ),
    ({  # нет подкласса, когда он требуется
        "name": "Player",
        "game_class": "cleric",
        "intelligence": 10,
        "wisdom": 16,
        "charisma": 10
    },
        'missing_subclass'
    ),
    ({  # неверный класс
        "name": "Player",
        "game_class": "wizarddd",
        "intelligence": 10,
        "wisdom": 16,
        "charisma": 10
    },
        'invalid_class'
    ),
    ({  # неверный подкласс для класса
        "name": "Player",
        "game_class": "cleric",
        "game_subclass": "subclass",
        "intelligence": 10,
        "wisdom": 16,
        "charisma": 10
    },
        'invalid_subclass'
    ),
]


@pytest.mark.parametrize("data, expected_error_type", param_invalid_caster)
def test_create_invalid(client, data, expected_error_type):
    response = client.post("/caster/create", json=data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    response_json = response.json()
    error_types = [e['type'] for e in response_json.get('detail')]
    assert expected_error_type in error_types


@pytest.mark.dependency(depends=["create_valid"])
def test_get_existing(client):

    # arrange
    data = {
        "name": "Player",
        "game_class": "wizard",
        "intelligence": 16,
        "wisdom": 10,
        "charisma": 10
    }
    client.post('/caster/create', json=data)

    # act
    response = client.get("/caster/1")

    # assert
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert response_json.get('name') == 'Player'
    assert response_json.get('classes')[0].get('alias') == 'wizard'


def test_get_non_existing(client):

    response = client.get("/caster/1")
    assert response.status_code == status.HTTP_404_NOT_FOUND

    response_json = response.json()
    assert (response_json.get('detail')[0].get('type')
            == CoreExcType.NOT_FOUND.value)
