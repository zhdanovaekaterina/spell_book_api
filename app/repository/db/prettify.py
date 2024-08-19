class Prettify:
    """
    Дополнительные методы для читабельного вывода моделей
    """

    def public_attrs(self):
        return {x: y for x, y in self.__dict__.items() if not x.startswith('_')}

    def __repr__(self):
        public = self.public_attrs()

        string_pairs = [f'{key}="{getattr(self, key)}"' for key in public]
        attributes = ', '.join(string_pairs)
        class_name = self.__class__.__name__

        return f'<{class_name}: {attributes}>'
