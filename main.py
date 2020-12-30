import matplotlib.pyplot as plt
import pygal
from random_walk import RandomWalk

point_numbers = list(range(30))

walk = RandomWalk(len(point_numbers))
for i in range(1):
    walk.fill()
    walk.paint()
    #print(walk.colors)
    plt.scatter(walk.x_values, walk.y_values, c=walk.colors,
                cmap=plt.cm.Blues, edgecolor='none', s=6)
    #plt.scatter(0, 0, c='green', edgecolors='none', s=80)
    #plt.scatter(walk.x_values[-1], walk.y_values[-1], c='red',
    #            edgecolors='none', s=80)
    walk.clear()
plt.savefig('squares_plot_new.png', bbox_inches='tight')
#plt.savefig('squares_plot.png', bbox_inches='tight')
#plt.show()