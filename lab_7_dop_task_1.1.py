import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def move1(R, angle_vel, time):
    t = angle_vel * time 
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    return x, y
def move2(R, time, angle_vel):
    t = angle_vel * time 
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    return x, y
def circle_move(R, vx0, time):
    x0 = vx0 * time
    alpha = np.arange(0, 2 * np.pi, 0.1)
    x = x0 + R * np.cos(alpha)
    y = R + R * np.sin(alpha)
    return x, y

x, y = [], []

def animate(i):
    coords = move1(R=2, angle_vel=1, time=i)
    x.append(coords[0])
    y.append(coords[1])

    ball1.set_data(x, y)
    ball2.set_data(move2(R=2, angle_vel=1, time=i))
    circle.set_data(circle_move(R=2, vx0=2, time=i))

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ball1, = plt.plot([],[], '-', color='b', lw=2)
    ball2, = plt.plot([], [], 'o', color='r', lw=2)
    circle, = plt.plot([], [], '-', color='black')




    edge = 20
    plt.axis('equal')
    ax.set_xlim(-2, edge)
    ax.set_ylim(-5, edge)

    ani = FuncAnimation(fig, animate, frames=np.linspace(0, 3*np.pi, 100), interval=30)
    ani.save('animation_dop_lab_1.1.gif')





