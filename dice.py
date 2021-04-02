import random

class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Sides must be a whole number")
        if not isinstance (sides, int):
            raise ValueError("Sides must be a whole number")
        self.value = value or random.randint(1, sides)