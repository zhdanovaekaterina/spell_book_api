# таблица классов
game_class_table_data = [
    {
        'alias': 'wizard',
        'title': 'Волшебник',
        'choose_subclass_level': 2,
    },
    {
        'alias': 'cleric',
        'title': 'Жрец',
        'choose_subclass_level': 1,
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
