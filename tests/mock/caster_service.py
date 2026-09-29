from typing import List

from app.core import SpellAggregate
from app.core.base.core_exception import NotFoundException


class MockCasterService():
    """
    Мок кастер-службы для проверки rest-модуля caster
    """
    
    def get_available(self, caster_id, **data) -> List[dict]:

        if caster_id == 1:
            return SpellAggregate(input=[
                {
                    "id": 1,
                    "alias": "some_spell",
                    "title": "Заклинание",
                    "level": 0,
                }
            ])
        else:
            raise NotFoundException

    def get_cells(self, caster_id) -> dict:

        if caster_id == 2:
            return {1: 2}
