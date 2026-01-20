import pytest

from app.core.models.spell import SpellAggregate
from app.core.models.cell import CellAggregate
from tests.mock.params import params_available_for_class, params_cell_for_class


@pytest.mark.parametrize("data, expected_spells", params_available_for_class)
def test_get_available(info_service, data, expected_spells):

    spells = info_service.get_available(**data)
    assert spells == SpellAggregate(input=expected_spells)  # todo: работа с мок-данными, которая зависит от тестов агрегата


@pytest.mark.parametrize("data, expected_cells", params_cell_for_class)
def test_get_cells(info_service, data, expected_cells):

    cells = info_service.get_cells(**data)
    assert isinstance(cells, CellAggregate)
    assert cells.data == expected_cells
