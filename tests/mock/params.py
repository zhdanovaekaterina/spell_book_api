# Мок-данные для связей класса, подкласса, уровня и заклинаний
params_available_for_class = (
    (  # без указания уровня должны вернуться все доступные заклинания
        # для класса
        {
            'game_class': 'wizard'
        },
        [
            {'id': 1, 'alias': 'spell1', 'title': 'spell_wizard_1lvl', 'level': 1},
            {'id': 2, 'alias': 'spell2', 'title': 'spell_wizard_5lvl', 'level': 3},
            {'id': 3, 'alias': 'spell3', 'title': 'spell_wizard_20lvl', 'level': 9},
            {'id': 6, 'alias': 'spell6', 'title': 'spell_wiz_cleric_5lvl', 'level': 3},
        ]
    ),
    (  # на первом уровне - получаем только доступные первому
        {
            'game_class': 'wizard',
            'level': 1
        },
        [
            {'id': 1, 'alias': 'spell1', 'title': 'spell_wizard_1lvl', 'level': 1},
        ]
    ),
    (  # на пятом уровне - доступные пятому (плюс одно общее)
        {
            'game_class': 'wizard',
            'level': 5
        },
        [
            {'id': 1, 'alias': 'spell1', 'title': 'spell_wizard_1lvl', 'level': 1},
            {'id': 2, 'alias': 'spell2', 'title': 'spell_wizard_5lvl', 'level': 3},
            {'id': 6, 'alias': 'spell6', 'title': 'spell_wiz_cleric_5lvl', 'level': 3},
        ]
    ),
    (  # на первом уровне для класса, где требуется подкласс
        # - получаем только те, что доступны чистому классу
        {
            'game_class': 'cleric',
            'level': 1
        },
        [
            {'id': 4, 'alias': 'spell4', 'title': 'spell_cleric_1lvl', 'level': 1},
        ]
    ),
    (  # если подкласс указан, получаем также заклинания для подкласса
        {
            'game_class': 'cleric',
            'game_subclass': 'life',
            'level': 1
        },
        [
            {'id': 4, 'alias': 'spell4', 'title': 'spell_cleric_1lvl', 'level': 1},
            {'id': 5, 'alias': 'spell5', 'title': 'spell_cleric_life_1lvl', 'level': 1},
        ]
    ),
    (  # убедимся что на пятом уровне получаем общее заклинание ...
        {
            'game_class': 'cleric',
            'level': 5
        },
        [
            {'id': 4, 'alias': 'spell4', 'title': 'spell_cleric_1lvl', 'level': 1},
            {'id': 6, 'alias': 'spell6', 'title': 'spell_wiz_cleric_5lvl', 'level': 3},
        ]
    ),
    (  # ... и это также работает, если указать подкласс
        {
            'game_class': 'cleric',
            'game_subclass': 'life',
            'level': 5
        },
        [
            {'id': 4, 'alias': 'spell4', 'title': 'spell_cleric_1lvl', 'level': 1},
            {'id': 6, 'alias': 'spell6', 'title': 'spell_wiz_cleric_5lvl', 'level': 3},
            {'id': 5, 'alias': 'spell5', 'title': 'spell_cleric_life_1lvl', 'level': 1},
        ]
    ),
    (  # а теперь попробуем сделать все то же самое для полукастера - соль в получении правильного уровня ячейки по уровню персонажа
        {
            'game_class': 'ranger',
            'level': 5
        },
        [
            {'id': 7, 'alias': 'spell7', 'title': 'spell_ranger_5lvl', 'level': 2},
        ]
    )
)
