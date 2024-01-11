import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def drawing(C, D, y0, x0, time):
    xn1 = x0 * time
    yn1 = y0 * time
    xn = xn1 ** 2 - yn1 ** 2 + C
    yn = 2 * xn1 * yn1 + D
    return xn, yn

def animate(i):
    fractal.set_data(drawing(C=0.3, D=0.33, x0=0.1, y0=0.1, time=i))

if __name__ == '__main__':
    fig, ax = plt.subplots()
    fractal, = plt.plot([], [], 'o', color='r')

    edge = 100
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=180, interval=60)
    ani.save('animation_lab_4.gif')
