# таблица классов
game_class_table_data = [
    {
        'alias': 'wizard',
        'title': 'Волшебник',
        'choose_subclass_level': 2,
        'type': 'full',
    },
    {
        'alias': 'cleric',
        'title': 'Жрец',
        'choose_subclass_level': 1,
        'type': 'full',
    },
    {
        'alias': 'ranger',
        'title': 'Следопыт',
        'choose_subclass_level': 3,
        'type': 'half',
    },
]


# таблица подклассов
game_subclass_table_data = [
    {
        'class_alias': 'wizard',
        'alias': 'transmutation',
        'title': 'школа преобразования',
    },
    {
        'class_alias': 'wizard',
        'alias': 'evocation',
        'title': 'школа воплощения',
    },
    {
        'class_alias': 'cleric',
        'alias': 'life',
        'title': 'домен жизни',
    },
    {
        'class_alias': 'cleric',
        'alias': 'peace',
        'title': 'домен мира',
    },
    {
        'class_alias': 'cleric',
        'alias': 'light',
        'title': 'домен света',
    },
]


# таблица типов классов
game_class_type_table_data = [
    {
        'alias': 'full',
        'class_level': 1,
        'cell_level': 1,
        'cell_add_amount': 2,
    },
    {
        'alias': 'full',
        'class_level': 5,
        'cell_level': 3,
        'cell_add_amount': 2,
    },
    {
        'alias': 'full',
        'class_level': 17,
        'cell_level': 9,
        'cell_add_amount': 1,
    },
    {
        'alias': 'half',
        'class_level': 2,
        'cell_level': 1,
        'cell_add_amount': 2,
    },
    {
        'alias': 'half',
        'class_level': 5,
        'cell_level': 2,
        'cell_add_amount': 2,
    },
    {
        'alias': 'half',
        'class_level': 9,
        'cell_level': 3,
        'cell_add_amount': 2,
    },
]


# таблица заклинаний
spell_table_data = [
    {
        'id': 1,
        'alias': 'spell1',
        'title': 'spell_wizard_1lvl',
        'level': 1,
    },
    {
        'id': 2,
        'alias': 'spell2',
        'title': 'spell_wizard_5lvl',
        'level': 3,
    },
    {
        'id': 3,
        'alias': 'spell3',
        'title': 'spell_wizard_20lvl',
        'level': 9,
    },
    {
        'id': 4,
        'alias': 'spell4',
        'title': 'spell_cleric_1lvl',
        'level': 1,
    },
    {
        'id': 5,
        'alias': 'spell5',
        'title': 'spell_cleric_life_1lvl',
        'level': 1,
    },
    {
        'id': 6,
        'alias': 'spell6',
        'title': 'spell_wiz_cleric_5lvl',
        'level': 3,
    },
    {
        'id': 7,
        'alias': 'spell7',
        'title': 'spell_ranger_5lvl',
        'level': 2,
    },
    {
        'id': 8,
        'alias': 'spell8',
        'title': 'spell_ranger_9lvl',
        'level': 3,
    },
]


# таблица связей заклинаний с классами
spell_available_data = [
    {
        'class': 'wizard',
        'spells': [1, 2, 3, 6],
    },
    {
        'class': 'cleric',
        'spells': [4, 6],
    },
    {
        'class': 'cleric',
        'subclass': 'life',
        'spells': [5],
    },
    {
        'class': 'ranger',
        'spells': [7, 8],
    },
]


# Ожидаемый результат
game_class_result = [
    {
        'alias': 'wizard',
        'subclasses': ['transmutation', 'evocation'],
        'choose_subclass_level': 2
    },
    {
        'alias': 'cleric',
        'subclasses': ['life', 'peace', 'light'],
        'choose_subclass_level': 1
    }
]
