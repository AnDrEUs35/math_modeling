import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def drawing1(A1, f1, t):
    y1 = A1 * np.sin(f1 * t)
    x = 5 * t 
    return x, y1
def drawing2(A2, f2, t):
    y2 = A2 * np.sin(f2 * t)
    x = 5 * t
    return x, y2

def animate(i):
    sin1.set_data(drawing1(A1=5, f1=10, t=np.arange(0, 10, 0.01) * np.pi / 180 * i ))
    sin2.set_data(drawing2(A2=5, f2=10, t=np.arange(-10, 0, 0.01) * np.pi / 180 * i ))


if __name__ == '__main__':
    fig, ax = plt.subplots()
    sin1, = plt.plot([], [], '-', color='r')
    sin2, = plt.plot([], [], '-', color='b')

    edge = 30
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=180, interval=60)
    ani.save('project.gif')

