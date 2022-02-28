from contextlib import contextmanager


@contextmanager
def open_file(path, mode):
    """
    Функция - менеджер контекста с функцией вывода количества строк в файле

    Args:
        path: путь к файлу,
        mode: режим, в котором будет открываться файл

    Raises:
        FileNotFoundError: Если файл не существует, а выбранный режим не позволяет его создать
    """

    try:
        f = open(path, 'r')
        line_count = sum(1 for _ in f)
        f.close()
        f = open(path, mode)

    except FileNotFoundError:
        if 'w' in mode or 'a' in mode:
            f = open(path, mode)
            line_count = 0
        else:
            raise FileNotFoundError

    print('Cтрок в файле:', line_count)
    yield f
    f.close()


with open_file('sample_submission.csv', 'r') as file:
    print(file.readline())
    pass
