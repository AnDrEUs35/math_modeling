import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def circle_move(t, a, time):
    R = a * t
    alpha = angle_vel * np.pi / 180 * time
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y
    
def animate(i):
    circle.set_data(circle_move(angle_vel=1, f=np.arange(0, 2 * np.pi, 0.01), a=5, t=np.arange(0, 2, 0.01), time=i))


if __name__ == '__main__':
    fig, ax = plt.subplots()
    circle, = plt.plot([], [], '-', color='r', label='ball')

    edge = 20
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=360, interval=30)
    ani.save('animation_lab_2.gif')