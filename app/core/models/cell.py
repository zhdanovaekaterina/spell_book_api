from collections.abc import Mapping

from app.core.models.const import MIN_SPELL_LEVEL, MAX_SPELL_LEVEL, MIN_CELL_COUNT, MAX_CELL_COUNT


class CellAggregate(dict):

    def __init__(self, *data):
        super().__init__()
        if not data:
            return

        items = data[0].items() if isinstance(data[0], Mapping) else data[0]
        for key, value in items:
            self[key] = value

    def __setitem__(self, key, value):

        if key < MIN_SPELL_LEVEL or key > MAX_SPELL_LEVEL:
            raise KeyError("Невалидное значение ячейки")
        if value < MIN_CELL_COUNT or value > MAX_CELL_COUNT:
            raise ValueError("Невалидное количество ячеек")
        super().__setitem__(key, value)

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __missing__(self, key):
        self[key] = MIN_CELL_COUNT
        return MIN_CELL_COUNT
    
    @property
    def data(self):
        return dict(self)
