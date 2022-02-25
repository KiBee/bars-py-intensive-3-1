class MathClock:
    def __init__(self):
        self.minutes = 0

    def __add__(self, x):
        self.minutes = self.minutes + x

    def __sub__(self, x):
        self.minutes = self.minutes - x

    def __mul__(self, x):
        self.minutes = self.minutes + 60 * x

    def __div__(self, x):
        self.minutes = self.minutes - 60 * x

    def get_time(self):
        minutes = self.minutes % 60
        hours = self.minutes // 60 % 24

        return "%02d:%02d" % (hours, minutes)
