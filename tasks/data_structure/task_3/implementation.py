import copy


def copy_dict(origin_dict: dict) -> dict:
    """
    Функция возвращает копию словаря.
    """
    return copy.deepcopy(origin_dict)
