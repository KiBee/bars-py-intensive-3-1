def error_checker(filename):
    """
    Функция-генератор возвращающая строки, содеражащие подстроку 'error'

    Args:
        filename: имя файла

    Yields:
        Итератор по строкам файла, содержащим 'error'
    """
    with open(filename, 'r') as file:
        for line in file:
            if 'error' in line.lower():
                yield line


for i in error_checker('log.txt'):
    print(i, end='')
