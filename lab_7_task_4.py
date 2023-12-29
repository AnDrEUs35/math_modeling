import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def drawing(C, D, y0, x0, n):
    

    x = x0 + xn ** 2 - yn ** 2 + C
    y = y0 + 2 * xn * yn + D
    return x, y

def animate(i):
    fractal.set_data(drawing(C=0.3, D=0.33, x0=0.1, y0=0.1, n=))

if __name__ == '__main__':
    fig, ax = plt.subplots()
    fractal, = plt.plot([], [], 'o', color='r', label='ball')

    edge = 10
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=360, interval=30)
    ani.save('animation_lab_4.gif')
