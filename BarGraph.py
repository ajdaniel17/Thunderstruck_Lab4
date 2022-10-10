import numpy as np
from matplotlib import animation as animation, pyplot as plt, cm

fig = plt.figure()

data = [1, 4, 3, 2, 6, 7, 5]
colors = ['red', 'yellow', 'blue', 'green', 'black']
bars = plt.bar(data, data, facecolor='green', alpha=0.75)

def animate(frame):
   global bars
   index = np.random.randint(1, 7)
   bars[frame].set_height(index)
   bars[frame].set_facecolor(colors[np.random.randint(0, len(colors))])

ani = animation.FuncAnimation(fig, animate, frames=len(data))

plt.show()