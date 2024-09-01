from enum import Enum


class CoreExcType(str, Enum):
    CORE_EXCEPTION: str = 'core_exception'
    INVALID_CLASS: str = 'invalid_class'
    INVALID_SUBCLASS: str = 'invalid_subclass'
    MISSING_SUBCLASS: str = 'missing_subclass'
    NOT_FOUND: str = 'not_found'
