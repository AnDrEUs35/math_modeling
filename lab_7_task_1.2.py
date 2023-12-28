import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def move(R):
    t = np.linspace(-5 * np.pi, 5 * np.pi, 10000)
    x = R * np.cos(t) ** 3
    y =  R * np.sin(t) ** 3
    return x, y

def animate(i):
    ball.set_data(move(R=2))


if __name__ == '__main__':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r', label='ball')

    edge = 6
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=360, interval=30)
    ani.save('animation_lab_1.2.gif')

