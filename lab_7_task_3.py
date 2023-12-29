import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def butterfly_draw(t, e):
    x = np.sin(t) * (e ** np.cos(t) - 2 * np.cos(4*t) + np.sin(t/12) ** 5)
    y = np.cos(t) * (e ** np.cos(t) - 2 * np.cos(4*t) + np.sin(t/12) ** 5)
    return x, y

def animate(i):
    butterfly.set_data(butterfly_draw(t=np.arange(0, 2 * np.pi, 0.01) * np.pi / 180 * i, e=2.7182818284590452353602874713527 ))

if __name__ == '__main__':
    fig, ax = plt.subplots()
    butterfly, = plt.plot([], [], '-', color='r')

    edge = 5
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=360, interval=30)
    ani.save('animation_lab_3.1.gif')







def hearth_draw(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

def animate(i):
    hearth.set_data(hearth_draw(t=np.arange(0, 2 * np.pi, 0.01) * np.pi /180 * i))


if __name__ == '__main__':
    fig, ax = plt.subplots()
    hearth, = plt.plot([], [], '-', color='r', label='ball')

    edge = 20
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=360, interval=30)
    ani.save('animation_lab_3.2.gif')


