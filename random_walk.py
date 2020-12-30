from random import choice

class RandomWalk():

    def __init__(self, num_points=500):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

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

    def clear(self):
        self.x_values = [0]
        self.y_values = [0]