import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def drawing(C, D, y0, x0, time):
    xn = x0 * time
    yn = y0 * time 
    x = xn ** 2 - yn ** 2 + C
    y = 2 * xn * yn + D
    return x, y

def animate(i):
    fractal.set_data(drawing(C=0.3, D=0.33, x0=0.1, y0=0.1, time=i))

if __name__ == '__main__':
    fig, ax = plt.subplots()
    fractal, = plt.plot([], [], 'o', color='r', label='ball')

    edge = 10
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=10, interval=30)
    ani.save('animation_lab_4.gif')
