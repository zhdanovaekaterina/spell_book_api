"""
Тесты для коннектора к реляционной БД (заклинания и связи с классами).
Закрывают функционал выборок с помощью ORM.
Для тестирования используется in-memory sqlite
"""

import pytest

from app.core.models.game_class import ParamsToGetSpellsAvailable
from app.core.models.spell import Spell, SpellAggregate
from tests.mock.params import params_available_for_class


@pytest.mark.parametrize("data, expected_spells", params_available_for_class)
def test_get_available_spells(mock_db, data, expected_spells):
    params = ParamsToGetSpellsAvailable(**data)
    spell_list = mock_db.get_available_spells(params)

    assert isinstance(spell_list, SpellAggregate)
    assert SpellAggregate(input=[Spell(**e) for e in expected_spells]) == spell_list  # todo: слишком много тут работы с мок-данными, которая зависит от тестов агрегата
