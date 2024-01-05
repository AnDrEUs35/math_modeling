import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def move1(R, angle_vel):
    t = angle_vel * np.pi
    x = R * np.cos(t) ** 3
    y =  R * np.sin(t) ** 3
    return x, y

def move2(R, angle_vel, time):
    t = angle_vel * np.pi / 180 * time
    x = R * np.cos(t) ** 3
    y =  R * np.sin(t) ** 3
    return x, y

def animate(i):
    ball1.set_data(move1(R=2, angle_vel=np.arange(0, np.pi, 0.01)))
    ball2.set_data(move2(R=2, angle_vel=1, time=i))

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ball1, = plt.plot([], [], 'o', color='b', label='ball', lw=3)
    ball2, = plt.plot([], [], 'o', color='r', label='ball', lw=3)
    edge = 6
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=360, interval=30)
    ani.save('animation_dop_lab_1.2.gif')
