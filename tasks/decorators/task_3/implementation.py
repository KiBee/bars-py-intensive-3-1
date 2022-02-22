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

    return wrapper
