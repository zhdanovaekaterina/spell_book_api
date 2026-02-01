import pytest

from app.core.models.game_class import ParamsToGetCellsAvailable
from app.core.models.cell import CellAggregate
from tests.mock.params import params_cell_for_class


@pytest.mark.parametrize("data, expected_cells", params_cell_for_class)
def test_get_cells(mock_db, data, expected_cells):
    """
    Получение ячеек заклинаний из БД
    """

    params = ParamsToGetCellsAvailable(**data)
    cells = mock_db.get_cells(params)

    assert isinstance(cells, CellAggregate)
    assert cells.data == expected_cells
