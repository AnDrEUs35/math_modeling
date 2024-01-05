import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def move1(R, angle_vel):
    t = angle_vel * np.pi
    x = R * t - R * np.sin(t)
    y = R - R * np.cos(t)
    return x, y
def move2(R, time, angle_vel):
    t = angle_vel * np.pi / 180 * time
    x = R * t - R * np.sin(t)
    y = R - R * np.cos(t)
    return x, y

def animate(i):
    ball1.set_data(move1(R=2, angle_vel=np.arange(0, 1 * np.pi, 0.01)))
    ball2.set_data(move2(R=2, angle_vel=1, time=i))


if __name__ == '__main__':
    fig, ax = plt.subplots()
    ball1, = plt.plot([],[], 'o', color='b', lw=3)
    ball2, = plt.plot([], [], 'o', color='r', lw=3)
    edge = 20
    plt.axis('equal')
    ax.set_xlim(-2, edge)
    ax.set_ylim(-5, edge)

    ani = FuncAnimation(fig, animate, frames=520, interval=30)
    ani.save('animation_dop_lab_1.1.gif')





