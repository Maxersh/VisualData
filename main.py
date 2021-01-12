import matplotlib.pyplot as plt
import pygal
from random_walk import RandomWalk
from die import Die
import time

die_1 = Die(6)
die_2 = Die(10)
N = 50000

results = [die_1.roll() + die_2.roll() for i in range(N)]
try:
    freqs = [results.count(value)/len(results)
             for value in range(2, die_1.n_sides + die_2.n_sides + 1)]
except:
    freqs = [0 for i in range(2, die_1.n_sides + die_2.n_sides + 1)]

hist = pygal.Bar()

hist.title = "Results of rolling D6+D10 1000 times."
hist.x_labels = [str(i) for i in range(2, die_1.n_sides + die_2.n_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D6+D10', freqs)

hist.render_to_file('die_visual.svg')
