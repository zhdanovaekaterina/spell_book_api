import pytest

from app.core.models.cell import CellAggregate


def test_cell_aggregate():

    # убедимся что возможно создать словарь с адекватными ключами
    cells = CellAggregate()
    cells[1] += 1  # убедимся что можно добавить значение через += к несуществующему ключу

    assert cells.data == {1: 1}

    # убедимся что нельзя добавить ключ, который не соответствует возможному уровню ячейки
    with pytest.raises(KeyError):
        cells[10] += 1

    # убедимся что нельзя задать неадекватное значение
    with pytest.raises(ValueError):
        cells[1] += 100
    
    # также убедимся что нельзя выйти за пределы допустимых значений при инкременте
    with pytest.raises(ValueError):
        cells[2] += 3
        cells[2] += 3  # здесь уже должна вывалиться ValueError
