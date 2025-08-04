from typing import List

from app.core.base.core_exception import NotFoundException


class MockCasterService():
    """
    Мок кастер-службы для проверки rest-модуля caster
    """
    
    def get_available(self, caster_id, **data) -> List[dict]:

        if caster_id == 1:
            return [
                {'id': 1, 'alias': 'spell1', 'title': 'some_spell_title_to_check', 'level': 1},
                {'id': 2, 'alias': 'spell2', 'title': 'spell_wizard_1lvl2', 'level': 1},
            ]
        else:
            raise NotFoundException
