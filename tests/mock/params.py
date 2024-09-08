# Мок-данные для связей класса, подкласса, уровня и заклинаний
params_available_for_class = (
    (  # без указания уровня должны вернуться все доступные заклинания
        # для класса
        {
            'game_class': 'wizard'
        },
        [
            {'id': 1, 'alias': 'spell', 'title': 'spell_wizard_1lvl'},
            {'id': 2, 'alias': 'spell', 'title': 'spell_wizard_5lvl'},
            {'id': 3, 'alias': 'spell', 'title': 'spell_wizard_20lvl'},
            {'id': 6, 'alias': 'spell', 'title': 'spell_wiz_cleric_5lvl'},
        ]
    ),
    (  # на первом уровне - получаем только доступные первому
        {
            'game_class': 'wizard',
            'level': 1
        },
        [
            {'id': 1, 'alias': 'spell', 'title': 'spell_wizard_1lvl'},
        ]
    ),
    (  # на пятом уровне - доступные пятому (плюс одно общее)
        {
            'game_class': 'wizard',
            'level': 5
        },
        [
            {'id': 1, 'alias': 'spell', 'title': 'spell_wizard_1lvl'},
            {'id': 2, 'alias': 'spell', 'title': 'spell_wizard_5lvl'},
            {'id': 6, 'alias': 'spell', 'title': 'spell_wiz_cleric_5lvl'},
        ]
    ),
    (  # на первом уровне для класса, где требуется подкласс
        # - получаем только те, что доступны чистому классу
        {
            'game_class': 'cleric',
            'level': 1
        },
        [
            {'id': 4, 'alias': 'spell', 'title': 'spell_cleric_1lvl'},
        ]
    ),
    (  # если подкласс указан, получаем также заклинания для подкласса
        {
            'game_class': 'cleric',
            'game_subclass': 'c_life',
            'level': 1
        },
        [
            {'id': 4, 'alias': 'spell', 'title': 'spell_cleric_1lvl'},
            {'id': 5, 'alias': 'spell', 'title': 'spell_cleric_life_1lvl'},
        ]
    ),
    (  # убедимся что на пятом уровне получаем общее заклинание ...
        {
            'game_class': 'cleric',
            'level': 5
        },
        [
            {'id': 4, 'alias': 'spell', 'title': 'spell_cleric_1lvl'},
            {'id': 6, 'alias': 'spell', 'title': 'spell_wiz_cleric_5lvl'},
        ]
    ),
    (  # ... и это также работает, если указать подкласс
        {
            'game_class': 'cleric',
            'game_subclass': 'c_life',
            'level': 5
        },
        [
            {'id': 4, 'alias': 'spell', 'title': 'spell_cleric_1lvl'},
            {'id': 5, 'alias': 'spell', 'title': 'spell_cleric_life_1lvl'},
            {'id': 6, 'alias': 'spell', 'title': 'spell_wiz_cleric_5lvl'},
        ]
    ),
)
