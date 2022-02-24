class Tuple:
    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """

    def __init__(self, *args, **kwargs):
        self.tuple_values = tuple(args)

    def __getitem__(self, index):
        return self.tuple_values[index]

    def count(self, value) -> int:
        """
        Возвращает количество появлений value в объекте.

        Args:
            value: количество вхождений в объекте
        """

        count = 0
        for t_value in self.tuple_values:
            if t_value == value:
                count += 1
        return count

    def index(self, value) -> int:
        """
        Возвращает индекс первого вхождения элемента в объекте.

        Args:
            value: индекс искомого элемента
        """
        for t_index, t_value in enumerate(self.tuple_values):
            if value == t_value:
                return t_index
        raise ValueError
