from typing import List

from app.core.base.core_exception import NotFoundException


class MockCasterService():
    """
    Мок кастер-службы для проверки rest-модуля caster
    """
    
    def get_available(self, caster_id, **data) -> List[dict]:

        if caster_id == 1:
            return {
                "levels": [
                    0
                ],
                "count": 1,
                "spells": {
                    "0": [
                        {
                            "id": 1,
                            "alias": "some_spell",
                            "title": "Заклинание",
                            "level": 0
                        }
                    ]
                }
            }
        else:
            raise NotFoundException
