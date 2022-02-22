from time import sleep
from tasks.common import MyException


def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """

    def decorator(func):

        def wrapper(*args,**kwargs):

            for i in range(times):
                try:
                    res = func()
                    return res
                except Exception:
                    sleep(delay)

            raise MyException

        return wrapper

    return decorator
