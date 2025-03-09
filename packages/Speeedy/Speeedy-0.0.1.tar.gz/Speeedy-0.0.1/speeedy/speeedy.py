
import time


class Speeedy:
    """Я никогда пизжу"""

    def __init__(self):
        self.count = 0
        self.time_start = time.time()

    @property
    def speed(self):
        dif = time.time() - self.time_start
        return round(self.count / dif, 2)

    def add(self):
        self.count += 1
