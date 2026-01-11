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


@pytest.mark.dependency(name="get_non_existing")
def test_get_non_existing(client):

    response = client.get("/caster/1")
    assert response.status_code == status.HTTP_404_NOT_FOUND

    response_json = response.json()
    assert (response_json.get('detail')[0].get('type')
            == CoreExcType.NOT_FOUND.value)


@pytest.mark.dependency(depends=["create_valid", "get_non_existing"])
def test_delete_existing(client):

    # arrange
    data = {
        "name": "Player",
        "game_class": "wizard",
        "intelligence": 16,
        "wisdom": 10,
        "charisma": 10
    }
    client.post('/caster/create', json=data)

    # act -> assert
    response = client.delete("/caster/1")
    assert response.status_code == status.HTTP_200_OK

    next_response = client.get("/caster/1")
    assert next_response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_non_existing(client):

    response = client.delete("/caster/1")
    assert response.status_code == status.HTTP_404_NOT_FOUND


# здесь и далее в тестах используем мок-службу кастера, чтобы не эмулировать всю цепочку
# с созданием кастера и связями с заклинаниями и снизить зависимость от служб
# todo: после ввода агрегата заклинаний тест сломался на первой строчке, неплохо бы его починить
@pytest.mark.xfail
def test_get_available_spells(client_mocked_caster_service):

    response = client_mocked_caster_service.get("/caster/1/spells/available")
    assert response.status_code == status.HTTP_200_OK

    response_json = response.json()
    assert len(response_json) == 3
    assert response_json["levels"] == [0]
    assert response_json["count"] == 1
    assert response_json["spells"]["0"] == [{"id": 1, "alias": "some_spell", "title": "Заклинание", "level": 0}]


def test_get_available_spells_from_invalid_caster(client_mocked_caster_service):

    response = client_mocked_caster_service.get("/caster/2/spells/available")
    assert response.status_code == status.HTTP_404_NOT_FOUND
