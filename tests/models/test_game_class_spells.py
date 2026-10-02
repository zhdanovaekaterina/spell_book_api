import pytest

from app.core.models.game_class import ParamsToGetSpellCount


params_game_class_spells_count_valid = [
    (
        {
            'alias': 'wizard',  # подкласс для этих рассчетов не нужен, но передан чтобы прошла валидация
            'level': 5,
        },
        {
            'prepare': 9,  # уровень + модификатор заклинательной характеристики
            'learn': 14,  # 6 (на 1 уровне) + 2 за каждый следующий
            'saving_throw': 15,  # 8 + бонус мастерства (от уровня) + модификатор заклинательной характеристики
            'attack_modifier': 7,  # бонус мастерства (от уровня) + модификатор заклинательной характеристики
        }
    ),
    (
        {
            'alias': 'wizard',  # уровень не передан, показываем для максимального
        },
        {
            'prepare': 25,
            'learn': 44,
            'saving_throw': 19,
            'attack_modifier': 11,
        }
    ),
    (
        {
            'alias': 'wizard',
            'level': 1,
        },
        {
            'prepare': 4,
            'learn': 6,
            'saving_throw': 13,
            'attack_modifier': 5,
        }
    ),
    (
        {
            'alias': 'cleric',  # класс-фуллкастер готовит заклинания, та же логика для druid
            'level': 5,
        },
        {  # атрибута 'learn' в ответе нет
            'prepare': 9,
            'saving_throw': 15,
            'attack_modifier': 7,
        }
    ),
    (
        {
            'alias': 'bard',  # класс-фуллкастер учит заклинания, та же логика для socherer
            'level': 5,
        },
        {  # атрибута 'prepare' в ответе нет
            'learn': 8,  # берется из таблицы, 4 на 1 уровне
            'saving_throw': 15,
            'attack_modifier': 7,
        }
    ),
    (
        {
            'alias': 'artificier',  # класс-полукастер готовит заклинания, та же логика для paladin
            'level': 5,
        },
        {
            'prepare': 6,  # половина уровня (округл вниз, min 1) + модификатор заклинательной характеристики
            'saving_throw': 15,
            'attack_modifier': 7,
        }
    ),
    (
        {
            'alias': 'ranger',  # класс-полукастер учит заклинания
            'level': 5,
        },
        {
            'learn': 4,  # берется из таблицы, 2 на 1 уровне
            'saving_throw': 15,
            'attack_modifier': 7,
        }
    ),
]


@pytest.mark.xfail
@pytest.mark.parametrize("data, expected", params_game_class_spells_count_valid)
def test_game_class_spells_count_valid(di, data, expected):
    # print(f"data: {data}, expected: {expected}")

    SPELL_CHAR_VALUE = 18
    game_class = ParamsToGetSpellCount(**data)
    spell_count = game_class.get_spells_count(SPELL_CHAR_VALUE)
    assert spell_count == expected
