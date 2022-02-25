class MathClock:
    def __init__(self):
        self.minutes = 0

    def __add__(self, x):
        self.minutes = self.minutes + x

    def __radd__(self, x):
        self.minutes = self.minutes + x

    def __sub__(self, x):
        self.minutes = self.minutes - x

    def __mul__(self, x):
        self.minutes = self.minutes + 60 * x

    def __truediv__(self, x):
        self.minutes = self.minutes - 60 * x

    def __floordiv__(self, x):
        self.minutes = self.minutes - 60 * x

    def get_time(self):
        self.minutes = int(self.minutes)
        minutes = self.minutes % 60
        hours = self.minutes // 60 % 24

        return f'{hours:02}:{minutes:02}'
