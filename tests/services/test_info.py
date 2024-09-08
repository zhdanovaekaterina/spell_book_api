import pytest

from tests.mock.params import params_available_for_class


@pytest.mark.parametrize("data, expected_spells", params_available_for_class)
def test_get_available(info_service, data, expected_spells):

    spells = info_service.get_available(**data)
    assert spells == expected_spells
