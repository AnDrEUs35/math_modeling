import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def drawing_star(t):
    x = 12 * np.cos(t) + 8 * np.cos(1.5 * t)
    y = 12 * np.sin(t) - 8 * np.sin(1.5 * t)
    return x, y
def spin_star(t, x, y):
    X = x * np.cos(t) - y * np.sin(t)
    Y = x * np.sin(t) + y * np.cos(t)


def animate(i):
    star.set_data(drawing_star(t=np.arange(0, 4 * np.pi, 0.001)))
    
if __name__ == '__main__':
    fig, ax = plt.subplots()
    star, = plt.plot([], [], 'o', color='yellow')

    edge = 25
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=180, interval=60)
    ani.save('animation_dop_lab_3.gif')


