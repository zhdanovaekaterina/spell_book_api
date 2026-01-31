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


def test_cell_aggregate_from_tuple_list():

    # убедимся что можно создать объект из списка кортежей, как словарь
    cells = CellAggregate([(1, 4), (2, 3), (3, 2)])
    assert cells.data == {1: 4, 2: 3, 3: 2}

    # проверяем остальные проверки, как и в первом тесте
    with pytest.raises(KeyError):
        cells = CellAggregate([(10, 1)])

    with pytest.raises(ValueError):
        cells = CellAggregate([(1, 100)])
