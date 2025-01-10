"""
Тесты для коннектора к реляционной БД (заклинания и связи с классами).
Закрывают функционал выборок с помощью ORM.
Для тестирования используется in-memory sqlite
"""

import pytest

from app.core.interfaces.dto import ParamsToGetSpellsAvailable
from tests.mock.params import params_available_for_class


@pytest.mark.parametrize("data, expected_spells", params_available_for_class)
def test_get_available_spells(full_db_spells, data, expected_spells):
    params = ParamsToGetSpellsAvailable(**data)
    spell_list = full_db_spells.get_available_spells(params)
    assert expected_spells == [res.model_dump() for res in spell_list]
