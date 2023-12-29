import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def circle_move(t, a, f):
    R = a * t
    x = R * np.cos(f)
    y = R * np.sin(f)
    return x, y
    
def animate(i):
    circle.set_data(circle_move(a = 5, f = np.arange(0, 2 * np.pi, 0.01), t = 1 * np.pi / 180 * i))


if __name__ == '__main__':
    fig, ax = plt.subplots()
    circle, = plt.plot([], [], '-', color='r', label='circle')

    edge = 20
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=360, interval=30)
    ani.save('animation_lab_2.gif')