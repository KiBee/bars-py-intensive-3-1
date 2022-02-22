import time


def time_execution(func):
    """
    Обертка, печатающая время выполнения функции.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start_time)
        return res

    return wrapper
