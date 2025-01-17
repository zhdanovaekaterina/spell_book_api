from app.core.models.spell import SpellAggregate, Spell
from tests.models.params import spell_list


def test_spell_aggregate():
    assert len(spell_list) == 5

    aggr = SpellAggregate(input=spell_list)

    assert len(aggr) == 4  # убедимся что дубль не попал в коллекцию
    assert aggr.spells.get(2) is None  # убедимся что несуществующий уровень дает None
    assert type(aggr.spells.get(1)[0]) == Spell  # проверим тип
    assert aggr.spells.get(1)[0] == Spell(**spell_list[1])  # проверим одно заклинание
    assert aggr.levels == [1, 3, 9]  # проверим список уровней
