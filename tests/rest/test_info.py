import pytest
from fastapi import status

from tests.mock.params import params_available_for_class


@pytest.mark.parametrize("data, expected_spells", params_available_for_class)
def test_get_available(client, data, expected_spells):

    # Получим доступные заклинания для песонажа
    # todo: ту же работу для конкретного персонажа должен делать метод GET "/caster/{caster_id}/spells/available" без параметров
    response = client.get("/info/spells/available", params=data)
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert response_json == expected_spells
