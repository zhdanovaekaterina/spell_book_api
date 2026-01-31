from collections import defaultdict

from app.core.models.const import MIN_SPELL_LEVEL, MAX_SPELL_LEVEL, MIN_CELL_COUNT, MAX_CELL_COUNT


class CellAggregate(dict):

    def __init__(self, *data):
        self._data = defaultdict(int)

        # если получили на вход список, пробуем обработать его как список пар
        if len(data) > 0 and isinstance(data[0], list):
            for item in data[0]:
                self[item[0]] = item[1]

    def __setitem__(self, key, value):

        if key < MIN_SPELL_LEVEL or key > MAX_SPELL_LEVEL:
            raise KeyError("Невалидное значение ячейки")
        if value < MIN_CELL_COUNT or value > MAX_CELL_COUNT:
            raise ValueError("Невалидное количество ячеек")
        
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return repr(self._data)
    
    @property
    def data(self):
        return self._data
