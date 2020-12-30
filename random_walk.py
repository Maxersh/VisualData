from random import choice
from time import time
class RandomWalk():

    def __init__(self, num_points=500):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

        self.colors = []


    def fill(self):

        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            y_direction = choice([1, -1])

            x_step = choice([1, 2, 3, 4])
            y_step = choice([1, 2, 3, 4])

            x_new_val = x_direction * x_step + self.x_values[-1]
            y_new_val = y_direction * y_step + self.y_values[-1]

            self.x_values.append(x_new_val)
            self.y_values.append(y_new_val)

    def paint(self):

        gap = 4
        points = zip(self.x_values, self.y_values)
        for point in (self.x_values, self.y_values):
            number = 0
            print(point)
            for pnt in (self.x_values, self.y_values):
                print(pnt)
                number += int(abs(pnt[0] - point[0]) <= gap and abs(pnt[1] - point[1]) <= gap)
            print('!!{}'.format(number))
            number -= 1
            self.colors.append(number)
        print(self.colors)

    def clear(self):
        self.x_values = [0]
        self.y_values = [0]
        self.colors = []