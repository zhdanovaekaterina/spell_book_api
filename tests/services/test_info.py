import pytest

from app.core.models.spell import SpellAggregate
from tests.mock.params import params_available_for_class


@pytest.mark.parametrize("data, expected_spells", params_available_for_class)
def test_get_available(info_service, data, expected_spells):

    spells = info_service.get_available(**data)
    assert spells == SpellAggregate(input=expected_spells)  # todo: работа с мок-данными, которая зависит от тестов агрегата
