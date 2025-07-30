from typing import List


class MockInfoService():
    """
    Мок инфо-службы для подстановки в CasterService
    """
    
    def get_available(self, **data) -> List[dict]:

        # по факту этой конструкцией сейчас мы просто проверяем, что по id получены верные
        # характеристики заклинателя
        if data.get("alias") == "wizard" and data.get("level") == 1:
            return [
                {'id': 1, 'alias': 'spell1', 'title': 'spell_wizard_1lvl', 'level': 1},
            ]
