from tasks.common import MyException


def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """

    def wrapper(arg):
        if type(arg) == int and arg >= 0:
            res = func(arg)
        else:
            raise MyException

        return res

    return wrapper


def cash_factorial(func):
    factorial_values_dict = {}

    def wrapper(arg):
        if arg in factorial_values_dict:
            res = factorial_values_dict[arg]
        else:
            res = func(arg)
            factorial_values_dict[arg] = res

        return res

    return wrapper


@check_value
@cash_factorial
def factorial(number):
    """
    Возвращает факториал переданного числа
    Args:
        number: число, для которого надо посчитать факториал

    Returns:
        product - int - факториал от number
    """
    product = 1
    for element in range(1, number + 1):
        product *= element

    return product
