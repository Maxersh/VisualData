import random

class Die():

    def __init__(self, n_sides=6):
        self.n_sides = n_sides

    def roll(self):
        return random.randint(1, self.n_sides)