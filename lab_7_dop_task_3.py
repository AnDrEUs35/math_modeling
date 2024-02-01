import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def drawing_star(t, a):
    x = 12 * np.cos(t) + 8 * np.cos(1.5 * t)
    y = 12 * np.sin(t) - 8 * np.sin(1.5 * t)
    
    X = x * np.cos(a) - y * np.sin(a)
    Y = y * np.cos(a) + x * np.sin(a)
    return X, Y


def animate(i):
    star.set_data(drawing_star(t=np.linspace(0, 4 * np.pi, 100), a=i))

if __name__ == '__main__':
    fig, ax = plt.subplots()
    star, = plt.plot([], [], '-', color='yellow')

    edge = 25
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=np.linspace(0, 2 * np.pi, 100), interval=60)
    ani.save('animation_dop_lab_3.gif')


