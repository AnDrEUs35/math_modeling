import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 1000, frames)

def move_func(z, t):
    x, y = z
    dXdt = k1 * (A - X - Y)
    dYdt = k2 * (A - X - Y)
    return dXdt, dYdt

k1 = 0.3
k2 = 0.7
A = 100
X = 0
Y = 0

x0 = 0
y0 = 0

z0 = x0, y0

sol = odeint(move_func, z0, t)

def solve_func(i):
    x = sol[:i, 0]
    y = sol[:i, 1]
    return x, y

fig, ax = plt.subplots()
ball_line, = plt.plot([], [], '-', color='r')

def animate(i):
    ball_line.set_data(solve_func(i))
ani = FuncAnimation(fig, animate, frames=frames, interval=100)

edge = 100
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ani.save('lab_11_animation_3.gif')