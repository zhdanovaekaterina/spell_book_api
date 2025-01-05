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
    }
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
