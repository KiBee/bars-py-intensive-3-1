from tasks.common import MyException
class Value:
    def __init__(self, value):
        self.value = value


    def __add__(self, x):
        return self.value + x

    def __sub__(self, x):
        return self.value - x

    def __mul__(self, x):
        return self.value * x

    def __truediv__(self, x):
        if x == 0:
            raise MyException
        return self.value / x

    def __getattr__(self, x):
        raise MyException
    pass
