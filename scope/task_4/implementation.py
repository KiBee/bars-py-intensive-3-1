def bad_open(file_path, mode):
    """Некорректная функция открытия файла"""
    raise Exception


def open_and_close_file(file_path):
    """Открывет и закрывает файл

    Args:
        file_path: путь до файла
    """
    open = bad_open

    ###
    # Добавьте свой код сюда
    # open = __builtins__['open']  # присваиваем переменной встроенный open

    # Переопределяем битую функцию локальной функцией, которая будет вызывать глобальный open
    def global_open(file_path, mode):
        global open
        return open(file_path, mode)

    open = global_open

    ###
    f = open(file_path, 'r')
    f.close()
