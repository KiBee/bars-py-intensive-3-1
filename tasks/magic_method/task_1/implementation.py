class Multiplier:
    def __init__(self, value):
        self.value = value

    def __add__(self, x):
        return Multiplier(self.value + x)

    def __radd__(self, x):
        return x + self.value

    def __sub__(self, x):
        return Multiplier(self.value - x)

    def __rsub__(self, x):
        return x - self.value

    def __mul__(self, x):
        return Multiplier(self.value * x)

    def __rmul__(self, x):
        return x * self.value

    def __truediv__(self, x):
        return Multiplier(self.value / x)

    def __rtruediv__(self, x):
        return x / self.value

    def __floordiv__(self, x):
        return Multiplier(self.value // x)

    def __rfloordiv__(self, x):
        return x // self.value

    def __iadd__(self, x):
        self.value = self.value + x

        return Multiplier(self.value)

    def __isub__(self, x):
        self.value = self.value - x

        return Multiplier(self.value)

    def get_value(self):
        return int(self.value)


class Hundred(Multiplier):
    """Множитель на 100"""

    def __init__(self, value):
        super().__init__(value * 100)


class Thousand(Multiplier):
    """Множитель на 1 000"""

    def __init__(self, value):
        super().__init__(value * 1000)


class Million(Multiplier):
    """Множитель на 1 000 000"""

    def __init__(self, value):
        super().__init__(value * 1000000)
