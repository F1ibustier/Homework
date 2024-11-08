# Интроспекция
# coded by f1ibustier
from pprint import pprint


def introspection_info(obj):
    type_obj = type(obj)

    metod_obj = [metod for metod in dir(obj) if callable(getattr(obj, metod))]

    attr_obj = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]

    module_obj = obj.__class__.__module__

    info = {'тип:':type_obj, 'методы:':metod_obj, 'атрибуты:':attr_obj, 'модуль:':module_obj}
    return info

number_info = introspection_info(42)
pprint(number_info)
