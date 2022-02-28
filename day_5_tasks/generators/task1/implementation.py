def fib(n):
    """
    Функция-генератор возвращающая последовательность чисел Фибоначчи

    Args:
        n: количество чисел Фибоначчи

    Yields:
        Итератор по последовательности чисел Фибоначчи
    """
    first_number, second_number = 0, 1
    for _ in range(n):
        first_number, second_number = second_number, first_number + second_number
        yield first_number
