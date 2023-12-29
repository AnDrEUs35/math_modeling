import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def move(R, time, angle_vel):
    t = angle_vel * np.pi / 180 * time
    x = R * t - R * np.sin(t)
    y = R - R * np.cos(t)
    return x, y

def animate(i):
    ball.set_data(move(R=2, angle_vel=1, time=i))


if __name__ == '__main__':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r', label='ball')

    edge = 20
    #plt.axis('equal')
    ax.set_xlim(-1, edge)
    ax.set_ylim(-1, edge)

    ani = FuncAnimation(fig, animate, frames=360, interval=30)
    ani.save('animation_lab_1.gif')
