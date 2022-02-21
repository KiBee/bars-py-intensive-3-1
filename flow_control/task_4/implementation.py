from datetime import date


def next_month(some_date):
    if some_date.month == 12:
        return date(some_date.year + 1, 1, 1)
    else:
        return date(some_date.year, some_date.month + 1, 1)


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """

    # return some_date + datetime.timedelta(days=1)

    is_leap_year = ((some_date.year % 4 == 0) and (some_date.year % 100 != 0) or  # определяем, високосный ли год
                    (some_date.year % 400 == 0))

    mapper = {1: 31,  # январь
              2: 29 if is_leap_year else 28,  # февраль
              3: 31,  # март
              4: 30,  # апрель
              5: 31,  # май
              6: 30,  # июнь
              7: 31,  # июль
              8: 31,  # август
              9: 30,  # сентябрь
              10: 31,  # октябрь
              11: 30,  # ноябрь
              12: 31}  # декабрь

    if mapper.get(some_date.month) == some_date.day:
        return next_month(some_date)
    else:
        return date(some_date.year, some_date.month, some_date.day + 1)
