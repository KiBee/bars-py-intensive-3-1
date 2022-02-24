def counter(func):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """
    counter.count = 0

    def wrapper(*args, **kwargs):
        counter.count += 1
        func(*args, **kwargs)
        return counter.count

    """ 
    Использование counter перед count явно говорит о том, что используется 
    поле внешней функции counter. Вместо этого можно было использовать nonlocal, 
    но такой метод более наглядный на мой взгляд.
    """
    return wrapper
