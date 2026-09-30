from enum import Enum


class SpellCharacteristic(str, Enum):
    """
    Заклинательная характеристика класса
    """
    INT = 'intelligence'
    WIS = 'wisdom'
    CHA = 'charisma'
