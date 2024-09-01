from app.core.base.exc_type import CoreExcType


class CoreException(Exception):
    """
    Исключения, вызываемые ядром
    """

    _type: CoreExcType = CoreExcType.CORE_EXCEPTION
    _msg: str = ''

    def __init__(self, **kwargs):
        if kwargs:
            self._type = kwargs.get('type')
            self._msg = kwargs.get('msg')

    def __str__(self):
        if self._msg:
            return f'{self.__class__.__name__} have been raised; {self._msg}'
        else:
            return f'{self.__class__.__name__} have been raised'

    def error(self):
        return {
            'type': self._type.value,
            'msg': self._msg
        }


class NotFoundException(CoreException):
    _type: CoreExcType = CoreExcType.NOT_FOUND
